import pandas as pd

def read_from_console():
    """
    Reads text input from the console.

    Returns:
        str: The text entered by the user
    """
    return input("Enter text: ")


def read_from_file_builtin(filepath):
    """
    Reads content from a file using Python's built-in capabilities.

    Args:
        filepath (str): Path to the file to be read

    Returns:
        str: The content read from the file

    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(filepath):
    """
    Reads content from a file using the pandas library.

    Args:
        filepath (str): Path to the CSV file to be read

    Returns:
        pandas.DataFrame: The data read from the CSV file

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        pandas.errors.EmptyDataError: If the CSV file is empty
    """
    return pd.read_csv(filepath)