# Document Editor

## Concepto
Capítulo introductorio de testing unitario con pytest: asserts básicos, `pytest.raises` para excepciones, y `pytest.mark.xfail` para documentar un bug conocido sin romper la suite.

## Qué demuestra el código
- `src/main.py`: clase `DocumentEditor` con `write`, `clear`, `is_empty` y `get_last_content`. Tiene un bug intencional: `history.append(self.content)` se ejecuta *antes* de actualizar `content`, por lo que `get_last_content()` siempre devuelve el contenido anterior al último `write`.
- `tests/test_main.py`: cubre los casos normales de la clase y usa `@pytest.mark.xfail` sobre `test_get_last_content` para dejar constancia del bug sin que falle el pipeline, además de `pytest.raises` para el caso de historial vacío.

## Cómo correrlo
No hay dependencias externas, solo pytest:
```
pip install -r requirements.txt
```
Y desde esta carpeta:
```
pytest
```
