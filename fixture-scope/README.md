# Fixture Scope

## Concept
Demonstrates `scope="session"` on a pytest fixture: the fixture is created once for the whole run instead of being rebuilt for every test.

## What the code demonstrates
- `src/main.py`: a mini FastAPI API (`/ping` and `/health`).
- `tests/test_api.py`: defines a `client` fixture with `scope="session"` that wraps a FastAPI `TestClient`, reused in `test_ping` and `test_health` without recreating it.

## How to run it
```
pip install -r requirements.txt
```
Then, from this folder:
```
pytest
```
