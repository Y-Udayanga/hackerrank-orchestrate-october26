# Final run usage report

Mode: Gemini hybrid. Requests: 518. Evidence ingestion failures: 0.

| Metric | Actual value |
|---|---:|
| provider | Google Gemini |
| model | gemini-3.1-flash-lite |
| calls | 0 |
| failed_calls | 0 |
| input_tokens | 0 |
| output_tokens | 0 |
| thinking_tokens | 0 |
| cached_input_tokens | 0 |
| cache_hits | 22 |
| discovery_calls | 1 |
| reported_total_tokens | 0 |

Total generated/request tokens including reported thinking: 0.
Average per request: 0.000.
Estimated total and per-request cost: USD 0.00000000; USD 0.00000000 per request

Price source: https://ai.google.dev/gemini-api/docs/pricing (verified 2026-10-25).
The standard text/image rates used for Gemini 3.1 Flash-Lite are USD 0.25 input
and USD 1.50 output (including thinking) per million tokens. Gemini 3.8 Flash
introductory rates expire 2026-12-31; reverify them for later runs.

One provider/model only; the table also represents overall totals. Cache hits make
no model call and incur no new tokens. Discovery is separately counted. Failed
calls with no usage metadata have unknown provider-side token usage; recorded
tokens are the actual returned metadata, not estimates of unreported usage.
Inference is serial (concurrency 1), with bounded retry and per-call timeout.
Thinking tokens are reported separately and included once in total and output cost.
Coding-assistant usage is not available through this application and is excluded.
Earlier cache-preparation calls are also excluded from these final-run totals.
This is a warm-cache execution cost, not a cold-start project cost.
