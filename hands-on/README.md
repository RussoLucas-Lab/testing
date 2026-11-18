# Hands-on: E-commerce Order Processing

## Concept
Hands-on unit-testing exercise on a business function with several branches (discounts, stock, expedited shipping), covering both happy and error paths with `pytest.raises`.

## What the code demonstrates
- `src/ecommerce.py`: `process_order` calculates an order's total (with a discount for premium users), validates stock/quantity, and estimates the delivery date based on the order's time.
- `tests/test_ecommerce.py`: cases for a simple order, a premium user, a quantity above available stock, and an invalid (negative) quantity.
- `worker.feature`: an empty Gherkin file (placeholder). No `pytest-bdd` is installed and no tests reference it, so it isn't part of the executable suite for now.

## How to run it
No external dependencies, just pytest:
```
pip install -r requirements.txt
```
Then, from this folder:
```
pytest
```
