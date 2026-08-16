import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_generic_node(self):
        tag: str = "p"
        text: str = "I'm a text"
        empty: str = ""

        node: LeafNode = LeafNode(tag=tag, value=text)
        self.assertEqual(node.__repr__(), f"LeafNode({tag}, {text}, None)")
        self.assertEqual(node.to_html(), f"<{tag}>{text}</{tag}>")

        node_without_tag: LeafNode = LeafNode(tag=empty, value=text)
        self.assertEqual(
            node_without_tag.__repr__(), f"LeafNode({empty}, {text}, None)"
        )
        self.assertEqual(node_without_tag.to_html(), text)

    def test_faulty_nodes(self):
        tag: str = "p"
        empty: str = ""

        node_without_value: LeafNode = LeafNode(tag=tag, value=empty)
        self.assertEqual(
            node_without_value.__repr__(), f"LeafNode({tag}, {empty}, None)"
        )
        self.assertRaises(ValueError, node_without_value.to_html)

    def test_node_with_props(self):
        tag: str = "p"
        text: str = "I'm a text"
        props: dict[str, str] = {"href": "http://boot.dev", "a": "http://boot.dev"}
        node: LeafNode = LeafNode(tag=tag, value=text, props=props)

        self.assertEqual(node.__repr__(), f"LeafNode({tag}, {text}, {props})")
        self.assertEqual(
            node.to_html(),
            f'<{tag} href="{props["href"]}" a="{props["a"]}">{text}</{tag}>',
        )


if __name__ == "__main__":
    _ = unittest.main()
