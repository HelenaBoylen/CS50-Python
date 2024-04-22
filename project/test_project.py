from project import get_last_name, sort_by_last_name, occupied_since, current_location
from datetime import date, datetime
import pytest


def test_get_last_name():
    assert get_last_name("Bob Jones") == "Jones"
    assert get_last_name("Mary Smith") == "Smith"
    assert get_last_name("Mary") != "Smith"
    assert get_last_name("Bob Jones") != "Bob Jones"


def test_sort_by_last_name():
    names = ["Mary Smith", "Bob Jones", "Stephen Davis", "Sue Baker"]
    sorted_names = sort_by_last_name(names)
    assert sorted_names == ["Sue Baker", "Stephen Davis", "Bob Jones", "Mary Smith"]
    names = ["Mary Smith", "Bob Jones", "Stephen Davis", "Sue Baker"]
    sorted_names = sort_by_last_name(names)
    assert sorted_names != ["Mary Smith", "Bob Jones", "Stephen Davis", "Sue Baker"]

def test_occupied_since():
    result = occupied_since()
    start_date = datetime(2000, 11, 2)
    expected_result = (datetime.now() - start_date).days
    assert result == expected_result



