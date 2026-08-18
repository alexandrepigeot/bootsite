import unittest

from src.leafnode import LeafNode
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_plain_node(self) -> None:
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)

        self.assertEqual("TextNode(This is a text node, text, None)", node1.__repr__())
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(tag="", value="This is a text node"), node1.to_leaf_node()
        )

    def test_bold_node(self):
        node1 = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)

        self.assertEqual(
            "TextNode(This is a bold text node, bold, None)", node1.__repr__()
        )
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(tag="b", value="This is a bold text node"), node1.to_leaf_node()
        )

    def test_italic_node(self):
        node1 = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)

        self.assertEqual(
            "TextNode(This is an italic text node, italic, None)", node1.__repr__()
        )
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(tag="i", value="This is an italic text node"), node1.to_leaf_node()
        )

    def test_code_node(self):
        node1 = TextNode("This is a code text node", TextType.CODE)
        node2 = TextNode("This is a code text node", TextType.CODE)

        self.assertEqual(
            "TextNode(This is a code text node, code, None)", node1.__repr__()
        )
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(tag="code", value="This is a code text node"), node1.to_leaf_node()
        )

    def test_link_node(self):
        node1 = TextNode("This is a link text node", TextType.LINK, "http://boot.dev")
        node2 = TextNode("This is a link text node", TextType.LINK, "http://boot.dev")

        self.assertEqual(
            "TextNode(This is a link text node, link, http://boot.dev)",
            node1.__repr__(),
        )
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(
                tag="a",
                value="This is a link text node",
                props={"href": "http://boot.dev"},
            ),
            node1.to_leaf_node(),
        )

    def test_image_node(self):
        node1 = TextNode(
            "This is an image text node", TextType.IMAGE, "http://boot.dev/image.png"
        )
        node2 = TextNode(
            "This is an image text node", TextType.IMAGE, "http://boot.dev/image.png"
        )

        self.assertEqual(
            "TextNode(This is an image text node, image, http://boot.dev/image.png)",
            node1.__repr__(),
        )
        self.assertEqual(node1, node2)
        self.assertEqual(
            LeafNode(
                tag="img",
                value="",
                props={
                    "alt": "This is an image text node",
                    "src": "http://boot.dev/image.png",
                },
            ),
            node1.to_leaf_node(),
        )

    def test_text_not_eq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This one has a different text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_text_type_not_eq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_not_eq(self):
        node1 = TextNode("This is a text node", TextType.TEXT, "http://boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "http://localhost")
        self.assertNotEqual(node1, node2)

    def test_default_url(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    _ = unittest.main()
