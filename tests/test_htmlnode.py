import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_div_node(self) -> None:
        node: HTMLNode = HTMLNode(tag="div")

        self.assertEqual("HTMLNode(div, None, None, None)", node.__repr__())
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual("", node.props_to_html())

    def test_p_node(self) -> None:
        node: HTMLNode = HTMLNode(tag="p", value="This is a paragraph")

        self.assertEqual(
            "HTMLNode(p, This is a paragraph, None, None)", node.__repr__()
        )
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual("", node.props_to_html())

    def test_a_node(self) -> None:
        node: HTMLNode = HTMLNode(
            tag="a", value="This is a link", props={"href": "http://boot.dev"}
        )

        self.assertEqual(
            "HTMLNode(a, This is a link, None, {'href': 'http://boot.dev'})",
            node.__repr__(),
        )
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(' href="http://boot.dev"', node.props_to_html())

    def test_parent_div_node(self) -> None:
        node: HTMLNode = HTMLNode(
            tag="div",
            children=[
                HTMLNode(tag="p", value="This is a paragraph"),
                HTMLNode(tag="p", value="This is a paragraph"),
            ],
        )

        self.assertEqual(
            "HTMLNode(div, None, [HTMLNode(p, This is a paragraph, None, None), HTMLNode(p, This is a paragraph, None, None)], None)",
            node.__repr__(),
        )
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual("", node.props_to_html())

    def test_img_node(self) -> None:
        node: HTMLNode = HTMLNode(
            tag="img", value="This is alternate text", props={"src": "http://boot.dev"}
        )

        self.assertEqual(
            "HTMLNode(img, This is alternate text, None, {'src': 'http://boot.dev'})",
            node.__repr__(),
        )
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(' src="http://boot.dev"', node.props_to_html())


if __name__ == "__main__":
    _ = unittest.main()
