import seasons
from datetime import date
import pytest


def test_correct():
    assert seasons.calculate("2000-01-01") == "twelve million, seven hundred eighty-one thousand, four hundred forty"

def test_format():
    with pytest.raises(SystemExit):
        seasons.calculate("1st January 2020")


