import unittest
import os
from app.io.input import read_from_file_builtin, read_from_file_pandas
import pandas as pd


class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("Test content")
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("col1,col2\n1,2\n3,4")

    def tearDown(self):
        if os.path.exists("test.txt"):
            os.remove("test.txt")
        if os.path.exists("test.csv"):
            os.remove("test.csv")

    def test_read_from_file_builtin_existing_file(self):
        result = read_from_file_builtin("test.txt")
        self.assertEqual(result, "Test content")

    def test_read_from_file_builtin_empty_file(self):
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("")
        result = read_from_file_builtin("test.txt")
        self.assertEqual(result, "")

    def test_read_from_file_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin("nonexistent.txt")

    def test_read_from_file_pandas_valid_csv(self):
        result = read_from_file_pandas("test.csv")
        expected = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
        pd.testing.assert_frame_equal(result, expected)

    def test_read_from_file_pandas_empty_file(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("")
        with self.assertRaises(pd.errors.EmptyDataError):
            read_from_file_pandas("test.csv")

    def test_read_from_file_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas("nonexistent.csv")


if __name__ == "__main__":
    unittest.main()