# project-one

A minimal FastAPI service, the repository of the Project One pod of AI Pods.

## Commands

| Purpose | Command |
|---|---|
| Install | `uv sync --frozen` |
| Lint | `uv run ruff check .` and `uv run ruff format --check .` |
| Test | `uv run pytest` |
| Run | `uv run uvicorn app.main:app --reload` |

## Endpoints

- `GET /health`: liveness probe.
- `GET /hello?name=Ada`: greeting.
