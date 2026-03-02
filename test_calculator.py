# test_calculator.py
import pytest  # Necesario para pytest.raises
from calculator import add, subtract, multiply, divide  # Se añade 'divide'


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0
    assert multiply(-2, 4) == -8
    assert multiply(-3, -5) == 15
    assert multiply(1, 10) == 10


def test_divide():
    # Casos de división normal
    assert divide(6, 3) == 2.0
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(-8, 2) == -4.0
    assert divide(9, -3) == -3.0
    assert divide(-10, -5) == 2.0
    assert divide(0, 5) == 0.0

    # Caso de división por cero (debe lanzar ZeroDivisionError)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)
