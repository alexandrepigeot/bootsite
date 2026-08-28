import unittest

from src.image import Image


class TestImage(unittest.TestCase):
    def test_eq(self) -> None:
        node1 = Image("alternate text", "source url")
        node2 = Image("alternate text", "source url")

        self.assertEqual(node1, node2)

    def test_eq_different_alt(self) -> None:
        node1 = Image("alternate text", "source url")
        node2 = Image("different alternate text", "source url")

        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self) -> None:
        node1 = Image("alternate text", "source url")
        node2 = Image("alternate text", "different source url")

        self.assertNotEqual(node1, node2)

    def test_to_markdown(self) -> None:
        node = Image("alternate text", "source url")
        expected_markdown = "![alternate text](source url)"

        self.assertEqual(node.to_markdown(), expected_markdown)


if __name__ == "__main__":
    _ = unittest.main()
