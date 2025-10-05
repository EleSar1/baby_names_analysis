import pytest

from src.analysis import name_length


def test_name_length_ok():

    mock_data = [
        {"Name": "Elena", "Year": "2020", "Gender": "f"},
        {"Name": "Marcus", "Year": "2020", "Gender": "m"}
        ]

    result = {
        "2020": {"f": 5, "m": 6}
    }

    assert result == name_length(mock_data)


def test_name_length_without_a_gender_field():

    mock_data = [
        {"Name": "Elena", "Year": "2020", "Gender": "f"}
    ]

    result = {
        "2020": {"f": 5, "m": 0}
    }

    assert result == name_length(mock_data)