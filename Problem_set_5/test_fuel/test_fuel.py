from fuel import convert
from fuel import gauge
import pytest


def test_notint_convert():
    with pytest.raises(ValueError):
        convert("2/dog")
    with pytest.raises(ValueError):
        convert("dog/2")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("2c/3d")


def test_ygreaterx_convert():
    with pytest.raises(ValueError):
        convert("3/2")


def test_dividebyzero_convert():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_convert():
    assert convert("1/2") == 50
    assert convert("0/2") == 0
    assert convert("2/2") == 100


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
