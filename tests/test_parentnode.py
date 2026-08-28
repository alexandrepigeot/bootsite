import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_eq(self) -> None:
        node1 = ParentNode(
            tag="tag",
            children=[LeafNode(tag="tag", value="value")],
            props={"prop": "attribute"},
        )
        node2 = ParentNode(
            tag="tag",
            children=[LeafNode(tag="tag", value="value")],
            props={"prop": "attribute"},
        )

        self.assertEqual(node1, node2)

    def test_to_html(self) -> None:
        node = ParentNode(tag="tag", children=[LeafNode(tag="childtag", value="value")])
        expected_html = "<tag><childtag>value</childtag></tag>"

        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_props(self) -> None:
        node = ParentNode(
            tag="tag",
            children=[LeafNode(tag="childtag", value="value", props={"prop": "attribute"})],
            props={"prop": "attribute"},
        )
        expected_html = (
            '<tag prop="attribute"><childtag prop="attribute">value</childtag></tag>'
        )

        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_empty_children(self) -> None:
        node = ParentNode(tag="tag", children=[])
        expected_html = "<tag></tag>"

        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_empty_tag(self) -> None:
        node = ParentNode(tag="", children=[LeafNode(tag="childtag", value="value")])

        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    _ = unittest.main()
