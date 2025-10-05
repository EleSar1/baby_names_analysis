import pytest

from src.analysis import popular_names

def test_basic_case():
    
    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "150"},
        {"Name": "Bob", "Year": "2020", "Count": "120"},
        {"Name": "Charlie", "Year": "2020", "Count": "90"},
        {"Name": "Diana", "Year": "2020", "Count": "85"},
        {"Name": "Eve", "Year": "2020", "Count": "70"},
        {"Name": "Frank", "Year": "2020", "Count": "65"},
        {"Name": "Grace", "Year": "2020", "Count": "60"},
        {"Name": "Hank", "Year": "2020", "Count": "55"},
        {"Name": "Ivy", "Year": "2020", "Count": "50"},
        {"Name": "Jack", "Year": "2020", "Count": "45"},
        {"Name": "Karl", "Year": "2020", "Count": "40"},
        {"Name": "Laura", "Year": "2019", "Count": "200"},
        {"Name": "Mike", "Year": "2019", "Count": "180"},
    ]

    result = popular_names(mock_data, "2020")
    assert len(result) == 10
    assert result[0]["Name"] == "Alice"
    assert result[0]["Count"] == 150
    assert result[-1]["Name"] == "Jack"
    assert result[-1]["Count"] == 45


def test_less_than_10():

    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "150"},
        {"Name": "Bob", "Year": "2020", "Count": "120"},
        {"Name": "Charlie", "Year": "2021", "Count": "90"}
    ]

    result = popular_names(mock_data, "2020")
    assert len(result) == 2
    assert result[0]["Name"] == "Alice"
    assert result[1]["Name"] == "Bob"


def test_empty_list():

    result = popular_names([], "2020")
    assert result == []


def test_mixed_count_type():

    mock_data = [
        {"Name": "Alice", "Year": "2020", "Count": "150"},
        {"Name": "Bob", "Year": "2020", "Count": 120},
        {"Name": "Charlie", "Year": "2021", "Count": 90}
    ]

    result = popular_names(mock_data, "2020")
    assert type(result[0]["Count"]) == int
    assert type(result[1]["Count"]) == int
    assert result[0]["Count"] == 150
    assert result[1]["Count"] == 120


def test_no_matching_year():

    mock_data = [{"Name": "Alice", "Year": "1999", "Count": "150"}]

    result = popular_names(mock_data, "2020")
    assert result == []


def test_type_errors():

    with pytest.raises(TypeError):
        popular_names("not a list", "2020")

    with pytest.raises(TypeError):
        popular_names([], 2020)


def test_value_error_count_not_convertible():

    mock_data = [{"Name": "Alice", "Year": "2020", "Count": "not convertible"}]

    with pytest.raises(ValueError):
        popular_names(mock_data, "2020")
    