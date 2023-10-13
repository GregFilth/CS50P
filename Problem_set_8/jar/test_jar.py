from jar import Jar
import pytest

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)
        