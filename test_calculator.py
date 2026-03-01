# test_calculator.py
import pytest # Se necesita para testear excepciones
from calculator import add, subtract, multiply, divide # Se agrega 'divide'

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
    assert divide(5, 2) == 2.5
    assert divide(10, 1) == 10.0
    assert divide(0, 5) == 0.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0
    assert divide(7, 3) == pytest.approx(2.3333333333333335) # Usar pytest.approx para floats

    # Caso de división por cero
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)