from plates import is_valid

def test_max_length():
    assert is_valid("cs1234") == True

def test_min_length():
    assert is_valid("c") == False

def test_alpha_first():
    assert is_valid("c12345") == False

def test_number():
    assert is_valid("cs50p") == False

def test_zero_not_first():
    assert is_valid("cs055") == False

def test_no_punctuation():
    assert is_valid("cS50!") == False

