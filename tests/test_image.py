import unittest

from src.image import Image


class TestImageNode(unittest.TestCase):
    def test_image_node(self):
        node1 = Image("alternate text", "source url")
        node2 = Image("alternate text", "source url")

        self.assertEqual("ImageNode(alternate text, source url)", node1.__repr__())
        self.assertEqual(node1, node2)
        self.assertEqual("![alternate text](source url)", node1.to_markdown())


if __name__ == "__main__":
    _ = unittest.main()
