import unittest

from get_content import extract_title

class TestGetContent(unittest.TestCase):
    def test_extract_title_invalid(self):
        md = "Hello"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_empty(self):
        md = ""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)

        self.assertEqual(title, "Hello")

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        with self.assertRaises(Exception):
            extract_title(
                """
no title
"""
            )


if __name__ == "__main__":
    unittest.main()
