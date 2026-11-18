# Fixture Scope

## Concepto
Demuestra el uso de `scope="session"` en una fixture de pytest: el fixture se crea una sola vez para toda la corrida en vez de reconstruirse en cada test.

## Qué demuestra el código
- `src/main.py`: mini API con FastAPI (`/ping` y `/health`).
- `tests/test_api.py`: define un fixture `client` con `scope="session"` que envuelve un `TestClient` de FastAPI, y lo reutiliza en `test_ping` y `test_health` sin recrearlo.

## Cómo correrlo
```
pip install -r requirements.txt
```
Y desde esta carpeta:
```
pytest
```
