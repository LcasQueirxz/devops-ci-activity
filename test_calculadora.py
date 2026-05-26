import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 5) == -5

**3. Arquivo:** `requirements.txt`
* Texto para colar:
```text
pytest==7.4.0
