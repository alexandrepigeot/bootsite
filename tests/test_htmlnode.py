import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_generic_nodes(self):
        generic_tag: str = "p"
        node_with_tag: HTMLNode = HTMLNode(tag=generic_tag)
        generic_value: str = "This is some text"
        node_with_value: HTMLNode = HTMLNode(value=generic_value)
        generic_children: list[HTMLNode] = [node_with_tag, node_with_value]
        node_with_children: HTMLNode = HTMLNode(children=generic_children)
        generic_props: dict[str, str] = {"href": "/styles", "a": "http://boot.dev"}
        node_with_props: HTMLNode = HTMLNode(props=generic_props)

        self.assertEqual(
            f"{node_with_tag}", f"HTMLNode({generic_tag}, None, None, None)"
        )
        self.assertRaises(NotImplementedError, node_with_tag.to_html)
        self.assertEqual(node_with_tag.props_to_html(), "")

        self.assertEqual(
            f"{node_with_value}", f"HTMLNode(None, {generic_value}, None, None)"
        )
        self.assertRaises(NotImplementedError, node_with_value.to_html)
        self.assertEqual(node_with_value.props_to_html(), "")

        self.assertEqual(
            f"{node_with_children}",
            f"HTMLNode(None, None, [HTMLNode({generic_tag}, None, None, None), HTMLNode(None, {generic_value}, None, None)], None)",
        )
        self.assertRaises(NotImplementedError, node_with_children.to_html)
        self.assertEqual(node_with_children.props_to_html(), "")

        self.assertEqual(
            f"{node_with_props}", f"HTMLNode(None, None, None, {generic_props})"
        )
        self.assertRaises(NotImplementedError, node_with_props.to_html)
        self.assertEqual(
            node_with_props.props_to_html(),
            f' href="{generic_props["href"]}" a="{generic_props["a"]}"',
        )

    def test_paragraph(self):
        tag: str = "p"
        text: str = "This is a paragraph"
        node: HTMLNode = HTMLNode(tag, text, None, None)
        self.assertEqual(f"{node}", f"HTMLNode({tag}, {text}, None, None)")
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(node.props_to_html(), "")

    def test_div(self):
        paragraph_tag: str = "p"
        paragraph_text: str = "This is a paragraph"
        paragraph_node: HTMLNode = HTMLNode(paragraph_tag, paragraph_text, None, None)
        div_tag: str = "div"
        div_children: list[HTMLNode] = [paragraph_node, paragraph_node]
        div_node: HTMLNode = HTMLNode(div_tag, None, div_children, None)
        self.assertEqual(
            f"{div_node}", f"HTMLNode({div_tag}, None, {div_children}, None)"
        )
        self.assertRaises(NotImplementedError, div_node.to_html)
        self.assertEqual(div_node.props_to_html(), "")

    def test_link(self):
        tag: str = "a"
        text: str = "This is a link"
        props: dict[str, str] = {"href": "http://boot.dev"}
        node: HTMLNode = HTMLNode(tag, text, None, props)
        self.assertEqual(f"{node}", f"HTMLNode({tag}, {text}, None, {props})")
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(node.props_to_html(), f' href="{props["href"]}"')

    def test_image(self):
        tag: str = "img"
        props: dict[str, str] = {
            "src": "http://boot.dev/image.png",
            "alt": "Boot dev image",
        }
        node: HTMLNode = HTMLNode(tag=tag, props=props)
        self.assertEqual(f"{node}", f"HTMLNode({tag}, None, None, {props})")
        self.assertRaises(NotImplementedError, node.to_html)
        self.assertEqual(
            node.props_to_html(), f' src="{props["src"]}" alt="{props["alt"]}"'
        )


if __name__ == "__main__":
    unittest.main()
