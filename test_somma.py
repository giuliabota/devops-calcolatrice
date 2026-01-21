import pytest
from operazioni import somma


def test_somma_interi():
    assert somma(-3, 2) == -1


def test_somma_float_e_int():
    assert somma(2.5, 2) == 4.5


def test_somma_divisione():
    assert somma(3 / 2.5, 1) == (3 / 2.5) + 1


def test_somma_a_non_numero():
    assert somma("a", 2.5) == "A is Not a number"


def test_somma_b_non_numero():
    assert somma(3, "+") == "B is Not a number"