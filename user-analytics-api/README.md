# User Analytics API

## Concepto
Testing de una API FastAPI con `TestClient`, mockeo de dependencias lentas/externas con `monkeypatch` (incluido un fixture `autouse`), manejo de variables de entorno y upload de archivos.

## Qué demuestra el código
- `src/main.py`: endpoints `/user/{id}/profile`, `/user/{id}/files`, `/user/{id}/file` (upload), `/analytics/sales` y `/analytics/stock`. Los endpoints de analytics simulan llamadas lentas/externas con `time.sleep` y una variable de entorno `SALES_DB_ENABLED`.
- `tests/conftest.py`: fixture `client` de `scope="session"` con `TestClient`.
- `tests/test_analytics_endpoints.py`: fixture `autouse` que neutraliza `process_request_context` (evita el `sleep` en todos los tests del archivo) y usa `monkeypatch` para simular éxito, fallo y el flag `SALES_DB_ENABLED` del fetch de ventas, sin esperar los tiempos reales.
- `tests/test_upload_files.py`: fixture de sesión que crea un archivo temporal con `tmp_path_factory` y lo sube al endpoint de upload.
- `tests/test_user_endpoints.py`: tests simples de los endpoints de perfil y archivos.

## Cómo correrlo
```
pip install -r requirements.txt
```
Y desde esta carpeta:
```
pytest
```
