from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    split_block = block.split(" ", 1)
    if len(split_block) == 2 and len(split_block[0]) <= 6 and split_block[0] == "#" * len(split_block[0]):
        return BlockType.HEADING

    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    lines = block.split("\n")
    counter = 1
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_unordered_list = False
        if not line.startswith(f"{counter}. "):
            is_ordered_list = False

        counter += 1

    if is_quote:
        return BlockType.QUOTE
    
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str):
    blocks = []
    for block in markdown.split("\n\n"):
        stripped_block = block.strip()

        if stripped_block:
            blocks.append(stripped_block)

    for i, block in enumerate(blocks):
        lines = block.split("\n")

        for j, line in enumerate(lines):
            lines[j] = line.strip()

        blocks[i] = "\n".join(lines)

    return blocks
