from working import convert
import pytest


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"


def test_valueerror_convert():
    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 9 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 9:60 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 9 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 9:00 PM")

    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat AM to 9 PM")
    with pytest.raises(ValueError):
        convert("9 AM to cat PM")
        
    with pytest.raises(ValueError):
        convert("10:00 to 9 PM")
    with pytest.raises(ValueError):
        convert("10 to 9 PM")
    with pytest.raises(ValueError):
        convert("10 AM to 9:00")
    with pytest.raises(ValueError):
        convert("10:00 AM to 9:00")
