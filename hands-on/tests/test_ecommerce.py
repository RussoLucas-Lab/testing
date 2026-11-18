from datetime import datetime

import pytest

from src.ecommerce import OrderError, Product, process_order


# Empezamos sencillo, probando la función en sí
def test_process_order():
    product = Product(name="cheese", price=10000, stock=50)

    order_meta = process_order(
        product=product, quantity=10, is_premium_user=False, order_time=datetime.now()
    )

    assert order_meta["product"] == "cheese"
    assert order_meta["quantity"] == 10
    assert order_meta["total"] == 10000 * 10


def test_premium_user():
    product = Product(name="cheese", price=10000, stock=50)

    order_meta = process_order(
        product=product, quantity=10, is_premium_user=True, order_time=datetime.now()
    )

    assert order_meta["product"] == "cheese"
    assert order_meta["total"] == (10000 * 10 * 0.9)


def test_too_large_order():
    product = Product(name="cheese", price=10000, stock=10)

    # Los errores los testeamos con with, donde encapsulamos la funcion a testear
    with pytest.raises(OrderError):
        process_order(
            product=product, quantity=10000, is_premium_user=True, order_time=datetime.now()
        )


def test_too_little_quantity():
    product = Product(name="cheese", price=10000, stock=10)

    with pytest.raises(OrderError):
        process_order(
            product=product, quantity=-100, is_premium_user=True, order_time=datetime.now()
        )
