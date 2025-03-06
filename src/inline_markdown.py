from textnode import TextNode, TextType
import re

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            text_split = node.text.split(delimiter)
            if len(text_split) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")

            for i, content in enumerate(text_split):
                if i % 2 == 0 and content:
                    nodes.append(TextNode(content, TextType.TEXT))
                elif i % 2 != 0 and content:
                    nodes.append(TextNode(content, text_type))
    return nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            nodes.append(node)
            continue
        
        for image in images:
            alt, url = image[0], image[1]
            sections = text.split(f"![{alt}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            first_section = sections[0]
            second_section = sections[1]

            if first_section:
                nodes.append(TextNode(first_section, TextType.TEXT))

            nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = second_section

        if text:
            nodes.append(TextNode(text, TextType.TEXT))
    return nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            nodes.append(node)
            continue
        
        for link in links:
            alt, url = link[0], link[1]
            sections = text.split(f"[{alt}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            first_section = sections[0]
            second_section = sections[1]

            if first_section:
                nodes.append(TextNode(first_section, TextType.TEXT))

            nodes.append(TextNode(alt, TextType.LINK, url))
            text = second_section

        if text:
            nodes.append(TextNode(text, TextType.TEXT))
    return nodes

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

