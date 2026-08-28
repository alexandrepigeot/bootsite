from __future__ import annotations

from src.image import extract_images
from src.link import extract_links
from src.textnode import TextNode, TextType


def split_text_nodes(
    nodes: list[TextNode], delimiter: str, type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text: list[str] = node.text.split(delimiter, maxsplit=2)

        if len(split_text) == 1:
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            continue

        if len(split_text) == 2:
            raise SyntaxError("Invalid markdown. Closing delimiter not found")

        if split_text[0] != "":
            new_nodes.extend(
                split_text_nodes(
                    [TextNode(split_text[0], TextType.TEXT)], delimiter, type
                )
            )

        new_nodes.extend(
            split_text_nodes([TextNode(split_text[1], type)], delimiter, type)
        )

        if split_text[2] != "":
            new_nodes.extend(
                split_text_nodes([TextNode(split_text[2], TextType.TEXT)], delimiter, type)
            )

    return new_nodes

def split_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for image in images:
            split_text = remaining_text.split(image.to_markdown(), maxsplit=1)

            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            new_nodes.append(TextNode(image.alt, TextType.IMAGE, image.url))

            remaining_text = split_text[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for link in links:
            split_text = remaining_text.split(link.to_markdown(), maxsplit=1)

            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            new_nodes.append(TextNode(link.text, TextType.LINK, link.url))

            remaining_text = split_text[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_text_to_text_nodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_text_nodes(nodes, "**", TextType.BOLD)
    nodes = split_text_nodes(nodes, "`", TextType.CODE)
    nodes = split_text_nodes(nodes, "_", TextType.ITALIC)
    nodes = split_images(nodes)
    return split_links(nodes)
