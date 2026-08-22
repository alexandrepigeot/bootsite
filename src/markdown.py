from __future__ import annotations

import re

from src.image import Image
from src.link import Link
from src.textnode import TextNode, TextType

IMAGE_PATTERN: str = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_PATTERN: str = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_images(text: str) -> list[Image]:
    matches: list[(str)] = re.findall(IMAGE_PATTERN, text)

    result: list[Image] = []

    for match in matches:
        result.append(Image(match[0], match[1]))

    return result


def extract_links(text: str) -> list[Link]:
    matches: list[(str)] = re.findall(LINK_PATTERN, text)

    result: list[Link] = []

    for match in matches:
        result.append(Link(match[0], match[1]))

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


def split_images(old_nodes: list[TextNode]) -> list[TextNode]:
    # forloop the nodes in old_nodes
    #
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        images = extract_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for image in images:
            split_text = remaining_text.split(image.to_markdown(), maxsplit=1)

            if split_text[0] != "":
                new_nodes.append(TextNode(text=split_text[0], text_type=TextType.TEXT))

            new_nodes.append(
                TextNode(text=image.alt, text_type=TextType.IMAGE, url=image.url)
            )

            remaining_text = split_text[1]

        if remaining_text != "":
            new_nodes.append(TextNode(text=remaining_text, text_type=TextType.TEXT))

    return new_nodes
