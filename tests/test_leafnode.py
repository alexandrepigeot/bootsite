import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_text_node(self) -> None:
        node: LeafNode = LeafNode(tag="", value="This is a text")

        self.assertEqual("LeafNode(, This is a text, None)", node.__repr__())
        self.assertEqual("This is a text", node.to_html())

    def test_p_node(self) -> None:
        node: LeafNode = LeafNode(tag="p", value="This is a paragraph")

        self.assertEqual("LeafNode(p, This is a paragraph, None)", node.__repr__())
        self.assertEqual("<p>This is a paragraph</p>", node.to_html())

    def test_a_node(self) -> None:
        node: LeafNode = LeafNode(
            tag="a", value="This is a link", props={"href": "http://boot.dev"}
        )

        self.assertEqual(
            "LeafNode(a, This is a link, {'href': 'http://boot.dev'})", node.__repr__()
        )
        self.assertEqual('<a href="http://boot.dev">This is a link</a>', node.to_html())

    def test_img_node(self) -> None:
        node: LeafNode = LeafNode(
            tag="img",
            value="",
            props={"src": "http://boot.dev", "alt": "This is alternate text"},
        )

        self.assertEqual(
            "LeafNode(img, , {'src': 'http://boot.dev', 'alt': 'This is alternate text'})",
            node.__repr__(),
        )
        self.assertEqual(
            '<img src="http://boot.dev" alt="This is alternate text"></img>',
            node.to_html(),
        )


if __name__ == "__main__":
    _ = unittest.main()
