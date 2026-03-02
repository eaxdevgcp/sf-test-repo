# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

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
    # Casos básicos
    assert divide(6, 3) == 2.0
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5 # Resultado flotante
    assert divide(7, 1) == 7.0

    # Casos con números negativos
    assert divide(-6, 3) == -2.0
    assert divide(6, -3) == -2.0
    assert divide(-6, -3) == 2.0
    assert divide(0, 5) == 0.0 # División de cero por un número

def test_divide_by_zero():
    # Verificar que se lanza ZeroDivisionError al dividir por cero
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        divide(-5, 0)