import unittest

from src.leafnode import LeafNode
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node1 = TextNode("text", TextType.TEXT)
        node2 = TextNode("text", TextType.TEXT)

        self.assertEqual(node1, node2)

    def test_eq_full(self) -> None:
        node1 = TextNode("text", TextType.TEXT, "url")
        node2 = TextNode("text", TextType.TEXT, "url")

        self.assertEqual(node1, node2)

    def test_eq_different_text(self) -> None:
        node1 = TextNode("text", TextType.TEXT, "url")
        node2 = TextNode("different text", TextType.TEXT, "url")

        self.assertNotEqual(node1, node2)

    def test_eq_different_type(self) -> None:
        node1 = TextNode("text", TextType.TEXT, "url")
        node2 = TextNode("text", TextType.BOLD, "url")

        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self) -> None:
        node1 = TextNode("text", TextType.TEXT, "url")
        node2 = TextNode("text", TextType.TEXT, "different url")

        self.assertNotEqual(node1, node2)

    def test_to_leaf_node_text(self) -> None:
        node = TextNode("text", TextType.TEXT)
        expected_node = LeafNode(tag="", value="text")

        self.assertEqual(node.to_leaf_node(), expected_node)

    def test_to_leaf_node_bold(self) -> None:
        node = TextNode("text", TextType.BOLD)
        expected_node = LeafNode(tag="b", value="text")

        self.assertEqual(node.to_leaf_node(), expected_node)

    def test_to_leaf_node_italic(self) -> None:
        node = TextNode("text", TextType.ITALIC)
        expected_node = LeafNode(tag="i", value="text")

        self.assertEqual(node.to_leaf_node(), expected_node)

    def test_to_leaf_node_code(self) -> None:
        node = TextNode("text", TextType.CODE)
        expected_node = LeafNode(tag="code", value="text")

        self.assertEqual(node.to_leaf_node(), expected_node)

    def test_to_leaf_node_link(self) -> None:
        node = TextNode("text", TextType.LINK, "url")
        expected_node = LeafNode(tag="a", value="text", props={"href": "url"})

        self.assertEqual(node.to_leaf_node(), expected_node)

    def test_to_leaf_node_image(self) -> None:
        node = TextNode("text", TextType.IMAGE, "url")
        expected_node = LeafNode(
            tag="img", value="", props={"alt": "text", "src": "url"}
        )

        self.assertEqual(node.to_leaf_node(), expected_node)


if __name__ == "__main__":
    _ = unittest.main()
