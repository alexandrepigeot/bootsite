import unittest

from src.link import Link


class TestLinkNode(unittest.TestCase):
    def test_link_node(self) -> None:
        node1 = Link(text="This is text", url="http://boot.dev")
        node2 = Link(text="This is text", url="http://boot.dev")

        self.assertEqual("LinkNode(This is text, http://boot.dev)", node1.__repr__())
        self.assertEqual(node1, node2)
        self.assertEqual("[This is text](http://boot.dev)", node1.to_markdown())


if __name__ == "__main__":
    _ = unittest.main()
