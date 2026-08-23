import re
from enum import Enum

HEADING_PATTERN = r"#{1,6} .+"
CODE_PATTERN = r"`{3}\n.+`{3}"
QUOTE_PATTERN = r">.+(\n>.+)*"
UNORDERED_LIST_PATTERN = r"- .+(\n- .+)*"
ORDERED_LIST_PATTERN = r"\d\. .+(\n\d\. .+)*"


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_blocktype(block: str) -> BlockType:
    if re.match(HEADING_PATTERN, block, re.DOTALL):
        return BlockType.HEADING

    if re.match(CODE_PATTERN, block, re.DOTALL):
        return BlockType.CODE

    if re.match(QUOTE_PATTERN, block):
        return BlockType.QUOTE

    if re.match(UNORDERED_LIST_PATTERN, block):
        return BlockType.UNORDERED_LIST

    if re.match(ORDERED_LIST_PATTERN, block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
