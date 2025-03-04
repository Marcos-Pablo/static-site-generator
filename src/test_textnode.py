import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_when_urls_are_sent(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(node, node2)

    def test_not_eq_when_types_are_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_urls_are_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "url2")
        self.assertNotEqual(node, node2)

    def test_not_eq_when_texts_are_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.boot.dev/tracks/backend")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, { "href": "https://www.boot.dev/tracks/backend" })

    def test_image(self):
        node = TextNode("", TextType.IMAGE, "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2F%40bootdotdev&psig=AOvVaw2voQyAA7GhgFtDPJTFCFzQ&ust=1740871065199000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOCG2p3A54sDFQAAAAAdAAAAABAE")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2F%40bootdotdev&psig=AOvVaw2voQyAA7GhgFtDPJTFCFzQ&ust=1740871065199000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOCG2p3A54sDFQAAAAAdAAAAABAE", "alt": "Image" })

    def test_invalid_type(self):
        node = TextNode("", "")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
