import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self) -> None:
        node: ParentNode = ParentNode(tag="div", children=[])

        self.assertEqual("ParentNode(div, [], None)", node.__repr__())
        self.assertEqual("<div></div>", node.to_html())
        self.assertEqual("", node.props_to_html())

    def test_parent_of_parents_node(self) -> None:
        node: ParentNode = ParentNode(
            tag="div",
            children=[
                ParentNode(tag="div", children=[]),
                ParentNode(tag="div", children=[]),
            ],
        )

        self.assertEqual(
            "ParentNode(div, [ParentNode(div, [], None), ParentNode(div, [], None)], None)",
            node.__repr__(),
        )
        self.assertEqual("<div><div></div><div></div></div>", node.to_html())
        self.assertEqual("", node.props_to_html())

    def test_parent_of_leaves_node(self) -> None:
        node: ParentNode = ParentNode(
            tag="div",
            children=[
                LeafNode(tag="p", value="This is a paragraph"),
                LeafNode(tag="p", value="This is a paragraph"),
            ],
        )

        self.assertEqual(
            "ParentNode(div, [LeafNode(p, This is a paragraph, None), LeafNode(p, This is a paragraph, None)], None)",
            node.__repr__(),
        )
        self.assertEqual(
            "<div><p>This is a paragraph</p><p>This is a paragraph</p></div>",
            node.to_html(),
        )
        self.assertEqual("", node.props_to_html())

    def test_parent_with_props(self) -> None:
        node: ParentNode = ParentNode(
            tag="div", children=[], props={"key": "attribute"}
        )

        self.assertEqual("ParentNode(div, [], {'key': 'attribute'})", node.__repr__())
        self.assertEqual('<div key="attribute"></div>', node.to_html())
        self.assertEqual(' key="attribute"', node.props_to_html())

    def test_empty_tag(self) -> None:
        node: ParentNode = ParentNode(tag="", children=[])

        self.assertEqual("ParentNode(, [], None)", node.__repr__())
        self.assertRaises(ValueError, node.to_html)
        self.assertEqual("", node.props_to_html())


if __name__ == "__main__":
    _ = unittest.main()
