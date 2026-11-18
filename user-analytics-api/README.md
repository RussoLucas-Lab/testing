# User Analytics API

## Concept
Testing a FastAPI API with `TestClient`, mocking slow/external dependencies with `monkeypatch` (including an `autouse` fixture), handling environment variables, and file uploads.

## What the code demonstrates
- `src/main.py`: endpoints `/user/{id}/profile`, `/user/{id}/files`, `/user/{id}/file` (upload), `/analytics/sales`, and `/analytics/stock`. The analytics endpoints simulate slow/external calls with `time.sleep` and a `SALES_DB_ENABLED` environment variable.
- `tests/conftest.py`: a session-scoped `client` fixture with `TestClient`.
- `tests/test_analytics_endpoints.py`: an `autouse` fixture that neutralizes `process_request_context` (avoiding the `sleep` in every test in the file) and uses `monkeypatch` to simulate success, failure, and the `SALES_DB_ENABLED` flag for the sales fetch, without waiting out the real delays.
- `tests/test_upload_files.py`: a session fixture that creates a temporary file with `tmp_path_factory` and uploads it to the upload endpoint.
- `tests/test_user_endpoints.py`: simple tests for the profile and files endpoints.

## How to run it
```
pip install -r requirements.txt
```
Then, from this folder:
```
pytest
```
