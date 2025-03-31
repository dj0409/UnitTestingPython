# test_people_formatter.py

import pytest
from people_formatter import format_data_for_display

# 🔹 Fixture that prepares sample input data
@pytest.fixture
def sample_people():
    return [
        {"given_name": "Bruce", "family_name": "Wayne", "title": "CEO"},
        {"given_name": "Clark", "family_name": "Kent", "title": "Reporter"},
    ]

# 🔸 Test using the fixture
def test_format_data_for_display(sample_people):
    expected = [
        "Bruce Wayne: CEO",
        "Clark Kent: Reporter"
    ]
    result = format_data_for_display(sample_people)
    assert result == expected
