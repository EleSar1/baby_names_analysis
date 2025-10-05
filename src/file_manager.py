import csv

def read_file(file_path: str) -> list[dict[str,str]]:

    """
    Read a CSV file and return its contents as a list of dictionaries.
    
    Each row of the CSV will be represented as a dictionary where
    the keys are the column headers and the values are the row entries.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        list[dict[str, str]]: A list of dictionaries containing the CSV data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        csv.Error: If there is an error while parsing the CSV file.
    """

    with open(file_path, newline="") as file:
        try:
            file_data = csv.DictReader(file, delimiter=",")

            data = []
            for row in file_data:
                data.append(row)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")
        except csv.Error as e:
            raise csv.Error(f"{file_path}, line {file_data.line_num}: {e}")
        
    return data