from bank import value

# check hello or Hello
def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

# check first letter starts with H
def test_h_():
    assert value("hi") == 20
    assert value("hiya") == 20
    assert value("hallo") == 20
    assert value("Hallo") == 20

# check non-hello answers
def test_abc():
    assert value("abc") == 100
    assert value("ciao") == 100
    assert value("") == 100
