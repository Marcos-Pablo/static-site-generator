import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_optional_properties(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "teste", None, props1)
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

if __name__ == "__main__":
    unittest.main()
