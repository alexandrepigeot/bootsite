import unittest

from src.split import (
    split_images,
    split_links,
    split_text_nodes,
    split_text_to_text_nodes,
)
from src.textnode import TextNode, TextType


class TestSplit(unittest.TestCase):
    def test_split_text_nodes(self) -> None:
        node = TextNode("text **bold** text", TextType.TEXT)
        expected_nodes = [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(split_text_nodes([node], "**", TextType.BOLD), expected_nodes)

    def test_split_text_nodes_complex(self) -> None:
        node = TextNode("**bold** text **bold** text **bold**", TextType.TEXT)
        expected_nodes = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]

        self.assertEqual(split_text_nodes([node], "**", TextType.BOLD), expected_nodes)

    def test_split_images(self) -> None:
        node = TextNode("![image](source)", TextType.TEXT)
        expected_nodes = [
            TextNode("image", TextType.IMAGE, "source")
        ]

        self.assertEqual(split_images([node]), expected_nodes)

    def test_split_images_complex(self) -> None:
        node = TextNode("![image1](source1) text ![image2](source2) text ![image3](source3)", TextType.TEXT)
        expected_nodes = [
            TextNode("image1", TextType.IMAGE, "source1"),
            TextNode(" text ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "source2"),
            TextNode(" text ", TextType.TEXT),
            TextNode("image3", TextType.IMAGE, "source3")
        ]

        self.assertEqual(split_images([node]), expected_nodes)

    def test_split_links(self) -> None:
        node = TextNode("[link](url)", TextType.TEXT)
        expected_nodes = [
            TextNode("link", TextType.LINK, "url")
        ]

        self.assertEqual(split_links([node]), expected_nodes)

    def test_split_links_complex(self) -> None:
        node = TextNode("[link1](url1) text [link2](url2) text [link3](url3)", TextType.TEXT)
        expected_nodes = [
            TextNode("link1", TextType.LINK, "url1"),
            TextNode(" text ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "url2"),
            TextNode(" text ", TextType.TEXT),
            TextNode("link3", TextType.LINK, "url3")
        ]

        self.assertEqual(split_links([node]), expected_nodes)

    def test_text_to_text_nodes(self) -> None:
        text = "text **bold** text _italic_ text `code` text ![image](source) text [link](url) text"
        expected_nodes =[
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "source"),
            TextNode(" text ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(split_text_to_text_nodes(text), expected_nodes)


if __name__ == "__main__":
    _ = unittest.main()
