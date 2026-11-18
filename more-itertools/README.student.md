# more-itertools — notas del curso

Esta carpeta es la librería open-source [`more-itertools`](https://github.com/more-itertools/more-itertools) vendorizada tal cual, usada como "sandbox" para practicar cómo escribir tests contra una librería de terceros real. El `README.rst` original y el resto del código **no son material del curso** y no deben modificarse.

El único archivo propio del curso es `tests/test_custom.py`.

## Qué demuestra `tests/test_custom.py`
- `test_partition*`: prueba `more_itertools.partition`, que separa un iterable en dos listas según un predicado (incluyendo el caso de predicado `None` y de iterable vacío).
- `test_interleave*`: prueba `more_itertools.interleave`, que combina varios iterables intercalando sus elementos (incluyendo listas de distinta longitud).

## Cómo correrlo
```
pip install -e .
pip install pytest
```
Y desde esta carpeta:
```
pytest tests/test_custom.py
```
