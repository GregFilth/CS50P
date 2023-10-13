from seasons import Minutes
from datetime import date


def test_delta():
    assert Minutes.delta(Minutes, date(2023, 9, 30), date(2023, 9, 29)) == 1440
    assert Minutes.delta(Minutes, date(2023, 9, 30), date(2023, 8, 30)) == 44640
    assert Minutes.delta(Minutes, date(2023, 9, 30), date(2020, 9, 30)) == 1576800
    assert Minutes.delta(Minutes, date(2023, 9, 30), date(2019, 9, 30)) == 2103840

def test_convert():
    assert Minutes.convert(Minutes, 1440) == "One thousand, four hundred forty"
    assert Minutes.convert(Minutes, 44640) == "Forty-four thousand, six hundred forty"
    assert Minutes.convert(Minutes, 1576800) == "One million, five hundred seventy-six thousand, eight hundred"
    assert Minutes.convert(Minutes, 2103840) == "Two million, one hundred three thousand, eight hundred forty"
