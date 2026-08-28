import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self) -> None:
        node1 = LeafNode(tag="tag", value="value", props={"prop": "attribute"})
        node2 = LeafNode(tag="tag", value="value", props={"prop": "attribute"})

        self.assertEqual(node1, node2)

    def test_to_html(self) -> None:
        node = LeafNode(tag="tag", value="value")
        expected_html = "<tag>value</tag>"

        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_props(self) -> None:
        node = LeafNode(tag="tag", value="value", props={"prop": "attribute"})
        expected_html = '<tag prop="attribute">value</tag>'

        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self) -> None:
        node = LeafNode(tag="", value="value")
        expected_html = "value"

        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    _ = unittest.main()
