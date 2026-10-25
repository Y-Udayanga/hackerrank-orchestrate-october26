# GhostTrace AI — Evidence-Driven Deletion Auditor

A runnable Python CLI that audits deletion requests using participant evidence. It never deletes source data. It produces the challenge CSV and a proof-carrying remediation plan.

## Setup

Python 3.11+ is required. From the repository root:

```console
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Set `GEMINI_API_KEY` in your process environment, or in an ignored root `.env`. Never commit or package credentials. `GEMINI_MODEL` selects the model; leaving it blank prefers the successfully tested Gemini 3.1 Flash-Lite if available, otherwise an available stable Flash candidate after API discovery. A model appearing in discovery does not guarantee generation entitlement; API errors remain visible. `--model` overrides the environment for a run.

```console
python code/main.py --list-models
python code/main.py --model gemini-3.1-flash-lite
```

The default run reads `dataset/deletion_requests.csv`, validates its 518 rows, and atomically writes root `output.csv`. Inputs are never modified. Full processing fails on unreadable/corrupt evidence or API failure unless reduced-capability processing is explicitly selected.

```console
python code/main.py --offline --allow-evidence-errors
```

Offline mode is deliberately labeled reduced capability: it has conservative multilingual lexical intent handling and cannot interpret screenshots. Missing evidence prevents unsupported COMPLETE judgments. It is useful for debugging, not an equivalent substitute for the hybrid run.

## How it works

The logical agents are small Python modules: request intent, exact historical identity resolution, evidence retrieval, temporal reconstruction, deterministic policy, flow/restore risk, remediation planning, and output validation. See `ARCHITECTURE.md` and `code/evaluation/dataset_inspection.md` for the observed schemas and design.

Evidence adapters handle nested JSON, seven log layouts, SQLite tables and JSON columns, text, CSV, PDFs, and Gemini screenshot interpretation. The index is built once. Resource state must be supported by evidence whose event and capture times are both at/before the individual audit cutoff. File origins and reported workflow status do not prove ownership or deletion. Only exact identifiers and explicit resource relationships establish subject links; similar names and numeric suffixes do not.

`dataset/deletion_rules.csv` remains the policy authority. Unsupported rule conditions fail visibly. Retention, tombstones, replication, synchronization and backup restore access are handled separately. The tool writes plans only; it has no deletion-execution capability.

## Evaluation and tests

```console
python -m pytest -q
python code/inspect_dataset.py
python code/main.py --requests sample_deletion_requests.csv --output .cache/sample_output.csv
python code/evaluation/main.py --label hybrid-evaluation
```

The evaluator alone reads `dataset/sample_output.csv`. It reports status accuracy/confusion, unordered six-field step precision/recall/F1, field accuracy, exact ordered sequences, format failures, and every sample mismatch. Independent synthetic tests are separate from challenge cases. Reference answer IDs, states and resource mappings are never used in the prediction modules.

Reports are in `code/evaluation/`: `evaluation_report.md`, `usage_report.md`, `history.md`, `custom_cases.md`, `ingestion_report.md`, and `dataset_inspection.md`. Required evaluation/usage reports are also placed at archive root `evaluation/` when packaging to satisfy both repository layouts.

## Gemini reliability and cost

The maintained `google-genai` SDK uses stateless Interactions by default (`store=False`), JSON Schema plus Pydantic validation, low thinking effort, timeout, bounded exponential retries, and serial calls. Set `GEMINI_API=generate_content` for the supported legacy endpoint. Stable extraction caches are keyed by content, prompt/schema version and model; deleting `.cache/gemini/` forces new calls. The cache is local and excluded from the submission archive.

`GEMINI_TIMEOUT_MS` defaults to 60000 and `GEMINI_MAX_RETRIES` to 3 (bounded at 5). Optional `GEMINI_INPUT_USD_PER_MILLION` and `GEMINI_OUTPUT_USD_PER_MILLION` override cost estimates. Without verified rates cost is reported unknown. Tokens come from response usage metadata; failed calls without usage are not fabricated. The final report distinguishes input, output, thinking, cache hits and discovery calls. Warm-cache runs can incur zero generation tokens even though cached model work was done earlier.

SDK references: [structured output](https://ai.google.dev/gemini-api/docs/structured-output), [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview), and [pricing](https://ai.google.dev/gemini-api/docs/pricing). Prices must be rechecked when the model or billing date changes.

## Limitations and defensible interpretation

This is a challenge auditor, not a legal-compliance certification. It does not infer a missing record from a partial snapshot or connect anonymous resources by case numbers/timing coincidence. If a required subject link or proof is unavailable, diagnostics record an investigation gap. Because the output contract has no UNKNOWN status, an authorized audit with insufficient proof is marked INCOMPLETE without invented findings. Ambiguous authorization yields NOT_APPLICABLE and an internal diagnostic. These conservative decisions may differ from public references; the report gives measured performance rather than a leaderboard guarantee.

Per-case diagnostics and the evidence ledger are written to ignored `.cache/run/`. They are useful for review but excluded from `code.zip`. No arbitrary confidence columns are added to the output.

## Packaging and trace

```console
python code/package_submission.py
```

The allowlisted archive contains runnable source, tests, prompts (in source), configuration examples, documentation and evaluation reports. It excludes dataset/, caches, virtual environments, `.env`, nested archives and credentials. Submit root `output.csv`, `code.zip`, and root `log.txt` separately.

For the complete structured trace, finish and close this Codex session first, then use `code/export_trace.py` with the relevant rollout path. Review the redacted staged trace before upload. This live session cannot honestly package its own final, flushed raw trace before it ends. See `agent_trace_instructions.md`.

[Official challenge and submission](https://www.hackerrank.com/contests/hackerrank-orchestrate-october26/challenges/ghost-data-still-exists)
