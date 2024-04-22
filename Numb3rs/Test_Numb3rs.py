from Numb3rs import validate


def test_one():
    assert validate("1.1.1.1") == True


def test_two():
    assert validate("1.1.1.256") == False
    assert validate("a.b.c.d") == False
    assert validate("abcd") == False
