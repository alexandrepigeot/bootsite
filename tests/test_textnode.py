import unittest
from src.textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
	def test_plain_eq(self):
		node1 = TextNode("This is a text node", TextType.PLAIN)
		node2 = TextNode("This is a text node", TextType.PLAIN)
		self.assertEqual(node1, node2)

	def test_plain_repr(self):
		node = TextNode("This is a text node", TextType.PLAIN)
		text = "TextNode(This is a text node, plain, None)"
		self.assertEqual(f"{node}", text)

	def test_bold_eq(self):
		node1 = TextNode("This is a bold text node", TextType.BOLD)
		node2 = TextNode("This is a bold text node", TextType.BOLD)
		self.assertEqual(node1, node2)

	def test_bold_repr(self):
		node = TextNode("This is a bold text node", TextType.BOLD)
		text = "TextNode(This is a bold text node, bold, None)"
		self.assertEqual(f"{node}", text)
	
	def test_italic_eq(self):
		node1 = TextNode("This is an italic text node", TextType.ITALIC)
		node2 = TextNode("This is an italic text node", TextType.ITALIC)
		self.assertEqual(node1, node2)

	def test_italic_repr(self):
		node = TextNode("This is an italic text node", TextType.ITALIC)
		text = "TextNode(This is an italic text node, italic, None)"
		self.assertEqual(f"{node}", text)

	def test_code_eq(self):
		node1 = TextNode("This is a code text node", TextType.CODE)
		node2 = TextNode("This is a code text node", TextType.CODE)
		self.assertEqual(node1, node2)

	def test_code_repr(self):
		node = TextNode("This is a code text node", TextType.CODE)
		text = "TextNode(This is a code text node, code, None)"
		self.assertEqual(f"{node}", text)

	def test_link_eq(self):
		node1 = TextNode("This is a link text node", TextType.LINK, "http://boot.dev")
		node2 = TextNode("This is a link text node", TextType.LINK, "http://boot.dev")
		self.assertEqual(node1, node2)

	def test_link_repr(self):
		node = TextNode("This is a link text node", TextType.LINK, "http://boot.dev")
		text = "TextNode(This is a link text node, link, http://boot.dev)"
		self.assertEqual(f"{node}", text)

	def test_image_eq(self):
		node1 = TextNode("This is an image text node", TextType.IMAGE, "http://boot.dev/image.png")
		node2 = TextNode("This is an image text node", TextType.IMAGE, "http://boot.dev/image.png")
		self.assertEqual(node1, node2)

	def test_image_repr(self):
		node = TextNode("This is an image text node", TextType.IMAGE, "http://boot.dev/image.png")
		text = "TextNode(This is an image text node, image, http://boot.dev/image.png)"
		self.assertEqual(f"{node}", text)

	def test_text_not_eq(self):
		node1 = TextNode("This is a text node", TextType.PLAIN)
		node2 = TextNode("This one has a different text", TextType.PLAIN)
		self.assertNotEqual(node1, node2)

	def test_text_type_not_eq(self):
		node1 = TextNode("This is a text node", TextType.PLAIN)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node1, node2)

	def test_url_not_eq(self):
		node1 = TextNode("This is a text node", TextType.PLAIN, "http://boot.dev")
		node2 = TextNode("This is a text node", TextType.PLAIN, "http://localhost")
		self.assertNotEqual(node1, node2)

	def test_default_url(self):
		node1 = TextNode("This is a text node", TextType.PLAIN)
		node2 = TextNode("This is a text node", TextType.PLAIN, None)
		self.assertEqual(node1, node2)

if __name__ == "__main__":
	unittest.main()
