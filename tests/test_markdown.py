import unittest

from src.markdown import split_nodes
from src.textnode import TextNode, TextType


class TestMarkdown(unittest.TestCase):
    def test_split_text_node(self):
        node: TextNode = TextNode(text="This is a text", text_type=TextType.TEXT)

        self.assertEqual([node], split_nodes([node], "**", TextType.BOLD))

    def test_split_bold_node(self):
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

    def test_split_complex_bold_nodes(self):
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

    def test_split_invalid_node(self):
        node: TextNode = TextNode(text="**", text_type=TextType.TEXT)

        self.assertRaises(SyntaxError, split_nodes, [node], "**", TextType.BOLD)
