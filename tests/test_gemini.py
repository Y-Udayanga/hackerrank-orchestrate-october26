from types import SimpleNamespace
import pytest
from ghosttrace.gemini import Gemini
from ghosttrace.types import Intent


def client_fixture(monkeypatch,tmp_path,responses):
    from google import genai
    monkeypatch.setenv('GEMINI_API_KEY','unit-test-placeholder')
    monkeypatch.setenv('GEMINI_MODEL','gemini-3.1-flash-lite')
    monkeypatch.setenv('GEMINI_API','interactions')
    monkeypatch.setenv('GEMINI_MAX_RETRIES','3')
    monkeypatch.setattr('ghosttrace.gemini.time.sleep',lambda _:None)
    calls=[]
    def create(**kwargs):
        calls.append(kwargs)
        response=responses.pop(0)
        if isinstance(response,Exception):raise response
        return response
    fake=SimpleNamespace(models=SimpleNamespace(list=lambda:[SimpleNamespace(name='models/gemini-3.1-flash-lite',supported_actions=['generateContent'])]),
                         interactions=SimpleNamespace(create=create))
    monkeypatch.setattr(genai,'Client',lambda **_:fake)
    return Gemini(tmp_path),calls


def response(text='{"intent":"DELETE_REQUEST","quote":"delete","reason":"explicit"}'):
    usage=SimpleNamespace(total_input_tokens=10,total_output_tokens=5,total_thought_tokens=2,total_cached_tokens=0,total_tokens=17)
    usage.model_dump=lambda:{'total_input_tokens':10,'total_output_tokens':5,'total_thought_tokens':2,'total_tokens':17}
    return SimpleNamespace(output_text=text,usage=usage)


def test_actual_metadata_and_schema_validated_cache(monkeypatch,tmp_path):
    model,calls=client_fixture(monkeypatch,tmp_path,[response()])
    assert model.generate('delete',Intent)==model.generate('delete',Intent)
    assert len(calls)==1 and model.usage['cache_hits']==1
    assert model.usage['reported_total_tokens']==17
    assert model.usage['thinking_tokens']==2
    assert calls[0]['store'] is False
    assert calls[0]['response_format']['schema']==Intent.model_json_schema()


def test_bounded_transient_retry(monkeypatch,tmp_path):
    class Temporary(Exception):
        code=503
    model,calls=client_fixture(monkeypatch,tmp_path,[Temporary(),Temporary(),response()])
    model.generate('delete',Intent)
    assert len(calls)==3 and model.usage['failed_calls']==2


def test_invalid_response_never_enters_cache(monkeypatch,tmp_path):
    model,_=client_fixture(monkeypatch,tmp_path,[response('{"intent":"invented"}')])
    with pytest.raises(RuntimeError):model.generate('delete',Intent)
    assert not list(tmp_path.glob('*.json'))
    assert model.usage['input_tokens']==10


def test_api_secret_is_redacted(monkeypatch,tmp_path):
    class Denied(Exception):
        code=401
        message='rejected unit-test-placeholder'
    model,_=client_fixture(monkeypatch,tmp_path,[Denied()])
    with pytest.raises(RuntimeError) as exc:model.generate('delete',Intent)
    assert 'unit-test-placeholder' not in str(exc.value)
