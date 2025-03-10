from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children

def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            children = text_to_children(paragraph)
            return ParentNode("p", children)
        case BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break

            if level + 1 >= len(block):
                raise ValueError(f"Invalid heading level: {level}")

            text = block[level + 1:]
            children = text_to_children(text)
            return ParentNode(f"h{level}", children)
        case BlockType.QUOTE:
            processed_lines = []
            lines = block.split("\n")
            for line in lines:
                new_line = line.lstrip(">").strip()
                processed_lines.append(new_line)
            content = " ".join(processed_lines)
            children = text_to_children(content)
            return ParentNode("blockquote", children)
        case BlockType.CODE:
            content = block[4:-3]
            text_node = TextNode(content, TextType.TEXT)
            child = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [child])
            return ParentNode("pre", [code_node])
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line[2:]
                children = text_to_children(text)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)

            return ParentNode("ul", li_nodes)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line[3:]
                children = text_to_children(text)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)

            return ParentNode("ol", li_nodes)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    
    parent_node = ParentNode("div", children, {})
    return parent_node

def block_to_block_type(block: str) -> BlockType:
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        counter = 1
        for line in block.split("\n"):
            if not line.startswith(f"{counter}. "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    for block in markdown.split("\n\n"):
        stripped_block = block.strip()

        if stripped_block:
            blocks.append(stripped_block)

    for i in range(len(blocks)):
        block = blocks[i]
        lines = block.split("\n")

        for j in range(len(lines)):
            line = lines[j]
            lines[j] = line.strip()

        blocks[i] = "\n".join(lines)
    return blocks
