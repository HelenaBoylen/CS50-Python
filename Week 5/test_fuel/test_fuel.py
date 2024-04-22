from fuel import convert
from fuel import gauge
import pytest

def test_convert_fraction():
    assert convert ("1/3") == 33
    assert convert ("1/2") == 50
    assert convert ("1/4") == 25

def test_percentage():
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"

def test_full_empty():
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_alpha():
    with pytest.raises(ValueError):
        convert("hello/there")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")



