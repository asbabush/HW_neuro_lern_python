import pytest
from hw1_ababushkin.logic import modify_data_to_human


def test_modify_data_to_human():
    test_data = data = {
        "monday": [],
        "tuesday": [{"type": "open", "value": 3600}, {"type": "close", "value": 32400}],
        "wednesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 32400},
        ],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}],
        "saturday": [
            {"type": "close", "value": 82800},
            {"type": "close", "value": 3600},
            {"type": "open", "value": 32400},
            {"type": "close", "value": 39600},
            {"type": "open", "value": 57600},
        ],
        "sunday": [],
    }
    actual = modify_data_to_human(test_data)
    expected = "monday: close\ntuesday: 01:00 AM - 09:00 AM\nwednesday: 01:00 AM - 09:00 AM\nthursday: close\nfriday: 18:00 PM - 01:00 AM\nsaturday: 09:00 AM - 11:00 AM, 16:00 PM - 23:00 PM\nsunday: close\n"

    assert actual == expected
