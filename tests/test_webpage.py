import unittest

from src.webpage import extract_title


class TestWebpage(unittest.TestCase):
    def test_extract_title(self) -> None:
        markdown = """
# Title

This is a paragraph.
"""
        expected_title = "Title"

        self.assertEqual(extract_title(markdown), expected_title)

    def test_extract_title_multiple(self) -> None:
        markdown = """
# Title

# Title again

This is a paragraph.
"""
        self.assertRaises(SyntaxError, extract_title, markdown)

    def test_extract_title_missing(self) -> None:
        markdown = """
This is a paragraph.

This is a paragraph.
"""

        self.assertRaises(SyntaxError, extract_title, markdown)


if __name__ == "__main__":
    _ = unittest.main()
