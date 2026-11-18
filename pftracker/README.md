# pftracker (Personal Finance Tracker)

## Concept
A larger project that serves as a comprehensive review of pytest: fixtures with different scopes, `parametrize`, `pytest-mock` (the `mocker` fixture), `monkeypatch`, `caplog`, `tmp_path`/`tmp_path_factory`, and configuration via `pytest.ini`.

## What the code demonstrates
- `pftracker/`: a package with `PersonalFinanceTracker` (categories, transactions, monthly budgets, and balance in a base currency), `storage.py` (a `JsonFileStorage` backend with file locking and atomic writes), and `fx.py` (currency conversion via `ECBRateProvider`, which uses the `currency_converter` package).
- `tests/conftest.py`: `storage` and `tracker` fixtures (the latter mocks `exchange_provider` with `mocker.Mock()` to avoid depending on the network), and `clean_db`, a no-op fixture required by `usefixtures` in `pytest.ini`.
- `tests/test_main.py`: a large suite organized into classes (`TestCategories`, `TestTransactions`, `TestBudget`, `TestConversions`, `TestDefaultCurrency`, `TestLogging`, `TestPersistence`), with parametrization, mocking `ECBRateProvider` via `mocker.patch(..., autospec=True)`, `monkeypatch.setenv`, `caplog`, and class-scoped fixtures to test persistence across instances.
- `tests/test_json_file_storage.py`: mocks `os.getpid` to verify the lockfile's contents.
- `pytest.ini`: sets `addopts = -v`, `testpaths = tests`, and `usefixtures = clean_db`.

## How to run it
```
pip install -r requirements.txt
```
Then, from this folder:
```
pytest
```
