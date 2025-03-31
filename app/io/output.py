def write_to_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): Text to be printed

    Returns:
        None
    """
    print(text)


def write_to_file_builtin(filepath, text):
    """
    Writes content to a file using Python's built-in capabilities.

    Args:
        filepath (str): Path to the file where text will be written
        text (str): Text to be written to the file

    Returns:
        None

    Raises:
        IOError: If there's an error writing to the file
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)