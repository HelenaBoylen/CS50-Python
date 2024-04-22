from um import count
import pytest


def main():
    test_um()
    test_case()
    test_spaces()


def test_um():
    assert count("hello, um, world") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0

def test_case():
    assert count("Um, thanks, um") == 2
    assert count("UM, THANKS, UM") == 2
    assert count("Um, thanks, um") == 2


def test_spaces():
    assert count(" um ") == 1
    assert count("umum") == 0
    assert count("um um") == 2
