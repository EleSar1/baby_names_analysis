import pytest

from ..src.analysis import name_length


def test_name_length_basic():
    
    data = [
        {"Year": "2020", "Gender": "m", "Name": "Luca"},   
        {"Year": "2020", "Gender": "m", "Name": "Marco"},  
        {"Year": "2020", "Gender": "f", "Name": "Anna"},  
        {"Year": "2021", "Gender": "f", "Name": "Giulia"}, 
    ]

    result = name_length(data)

    expected = {
        "2020": {"m": "4.50", "f": "4.00"},
        "2021": {"m": "0.0", "f": "6.00"}
    }

    assert result == expected


def test_name_length_empty_list():
    
    result = name_length([])
    assert result == {}


def test_name_length_missing_key():

    data = [{"Year": "2020", "Gender": "M"}]  # missing "Name"
    with pytest.raises(KeyError):
        name_length(data)


def test_name_length_invalid_input_type():

    with pytest.raises(TypeError):
        name_length("not a list")