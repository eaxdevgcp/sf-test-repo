# test_calculator.py
from calculator import add, subtract, multiply

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