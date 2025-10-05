def popular_names(data: list, year: str) -> list:

    """
    Return the 10 most popular names for the specified year.

    Args: 
        data (list): a list of dictionaries, where each dictionary contains a "Year" key and a "Count" key
        representing the number of occurrences.
        year (str): the target year to filter by.

    Returns:
        list: a list cointaning the top 10 dictionaries sorted by "Count" in 
        descending order for the given year. If fewer than 10 exist, returns all the available entries.
        Returns an empty list if no year matches.

    Raises:
        TypeError: if 'data' is not a list or 'year' is not an int.
        ValueError: if the 'Year' field cannot be converted to int.
    """

    if not isinstance(data, list):
        raise TypeError(f"Expected a list for 'data', got {type(data).__name__}.")
    if not isinstance(year, str):
        raise TypeError(f"Expected a str for 'year', got {type(year).__name__}.")

    filtered = []
    for row in data:
        try:
            if row["Year"] == year:
                row = row.copy()
                row["Count"] = int(row["Count"])
                filtered.append(row)
        except ValueError:
            raise ValueError(f"'row[\"Year\"]' or 'row[\"Count\"]' field cannot be converted to type int.")
    
    first_ten = sorted(filtered, key= lambda x: x["Count"], reverse=True)[:10]
    return first_ten


def name_diversity(data: list) -> dict:

    """
    Count the number of unique baby names (male and female) for each year.

    Args:
        data (list): A list of dictionaries, each containing:
            - 'Year': the year of the name,
            - 'Name': the name,
            - 'Gender': the gender,
            - 'Count': the number of occurrences.

    Returns:
        dict: A nested dictionary where each key is a year and the value is another dictionary
        with genders as keys ('m', 'f') and the corresponding value as the count of names
        that occur only once that year.

    Raises:
        TypeError: if 'data' is not a list.
        ValueError: if 'Count' cannot be converted to int.
        KeyError: if required key is missing from data[row].
    """

    if not isinstance(data, list):
        raise TypeError(f"Expected list for 'data', got {type(data).__name__}.")
    
    unique_names: dict[str, dict[str, int]] = {}

    for row in data:
        
        try:
            year = row["Year"]
            gender = row["Gender"].lower()
            count = row["Count"]

        except KeyError as e:
            raise KeyError(f"Missing required key in row: {e}")
        
        if year not in unique_names:
            unique_names[year] = {}

        try:
            if int(count) == 1:
                unique_names[year][gender] = unique_names[year].get(gender, 0) + 1

        except ValueError:
            raise ValueError(f"'row[\"Count\"]' field cannot be converted to type int.")

    for year in unique_names:
        unique_names[year]["m"] = unique_names[year].get("m", 0)
        unique_names[year]["f"] = unique_names[year].get("f", 0)

    return unique_names


def name_length(data: list[dict[str,str]]) -> dict[str, dict[str, float]]:

    """
    Returns the average of the names length for each year.

    Args:
        data (list): a list of dictionaries, where each dictionary contains at least a "Year", "Gender"
        and a "Name" key.

    Returns:
        dict: a nested dictionary representing the average name length per year and gender.

    Raises:
        TypeError: if 'data' is not a list.
        KeyError: if required key is missing from data[row].
    
    """

    if not isinstance(data, list):
        raise TypeError(f"Expected list for 'data', got {type(data).__name__}.")
    
    data_for_year: dict[str, dict[str, list[str]]] = {}
    for row in data:

        try:
            year = row["Year"]
            gender = row["Gender"]
            name = row["Name"]
        except KeyError as e:
            raise KeyError(f"Missing required key in row: {e}")
        
        if year not in data_for_year:
            data_for_year[year] = {}
        
        if gender not in data_for_year[year]:
            data_for_year[year][gender] = []

        data_for_year[year][gender].append(name)

    averages: dict[str, dict[str, float]] = {}
    for year, genders in data_for_year.items():
        averages[year] = {}

        for gen in ["m", "f"]:  
            if gen in genders:
                averages[year][gen] = sum(len(name) for name in genders[gen]) / len(genders[gen])
            else:    
                averages[year][gen] = 0.0

    return averages


def name_endings_analisys(data: list):

    """
    Returns the 5 most popular name, grouping them in their base form (without the last charatcher).
    
    Args:
        data (list): a list of dictionaries, each cointaining at least:
        - 'Name' (str): the name to analyze.
        - 'Count' (int or str convertible to int): the frequency of the name.
    
    Returns:
        list: a list of touple (base_name, frequency), sorted in descending order,
            limited to the 5 most frequent.

    Raises:
        KeyError: if "Name" or "Count" keys are missing from a dictionary.
        ValueError: if 'count_names' cannot be converted to int.
        TypeError: if 'data' is not a list.
    """

    if not isinstance(data, list):
        raise TypeError(f"Expected list for 'data', got {type(data).__name__}.")
    
    most_popular_names = {} 
    for row in data:
        try:
            no_gender_name = row["Name"][:-1]
            count_names = int(row["Count"])
        except KeyError as e:
            raise KeyError(f"Missing required key in row: {e}")
        except ValueError:
            raise ValueError(f"{count_names} could not be cast as int.")
        
        most_popular_names[no_gender_name] = most_popular_names.get(no_gender_name, 0) + count_names

    return sorted(most_popular_names.items(), key=lambda x: x[1], reverse=True)[:5]


def name_popularity_over_decades(data: list[dict[str, str]]) -> dict[str, dict[str, list[tuple[str, int]]]]:

    """
    Returns the 5 most popular female and male names per decade.

    Args:
        data (list[dict[str, str]]): A list of dictionaries, each containing:
            - 'Year' (str): The year of the name.
            - 'Gender' (str): The gender of the name.
            - 'Name' (str): The name to analyze.
            - 'Count' (int or str convertible to int): The frequency of the name.

    Returns:
        dict[str, dict[str, list[tuple[str, int]]]]: A dictionary containing the 5 
        most popular female and male names per decade.

    Raises:
        TypeError: If 'data' is not a list.
        KeyError: If 'Year', 'Name', 'Count', or 'Gender' are missing from a dictionary.
        ValueError: If 'Count' is not convertible to an integer.
    """

    if not isinstance(data, list):
        raise TypeError(f"Expected list for 'data', got {type(data).__name__}.")
    
    names_for_decades = {}
    for row in data:
        try:
            year = row["Year"] 
            gender = row["Gender"]
            name = row["Name"]
            count = int(row["Count"])
        except ValueError:
            raise ValueError(f"{count} could not be cast as int")
        except KeyError as e:
            raise KeyError(f"Missing required key in row: {e}")
        
        decade = year[:3]+"0s"
        if decade not in names_for_decades:
            names_for_decades[decade] = {}

        if gender not in names_for_decades[decade]:
            names_for_decades[decade][gender] = {}

        names_for_decades[decade][gender][name] = names_for_decades[decade][gender].get(name, 0) + count

    for decade in names_for_decades:
        for gender in names_for_decades[decade]:
            top_5_names = sorted(names_for_decades[decade][gender].items(), key=lambda x:x[1], reverse=True)[:5]
            names_for_decades[decade][gender] = top_5_names

    return names_for_decades