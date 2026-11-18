# pftracker (Personal Finance Tracker)

## Concepto
Proyecto más grande que funciona como repaso integral de pytest: fixtures de distinto scope, `parametrize`, `pytest-mock` (fixture `mocker`), `monkeypatch`, `caplog`, `tmp_path`/`tmp_path_factory` y configuración vía `pytest.ini`.

## Qué demuestra el código
- `pftracker/`: paquete con `PersonalFinanceTracker` (categorías, transacciones, presupuestos mensuales y balance en moneda base), `storage.py` (backend `JsonFileStorage` con lock de archivo y escritura atómica) y `fx.py` (conversión de moneda vía `ECBRateProvider`, que usa el paquete `currency_converter`).
- `tests/conftest.py`: fixtures `storage` y `tracker` (este último mockea el `exchange_provider` con `mocker.Mock()` para no depender de la red), y `clean_db`, un fixture no-op requerido por `usefixtures` en `pytest.ini`.
- `tests/test_main.py`: suite grande organizada en clases (`TestCategories`, `TestTransactions`, `TestBudget`, `TestConversions`, `TestDefaultCurrency`, `TestLogging`, `TestPersistence`), con parametrización, mocking de `ECBRateProvider` vía `mocker.patch(..., autospec=True)`, `monkeypatch.setenv`, `caplog` y fixtures de scope `class` para probar persistencia entre instancias.
- `tests/test_json_file_storage.py`: mockea `os.getpid` para verificar el contenido del lockfile.
- `pytest.ini`: fija `addopts = -v`, `testpaths = tests` y `usefixtures = clean_db`.

## Cómo correrlo
```
pip install -r requirements.txt
```
Y desde esta carpeta:
```
pytest
```
