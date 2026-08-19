from src.textnode import TextNode, TextType


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
