import pytest
from operazioni import somma


def test_somma_interi():
    assert somma(-3, 2) == -1


def test_somma_float_e_int():
    assert somma(2.5, 2) == 4.5


def test_somma_divisione():
    assert somma(3 / 2.5, 1) == (3 / 2.5) + 1

