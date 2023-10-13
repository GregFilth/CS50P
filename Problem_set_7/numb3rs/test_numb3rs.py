from numb3rs import validate


def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

    assert validate("512.512.512.512") == False

    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False

    assert validate("a.1.1.1") == False
    assert validate("1.a.1.1") == False
    assert validate("1.1.a.1") == False
    assert validate("1.1.1.a") == False

    assert validate("1.1.1") == False

    assert validate("256.256.256.256") == False

    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

    assert validate("cat") == False
    