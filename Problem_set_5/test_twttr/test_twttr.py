from twttr import shorten


def test_capital():
    assert shorten("AsEsOsIsUs") == "sssss"
    assert shorten("AEOIU") == ""


def test_lowercase():
    assert shorten("aSeSoSiSuS") == "SSSSS"
    assert shorten("aeoiu") == ""

def test_empty():
    assert shorten("") == ""
    assert shorten("SSSSSS") == "SSSSSS"


def test_numbers():
    assert shorten("0123456789") == "0123456789"


def test_punct_specchar():
    assert shorten("@/&%$§!=)(/?`*'+#") == "@/&%$§!=)(/?`*'+#"
