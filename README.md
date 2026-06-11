# secure-api

A Python microservice built with FastAPI. The main point of this project is the CI/CD pipeline — every push to main runs security checks automatically, and if anything fails, deployment is blocked.

## What the pipeline does

If any stage fails, everything after it is cancelled. Nothing reaches deploy unless it passes all four checks.

## Security decisions worth noting

- Multi-stage Docker build — the final image doesn't include pip, gcc or any build tools, which cuts down the CVE surface significantly
- Container runs as a non-root user (`appuser`) rather than root
- Gitleaks uses `fetch-depth: 0` to scan the full commit history, not just the latest snapshot — so secrets that were committed and then deleted are still caught

## Stack

| Tool | Purpose |
|------|---------|
| FastAPI | Web framework |
| pytest + httpx | Async integration tests |
| Docker | Containerisation |
| Trivy | Container vulnerability scanning |
| Gitleaks | Secret and credential detection |
| GitHub Actions | Pipeline orchestration |

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Runs at `http://localhost:8000` — Swagger UI at `http://localhost:8000/docs`

## Tests

```bash
pytest tests/ -v
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Returns service status |
| GET | `/api/v1/health` | Health check endpoint |