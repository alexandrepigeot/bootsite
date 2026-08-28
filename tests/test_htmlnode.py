import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_empty(self) -> None:
        node1 = HTMLNode()
        node2 = HTMLNode()

        self.assertEqual(node1, node2)

    def test_eq_full(self) -> None:
        node1 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        node2 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )

        self.assertEqual(node1, node2)

    def test_eq_different_tag(self) -> None:
        node1 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        node2 = HTMLNode(
            tag="different tag",
            value="value",
            children=[HTMLNode()],
            props={"prop": "attribute"},
        )

        self.assertNotEqual(node1, node2)

    def test_eq_different_value(self) -> None:
        node1 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        node2 = HTMLNode(
            tag="tag",
            value="different value",
            children=[HTMLNode()],
            props={"prop": "attribute"},
        )

        self.assertNotEqual(node1, node2)

    def test_eq_different_children(self) -> None:
        node1 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        node2 = HTMLNode(
            tag="tag",
            value="value",
            children=[HTMLNode(tag="different tag")],
            props={"prop": "attribute"},
        )

        self.assertNotEqual(node1, node2)

    def test_eq_different_props(self) -> None:
        node1 = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        node2 = HTMLNode(
            tag="tag",
            value="value",
            children=[HTMLNode()],
            props={"prop": "different attribute"},
        )

        self.assertNotEqual(node1, node2)

    def test_to_html_not_implemented(self) -> None:
        node = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )

        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self) -> None:
        node = HTMLNode(
            tag="tag", value="value", children=[HTMLNode()], props={"prop": "attribute"}
        )
        expected_props = ' prop="attribute"'

        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_empty(self) -> None:
        node = HTMLNode(tag="tag", value="value", children=[HTMLNode()])
        expected_props = ""

        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_multiple(self) -> None:
        node = HTMLNode(
            tag="tag",
            value="value",
            children=[HTMLNode()],
            props={"prop": "attribute", "other-prop": "other attribute"},
        )
        expected_props = ' prop="attribute" other-prop="other attribute"'

        self.assertEqual(node.props_to_html(), expected_props)


if __name__ == "__main__":
    _ = unittest.main()
