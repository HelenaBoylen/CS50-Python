from numb3rs import validate

def test_255():
    assert validate("255.255.255.255") == True
    assert validate("355.225.225.225") == False
    assert validate("255.425.525.625") == False
    assert validate("2255.225.225.225") == False

def test_numbers():
    assert validate("hello") == False



