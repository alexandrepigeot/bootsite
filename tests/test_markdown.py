import unittest

from src.image import Image
from src.link import Link
from src.markdown import (
    extract_images,
    extract_links,
    markdown_to_blocks,
    split_images,
    split_links,
    split_nodes,
    text_to_text_nodes,
)
from src.textnode import TextNode, TextType


class TestMarkdown(unittest.TestCase):
    def test_extract_images(self) -> None:
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_nodes: list[Image] = extract_images(text)
        expected_nodes: list[Image] = [
            Image(alt="rick roll", url="https://i.imgur.com/aKaOqIh.gif"),
            Image(alt="obi wan", url="https://i.imgur.com/fJRm4Vk.jpeg"),
        ]

        self.assertEqual(expected_nodes, extracted_nodes)

    def test_extract_links(self) -> None:
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_nodes = extract_links(text)
        expected_nodes: list[Link] = [
            Link(text="rick roll", url="https://i.imgur.com/aKaOqIh.gif"),
            Link(text="obi wan", url="https://i.imgur.com/fJRm4Vk.jpeg"),
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

    def test_split_image(self) -> None:
        nodes = [
            TextNode(
                text="This is a text with an ![image](http://boot.dev) for sure",
                text_type=TextType.TEXT,
            )
        ]

        self.assertEqual(
            [
                TextNode(text="This is a text with an ", text_type=TextType.TEXT),
                TextNode(text="image", text_type=TextType.IMAGE, url="http://boot.dev"),
                TextNode(text=" for sure", text_type=TextType.TEXT),
            ],
            split_images(nodes),
        )

    def test_complex_split_images(self) -> None:
        nodes = [
            TextNode(
                text="![image1](source1) something ![image2](source2) something ![image3](source3)",
                text_type=TextType.TEXT,
            )
        ]

        self.assertEqual(
            [
                TextNode("image1", TextType.IMAGE, "source1"),
                TextNode(" something ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "source2"),
                TextNode(" something ", TextType.TEXT),
                TextNode("image3", TextType.IMAGE, "source3"),
            ],
            split_images(nodes),
        )

    def test_split_link(self) -> None:
        nodes = [
            TextNode(text="This is a [link](href) for sure", text_type=TextType.TEXT)
        ]

        self.assertEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, url="href"),
                TextNode(" for sure", TextType.TEXT),
            ],
            split_links(nodes),
        )

    def test_complex_split_links(self) -> None:
        nodes = [
            TextNode(
                text="[link1](href1) something [link2](href2) something [link3](href3)",
                text_type=TextType.TEXT,
            )
        ]

        self.assertEqual(
            [
                TextNode("link1", TextType.LINK, "href1"),
                TextNode(" something ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "href2"),
                TextNode(" something ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "href3"),
            ],
            split_links(nodes),
        )

    def test_text_to_text_nodes(self) -> None:
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(nodes, text_to_text_nodes(text))

    def test_markdown_to_blocks(self) -> None:
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""

        self.assertEqual([
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ], markdown_to_blocks(text))


if __name__ == "__main__":
    _ = unittest.main()
