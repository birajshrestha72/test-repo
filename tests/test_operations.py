from calculator.operations import add
from calculator.operations import subtract
from calculator.operations import multiple
from calculator.operations import power


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(4, 5) == -1


def test_multiple():
    assert multiple(4, 5) == 20


def test_power():
    assert power(2, 2) == 4
