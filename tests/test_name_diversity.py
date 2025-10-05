import pytest

from src.analysis import name_diversity


def test_name_diversity_basic_case():

    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "1", "Gender": "f"},
        {"Name": "Bob", "Year": "2020", "Count": "120", "Gender": "m"},
        {"Name": "Charlie", "Year": "2020", "Count": "1", "Gender": "m"},
        {"Name": "Diana", "Year": "2020", "Count": "85", "Gender": "f"},
        {"Name": "Eve", "Year": "2010", "Count": "70", "Gender": "f"},
        {"Name": "Frank", "Year": "2010", "Count": "1", "Gender": "m"},
        {"Name": "Grace", "Year": "2015", "Count": "60", "Gender": "f"},
        {"Name": "Hank", "Year": "2020", "Count": "55", "Gender": "m"}
    ]

    result = name_diversity(mock_data)
    assert result == {
        "2020": {"m": 1, "f": 1},
        "2015": {"m": 0, "f": 0},
        "2010": {"m": 1, "f": 0}, 
    }


def test_name_diversity_no_unique_names():

    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "3", "Gender": "f"},
        {"Name": "Bob", "Year": "2020", "Count": "120", "Gender": "m"},
        {"Name": "Charlie", "Year": "2020", "Count": "4", "Gender": "m"},
        {"Name": "Diana", "Year": "2020", "Count": "85", "Gender": "f"}
    ]

    result = name_diversity(mock_data)
    assert result == {
        "2020": {"m": 0, "f": 0}
    }


def test_name_diversity_empty_list():

    assert name_diversity([]) == {}


def test_name_diversity_uppercase_gender():

    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "1", "Gender": "F"},
        {"Name": "Bob", "Year": "2020", "Count": "1", "Gender": "M"}
    ]

    result = name_diversity(mock_data)
    assert result == {
        "2020": {"f": 1, "m": 1}
    }


def test_name_diversity_error_raises():

    with pytest.raises(TypeError):
        name_diversity({})

    with pytest.raises(ValueError):
        name_diversity([{"Name": "Alice", "Year": "2020", "Count": "not convertible", "Gender": "f"}])

    with pytest.raises(KeyError):
        name_diversity([{"Name": "Alice", "y": "2020", "c": "14", "g": "f"}])