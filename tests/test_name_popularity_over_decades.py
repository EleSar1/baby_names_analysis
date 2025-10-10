import pytest

from ..src.analysis import name_popularity_over_decades


def test_raises_type_error():
    with pytest.raises(TypeError):
        name_popularity_over_decades("not a list")


def test_raises_key_error():
    data = [{"Year": "1990", "Gender": "F", "Count": "10"}]  #'Name' is missing
    with pytest.raises(KeyError):
        name_popularity_over_decades(data)


def test_raises_value_error():
    data = [{"Year": "1990", "Gender": "M", "Name": "John", "Count": "abc"}]
    with pytest.raises(ValueError):
        name_popularity_over_decades(data)


def test_returns_top_5_per_decade():
    data = [
        {"Year": "1991", "Gender": "M", "Name": "John", "Count": "50"},
        {"Year": "1993", "Gender": "M", "Name": "Mark", "Count": "30"},
        {"Year": "1999", "Gender": "F", "Name": "Anna", "Count": "60"},
        {"Year": "1998", "Gender": "F", "Name": "Mary", "Count": "40"},
        {"Year": "1985", "Gender": "M", "Name": "Paul", "Count": "20"},
    ]

    result = name_popularity_over_decades(data)

    assert "1990s" in result
    assert "1980s" in result
    assert isinstance(result["1990s"]["M"], list)
    assert result["1990s"]["F"][0][0] == "Anna"