import re
from enum import Enum
from typing import override

HEADING1_PATTERN = r"#{1} .+"
HEADING2_PATTERN = r"#{2} .+"
HEADING3_PATTERN = r"#{3} .+"
HEADING4_PATTERN = r"#{4} .+"
HEADING5_PATTERN = r"#{5} .+"
HEADING6_PATTERN = r"#{6} .+"
CODE_PATTERN = r"`{3}\n.+`{3}"
QUOTE_PATTERN = r">.+(\n>.+)*"
UNORDERED_LIST_PATTERN = r"- .+(\n- .+)*"
ORDERED_LIST_PATTERN = r"\d\. .+(\n\d\. .+)*"


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


class Block:
    def __init__(self, text: str, type: BlockType) -> None:
        self.text: str = text
        self.type: BlockType = type

    @override
    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Block):
            return False

        return (self.text, self.type) == (value.text, value.type)

    @override
    def __repr__(self) -> str:
        return f"Block({self.text}, {self.type})"


def block_to_block_type(block: str) -> BlockType:
    if re.match(HEADING1_PATTERN, block, re.DOTALL):
        return BlockType.HEADING1

    if re.match(HEADING2_PATTERN, block, re.DOTALL):
        return BlockType.HEADING2

    if re.match(HEADING3_PATTERN, block, re.DOTALL):
        return BlockType.HEADING3

    if re.match(HEADING4_PATTERN, block, re.DOTALL):
        return BlockType.HEADING4

    if re.match(HEADING5_PATTERN, block, re.DOTALL):
        return BlockType.HEADING5

    if re.match(HEADING6_PATTERN, block, re.DOTALL):
        return BlockType.HEADING6

    if re.match(CODE_PATTERN, block, re.DOTALL):
        return BlockType.CODE

    if re.match(QUOTE_PATTERN, block):
        return BlockType.QUOTE

    if re.match(UNORDERED_LIST_PATTERN, block):
        return BlockType.UNORDERED_LIST

    if re.match(ORDERED_LIST_PATTERN, block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
