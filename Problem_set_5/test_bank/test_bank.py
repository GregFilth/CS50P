from bank import value


def test_h():
    assert value("h") == 20
    assert value("hahahha") == 20
    assert value("HahahahahHa") == 20


def test_hello():
    assert value("hello") == 0
    assert value("HeLlO") == 0


def test_noth():
    assert value("good morning") == 100
    assert value("GoOd MorNiNg") == 100