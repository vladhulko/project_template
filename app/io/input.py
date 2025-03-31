import pandas as pd


def read_from_console():
    return input("Enter text: ")


def read_from_file_builtin(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(filepath):
    return pd.read_csv(filepath)
