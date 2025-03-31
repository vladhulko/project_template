from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import write_to_console, write_to_file_builtin


def main():
    console_text = read_from_console()
    write_to_console(console_text)
    write_to_file_builtin("console_output.txt", console_text)

    builtin_text = read_from_file_builtin("input.txt")
    write_to_console(builtin_text)
    write_to_file_builtin("builtin_output.txt", builtin_text)

    pandas_df = read_from_file_pandas("data.csv")
    write_to_console(pandas_df)
    write_to_file_builtin("pandas_output.txt", str(pandas_df))


if __name__ == '__main__':
    main()