"""Official Google GenAI client: bounded calls, validated schemas, content cache."""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from pydantic import BaseModel

PROMPT_VERSION = 'ghosttrace-1'


class Gemini:
    def __init__(self, cache: Path):
        from google import genai
        from google.genai import types
        key = os.environ.get('GEMINI_API_KEY')
        if not key:
            raise RuntimeError('GEMINI_API_KEY unavailable. Configure it or explicitly select --offline.')
        self.client = genai.Client(api_key=key, http_options=types.HttpOptions(
            timeout=int(os.getenv('GEMINI_TIMEOUT_MS', '60000')),
            retry_options=types.HttpRetryOptions(attempts=1)))
        self.cache = cache
        cache.mkdir(parents=True, exist_ok=True)
        self.usage = {'provider': 'Google Gemini', 'model': '', 'calls': 0, 'failed_calls': 0,
                      'input_tokens': 0, 'output_tokens': 0, 'thinking_tokens': 0,
                      'cached_input_tokens': 0, 'cache_hits': 0, 'discovery_calls': 0}
        self.usage['discovery_calls'] += 1
        try:
            models = list(self.client.models.list())
        except Exception as exc:
            raise RuntimeError('Gemini model discovery failed; no inference performed. Error type: '
                               + type(exc).__name__) from None
        supported = sorted(m.name.removeprefix('models/') for m in models
                           if 'generateContent' in (m.supported_actions or []) and 'gemini' in m.name)
        configured = os.getenv('GEMINI_MODEL', '').removeprefix('models/')
        if configured and configured not in supported:
            raise RuntimeError('Configured GEMINI_MODEL not available for generateContent')
        candidates = [m for m in supported if 'flash' in m and not any(
            s in m for s in ('image', 'audio', 'tts', 'live', 'robotics', 'preview', 'exp', 'lite'))]
        if not configured and not candidates:
            raise RuntimeError('No stable Flash text/vision candidate found; explicitly set GEMINI_MODEL')
        # Selection is from actual access, never an assumed model name.
        self.model = configured or sorted(candidates, reverse=True)[0]
        self.available_models = supported
        self.usage['model'] = self.model

    def generate(self, prompt: str, schema: type[BaseModel], data: bytes | None = None,
                 mime_type: str = 'image/png') -> BaseModel:
        from google.genai import types
        signature = json.dumps([self.model, PROMPT_VERSION, prompt, schema.model_json_schema()], sort_keys=True)
        key = hashlib.sha256(signature.encode() + (data or b'')).hexdigest()
        path = self.cache / (key + '.json')
        if path.exists():
            try:
                result = schema.model_validate_json(path.read_text(encoding='utf-8'))
                self.usage['cache_hits'] += 1
                return result
            except (ValueError, OSError):
                pass
        contents = [prompt]
        if data:
            contents.append(types.Part.from_bytes(data=data, mime_type=mime_type))
        attempts = min(5, max(1, int(os.getenv('GEMINI_MAX_RETRIES', '3'))))
        for attempt in range(attempts):
            self.usage['calls'] += 1
            try:
                response = self.client.models.generate_content(model=self.model, contents=contents,
                    config=types.GenerateContentConfig(temperature=0, response_mime_type='application/json',
                        response_json_schema=schema.model_json_schema(), automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)))
                usage = response.usage_metadata
                for target, source in [('input_tokens', 'prompt_token_count'), ('output_tokens', 'candidates_token_count'),
                                       ('thinking_tokens', 'thoughts_token_count'), ('cached_input_tokens', 'cached_content_token_count')]:
                    self.usage[target] += (getattr(usage, source, 0) or 0)
                result = schema.model_validate_json(response.text)
                tmp = path.with_suffix('.tmp')
                tmp.write_text(result.model_dump_json(), encoding='utf-8')
                tmp.replace(path)
                return result
            except Exception as exc:
                self.usage['failed_calls'] += 1
                code = getattr(exc, 'code', None)
                transient = code in {429, 500, 502, 503, 504} or isinstance(exc, (TimeoutError, ConnectionError))
                transient |= type(exc).__name__ in {'ReadTimeout', 'ConnectTimeout', 'RemoteProtocolError'}
                if not transient or attempt + 1 == attempts:
                    message=str(getattr(exc,'message',''))
                    secret=os.environ.get('GEMINI_API_KEY','')
                    if secret:message=message.replace(secret,'[REDACTED]')
                    raise RuntimeError('Gemini request failed: ' + type(exc).__name__+' '+message[:500]) from None
                time.sleep(min(2 ** attempt, 8))
        raise RuntimeError('Unreachable retry state')

    def cost(self):
        rates = [os.getenv('GEMINI_INPUT_USD_PER_MILLION'), os.getenv('GEMINI_OUTPUT_USD_PER_MILLION')]
        if not all(rates):
            return None
        return (self.usage['input_tokens'] * float(rates[0]) +
                (self.usage['output_tokens'] + self.usage['thinking_tokens']) * float(rates[1])) / 1_000_000
