def write_to_console(text):
    print(text)


def write_to_file_builtin(filepath, text):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)
