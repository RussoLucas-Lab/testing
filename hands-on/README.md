# Hands-on: E-commerce Order Processing

## Concepto
Ejercicio práctico de testing unitario sobre una función de negocio con varias ramas (descuentos, stock, envío expedito), cubriendo casos felices y de error con `pytest.raises`.

## Qué demuestra el código
- `src/ecommerce.py`: `process_order` calcula el total de una orden (con descuento para usuarios premium), valida stock/cantidad y estima la fecha de entrega según la hora del pedido.
- `tests/test_ecommerce.py`: casos para orden simple, usuario premium, cantidad mayor al stock disponible y cantidad inválida (negativa).
- `worker.feature`: archivo Gherkin vacío (placeholder). No hay `pytest-bdd` instalado ni tests que lo referencien, así que por ahora no forma parte de la suite ejecutable.

## Cómo correrlo
No hay dependencias externas, solo pytest:
```
pip install -r requirements.txt
```
Y desde esta carpeta:
```
pytest
```
