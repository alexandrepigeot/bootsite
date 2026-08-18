from __future__ import annotations

from enum import Enum
from typing import override

from src.leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (self.text, self.text_type, self.url) == (
            other.text,
            other.text_type,
            other.url,
        )

    @override
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_leaf_node(self) -> LeafNode:
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag="", value=self.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=self.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=self.text)
            case TextType.LINK:
                if self.url is None:
                    raise ValueError("url cannot be None")
                return LeafNode(tag="a", value=self.text, props={"href": self.url})
            case TextType.IMAGE:
                if self.url is None:
                    raise ValueError("url cannot be None")
                return LeafNode(
                    tag="img", value="", props={"alt": self.text, "src": self.url}
                )
