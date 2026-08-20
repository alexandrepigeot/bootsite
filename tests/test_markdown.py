import unittest

from src.markdown import ImageNode, LinkNode, extract_images, split_nodes
from src.textnode import TextNode, TextType


class TestMarkdown(unittest.TestCase):
    def test_image_node(self):
        node1: ImageNode = ImageNode("alternate text", "source url")
        node2: ImageNode = ImageNode("alternate text", "source url")

        self.assertEqual("ImageNode(alternate text, source url)", node1.__repr__())
        self.assertEqual(node1, node2)

    def test_link_node(self):
        node1: LinkNode = LinkNode(text="This is text", url="http://boot.dev")
        node2: LinkNode = LinkNode(text="This is text", url="http://boot.dev")

        self.assertEqual("LinkNode(This is text, http://boot.dev)", node1.__repr__())
        self.assertEqual(node1, node2)

    def test_extract_images(self) -> None:
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_nodes: list[ImageNode] = extract_images(text)
        expected_nodes: list[ImageNode] = [
            ImageNode(alt="rick roll", src="https://i.imgur.com/aKaOqIh.gif"),
            ImageNode(alt="obi wan", src="https://i.imgur.com/fJRm4Vk.jpeg")
        ]

        self.assertEqual(expected_nodes, extracted_nodes)

    def test_split_text_node(self) -> None:
        node: TextNode = TextNode(text="This is a text", text_type=TextType.TEXT)

        self.assertEqual([node], split_nodes([node], "**", TextType.BOLD))

    def test_split_bold_node(self) -> None:
        node: TextNode = TextNode(
            text="This is a **bold** text", text_type=TextType.TEXT
        )

        self.assertEqual(
            [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="bold", text_type=TextType.BOLD),
                TextNode(text=" text", text_type=TextType.TEXT),
            ],
            split_nodes([node], "**", TextType.BOLD),
        )

    def test_split_complex_bold_nodes(self) -> None:
        nodes: list[TextNode] = [
            TextNode(text="**bold**", text_type=TextType.TEXT),
            TextNode(text="This is **bold**", text_type=TextType.TEXT),
            TextNode(text="**This** is bold", text_type=TextType.TEXT),
        ]

        self.assertEqual(
            [
                TextNode(text="bold", text_type=TextType.BOLD),
                TextNode(text="This is ", text_type=TextType.TEXT),
                TextNode(text="bold", text_type=TextType.BOLD),
                TextNode(text="This", text_type=TextType.BOLD),
                TextNode(text=" is bold", text_type=TextType.TEXT),
            ],
            split_nodes(old_nodes=nodes, delimiter="**", text_type=TextType.BOLD),
        )

    def test_split_invalid_node(self) -> None:
        node: TextNode = TextNode(text="**", text_type=TextType.TEXT)

        self.assertRaises(SyntaxError, split_nodes, [node], "**", TextType.BOLD)
