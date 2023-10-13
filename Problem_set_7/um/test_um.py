from um import count

def test_count():

    assert count("Asdum, asdUm, umAsd, Umasd") == 0

    assert count("Asd, um, asdum, umasd, asd") == 1

    assert count("Um, asdum, umasd, um") == 2

    assert count("um, Um, uM, asdum, asdUM, asdUm, asduM") == 3

    assert count("Um, um Um uM UM um, um, asd, asdum, asduM") == 7