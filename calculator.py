# calculator.py
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divide dos números enteros y retorna el resultado como un flotante.
    Lanza ZeroDivisionError si b es cero.
    """
    return a / b