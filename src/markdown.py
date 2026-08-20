from __future__ import annotations

import re
from typing import override

from src.textnode import TextNode, TextType

IMAGE_PATTERN: str = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_PATTERN: str = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


class ImageNode:
    def __init__(self, alt: str, src: str) -> None:
        self.alt: str = alt
        self.src: str = src

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, ImageNode):
            return False

        return (self.alt, self.src) == (other.alt, other.src)

    @override
    def __repr__(self) -> str:
        return f"ImageNode({self.alt}, {self.src})"


class LinkNode:
    def __init__(self, text: str, url: str) -> None:
        self.text: str = text
        self.url: str = url

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, LinkNode):
            return False

        return (self.text, self.url) == (other.text, other.url)

    @override
    def __repr__(self) -> str:
        return f"LinkNode({self.text}, {self.url})"


def extract_images(text: str) -> list[ImageNode]:
    matches: list[(str)] = re.findall(IMAGE_PATTERN, text)

    result: list[ImageNode] = []

    for match in matches:
        result.append(ImageNode(match[0], match[1]))

    return result


def extract_links(text: str) -> list[LinkNode]:
    matches: list[(str)] = re.findall(LINK_PATTERN, text)

    result: list[LinkNode] = []

    for match in matches:
        result.append(LinkNode(match[0], match[1]))

    return result


def split_nodes(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text: list[str] = node.text.split(delimiter, maxsplit=2)

        if len(split_text) == 1:
            new_nodes.append(TextNode(text=split_text[0], text_type=TextType.TEXT))
            continue

        if len(split_text) == 2:
            raise SyntaxError("Invalid markdown. Closing delimiter not found")

        if split_text[0] != "":
            new_nodes.extend(
                split_nodes(
                    [TextNode(text=split_text[0], text_type=TextType.TEXT)],
                    delimiter,
                    text_type,
                )
            )

        new_nodes.extend(
            split_nodes(
                [TextNode(text=split_text[1], text_type=text_type)],
                delimiter,
                text_type,
            )
        )

        if split_text[2] != "":
            new_nodes.extend(
                split_nodes(
                    [TextNode(text=split_text[2], text_type=TextType.TEXT)],
                    delimiter,
                    text_type,
                )
            )

    return new_nodes
