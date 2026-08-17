import unittest

from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_generic_node(self):
        normal_tag: str = "div"
        child_tag: str = "p"
        normal_content: str = "This is text"
        child: HTMLNode = LeafNode(tag=child_tag, value=normal_content)
        normal_children: list[HTMLNode] = [child]

        node: ParentNode = ParentNode(tag=normal_tag, children=normal_children)
        self.assertEqual(node.__repr__(), f"ParentNode({normal_tag}, [{child}], None)")
        self.assertEqual(
            node.to_html(),
            f"<{normal_tag}><{child_tag}>{normal_content}</{child_tag}></{normal_tag}>",
        )

    def test_faulty_nodes(self):
        normal_tag: str = "div"
        empty_tag: str = ""
        child: HTMLNode = HTMLNode(tag=normal_tag)
        normal_children: list[HTMLNode] = [child]
        empty_children: list[HTMLNode] = []

        node_without_tag: ParentNode = ParentNode(
            tag=empty_tag, children=normal_children
        )
        self.assertEqual(
            node_without_tag.__repr__(), f"ParentNode({empty_tag}, [{child}], None)"
        )
        self.assertRaises(ValueError, node_without_tag.to_html)

        node_without_children: ParentNode = ParentNode(
            tag=normal_tag, children=empty_children
        )
        self.assertEqual(
            node_without_children.__repr__(), f"ParentNode({normal_tag}, [], None)"
        )
        self.assertRaises(ValueError, node_without_children.to_html)


if __name__ == "__main__":
    _ = unittest.main()
