import unittest

from src.link import Link, extract_links


class TestLink(unittest.TestCase):
    def test_eq(self) -> None:
        node1 = Link("text", "url")
        node2 = Link("text", "url")

        self.assertEqual(node1, node2)

    def test_eq_different_text(self) -> None:
        node1 = Link("text", "url")
        node2 = Link("different text", "url")

        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self) -> None:
        node1 = Link("text", "url")
        node2 = Link("text", "different url")

        self.assertNotEqual(node1, node2)

    def test_to_markdown(self) -> None:
        node = Link("text", "url")
        expected_markdown = "[text](url)"

        self.assertEqual(node.to_markdown(), expected_markdown)

    def test_extract_links(self) -> None:
        text = "[content](href)"
        expected_links = [Link(text="content", url="href")]

        self.assertEqual(extract_links(text), expected_links)

    def test_extract_links_complex(self) -> None:
        text = "[content1](href1) text [content2](href2) text [content3](href3)"
        expected_links = [
            Link(text="content1", url="href1"),
            Link(text="content2", url="href2"),
            Link(text="content3", url="href3"),
        ]

        self.assertEqual(extract_links(text), expected_links)

    def test_extract_links_none(self) -> None:

        text = "text"
        expected_links = []

        self.assertEqual(extract_links(text), expected_links)


if __name__ == "__main__":
    _ = unittest.main()
