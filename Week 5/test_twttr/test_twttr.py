from twttr import shorten

# check uppercase
def test_uppercase():
    assert shorten("HARVARD") == "HRVRD"

# check lowercase
def test_lowercase():
    assert shorten("harvard") == "hrvrd"

# check capitalisation
def test_capitalising():
    assert shorten("Harvard") == "Hrvrd"

# check numbers
def test_numbers():
    assert shorten("123") == "123"

# check punctuation
def test_punctuation():
    assert shorten("!?,.") == "!?,."
