import pytest
from operazioni import sottrazione


def test_sottrazione_interi():
    assert sottrazione(-3, 2) == -5


def test_sottrazione_float_e_int():
    assert sottrazione(2.5, 2) == 0.5


def test_sottrazione_divisione():
    assert sottrazione(3 / 2.5, 1) == (3 / 2.5) - 1



