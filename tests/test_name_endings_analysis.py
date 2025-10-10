import pytest

from ..src.analysis import name_endings_analysis


def test_name_endings_analysis_base_case():

    data = [
            {"Year": "2020", "Gender": "m", "Name": "Giulio", "Count": 50},   
            {"Year": "2020", "Gender": "m", "Name": "Francesco", "Count": 22},  
            {"Year": "2020", "Gender": "f", "Name": "Francesca", "Count": 94},  
            {"Year": "2021", "Gender": "f", "Name": "Giulia", "Count": 43},
            {"Year": "2021", "Gender": "m", "Name": "Maria", "Count": 67},
            {"Year": "2021", "Gender": "f", "Name": "Minerva", "Count": 15}
        ]

    result = name_endings_analysis(data)
    expected_result = [("Francesc", 116), ("Giuli", 93), ("Mari", 67), ("Minerv", 15)]
    assert result == expected_result


def test_sum_count_for_different_year():

    data = [
            {"Year": "2020", "Gender": "m", "Name": "Giulio", "Count": 50},   
            {"Year": "2020", "Gender": "m", "Name": "Francesco", "Count": 22},  
            {"Year": "2020", "Gender": "f", "Name": "Francesca", "Count": 94},  
            {"Year": "2020", "Gender": "f", "Name": "Giulia", "Count": 43},
            {"Year": "2021", "Gender": "f", "Name": "Giulia", "Count": 67},
            {"Year": "2021", "Gender": "m", "Name": "Francesco", "Count": 15}
        ]
    
    result = name_endings_analysis(data)
    expected_result = [("Giuli", 160), ("Francesc", 131)]
    assert result == expected_result


def test_empty_data():

    assert name_endings_analysis([]) == []


def test_cast_count_to_str_to_int():

    data = [
            {"Year": "2020", "Gender": "m", "Name": "Giulio", "Count": "50"},   
            {"Year": "2020", "Gender": "m", "Name": "Francesco", "Count": "22"}
        ]
    
    result = name_endings_analysis(data)
    expected_result = [("Giuli", 50), ("Francesc", 22)]
    assert result == expected_result


def test_raises_type_error():

    with pytest.raises(TypeError):
        name_endings_analysis("Not a list")


def test_raises_value_error():

    with pytest.raises(ValueError):
        name_endings_analysis([{"Count": "not convertible", "Name": "Anna"}])


def test_raises_key_error():

    with pytest.raises(KeyError):
        name_endings_analysis([{"Name": "Anna"}]) #"Count" not found