import pytest
from operazioni import sottrazione


def test_sottrazione_interi():
    assert sottrazione(-3, 2) == -5


def test_sottrazione_float_e_int():
    assert sottrazione(2.5, 2) == 0.5


def test_sottrazione_divisione():
    assert sottrazione(3 / 2.5, 1) == (3 / 2.5) - 1


def test_sottrazione_a_non_numero():
    assert sottrazione("a", 2.5) == "A is Not a number"


def test_sottrazione_b_non_numero():
    assert sottrazione(3, "+") == "B is Not a number"
