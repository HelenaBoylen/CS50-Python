from working import convert
import pytest

# check times are converting properly
def test_valid_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

# check 12hr v 24hr format with AM/PM
def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5 PM to 7 PM")

# check hrs > 12 in AM and mins > 59
def test_outside_range():
    with pytest.raises(ValueError):
        convert("13:00 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 5:60 PM")
