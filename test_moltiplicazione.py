from operazioni import moltiplicazione

def test_moltiplicazione_positivi():
    assert moltiplicazione(3, 4) == 12
    assert moltiplicazione(10, 5) == 50

def test_moltiplicazione_zero():
    assert moltiplicazione(10, 0) == 0
    assert moltiplicazione(0, 5) == 0

def test_moltiplicazione_negativi():
    assert moltiplicazione(-3, 4) == -12
    assert moltiplicazione(-2, -5) == 10

def test_moltiplicazione_float():
    assert moltiplicazione(2.5, 2) == 5.0