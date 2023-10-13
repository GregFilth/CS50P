from plates import is_valid


def test_startwithtwoletters():
    assert is_valid("1250") == False
    assert is_valid("CS50") == True
    assert is_valid("C150") == False
    assert is_valid("1G50") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("CSSSSS") == True
    assert is_valid("CSSSSSS") == False
    assert is_valid("CSSSSSSSSSSSSSSSSSS") == False


def test_numinmiddle():
    assert is_valid("AAA2") == True
    assert is_valid("AAA0") == False
    assert is_valid("AA02") == False
    assert is_valid("AA2A") == False


def test_specchar():
    assert is_valid("AA.2") == False
    assert is_valid("AA 2") == False
    assert is_valid("AA?") == False
    assert is_valid("AA,2") == False
    assert is_valid("AA?2") == False
