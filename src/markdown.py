from block import Block, BlockType, block_to_block_type
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split import split_text_to_text_nodes


def markdown_to_blocks(markdown: str) -> list[Block]:
    raw_blocks = markdown.split("\n\n")

    blocks: list[Block] = []

    for raw_block in raw_blocks:
        stripped_block = raw_block.strip()

        if stripped_block == "":
            continue

        type = block_to_block_type(stripped_block)

        blocks.append(Block(stripped_block, type))

    return blocks


def markdown_to_html_node(markdown: str) -> HTMLNode:
    nodes: list[HTMLNode] = []

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        match block.type:
            case BlockType.PARAGRAPH:
                nodes.append(build_paragraph(block.text))
            case BlockType.HEADING1:
                nodes.append(build_heading(block.text, 1))
            case BlockType.HEADING2:
                nodes.append(build_heading(block.text, 2))
            case BlockType.HEADING3:
                nodes.append(build_heading(block.text, 3))
            case BlockType.HEADING4:
                nodes.append(build_heading(block.text, 4))
            case BlockType.HEADING5:
                nodes.append(build_heading(block.text, 5))
            case BlockType.HEADING6:
                nodes.append(build_heading(block.text, 6))
            case BlockType.CODE:
                nodes.append(build_code(block.text))
            case BlockType.QUOTE:
                nodes.append(build_quote(block.text))
            case BlockType.UNORDERED_LIST:
                nodes.append(build_unordered_list(block.text))
            case BlockType.ORDERED_LIST:
                nodes.append(build_ordered_list(block.text))

    return ParentNode("div", nodes)


def build_paragraph(text: str) -> HTMLNode:
    paragraph = ParentNode("p", [])

    if paragraph.children is None:
        raise ValueError

    children_nodes = split_text_to_text_nodes(text)

    for node in children_nodes:
        paragraph.children.append(node.to_leaf_node())

    return paragraph


def build_heading(text: str, level: int) -> HTMLNode:
    heading = ParentNode("", [])

    match level:
        case 1:
            heading.tag = "h1"
        case 2:
            heading.tag = "h2"
        case 3:
            heading.tag = "h3"
        case 4:
            heading.tag = "h4"
        case 5:
            heading.tag = "h5"
        case 6:
            heading.tag = "h6"
        case _:
            raise TypeError("Invalid heading level")

    if heading.children is None:
        raise ValueError

    starting_index = level + 1

    children_nodes = split_text_to_text_nodes(text[starting_index:])

    for node in children_nodes:
        heading.children.append(node.to_leaf_node())

    return heading


def build_code(text: str) -> HTMLNode:
    stripped_text = text.replace("```", "").strip()

    return ParentNode("pre", [LeafNode("code", stripped_text)])


def build_quote(text: str) -> HTMLNode:
    quote = ParentNode("blockquote", [])

    if quote.children is None:
        raise ValueError

    text = text.replace("> ", "")

    children_nodes = split_text_to_text_nodes(text)

    for node in children_nodes:
        quote.children.append(node.to_leaf_node())

    return quote


def build_unordered_list(text: str) -> HTMLNode:
    unordered_list = ParentNode("ul", [])

    if unordered_list.children is None:
        raise ValueError

    lines: list[str] = text.split("\n")

    for line in lines:
        list_item = ParentNode("li", [])

        if list_item.children is None:
            raise ValueError

        children_nodes = split_text_to_text_nodes(line[2:])

        for node in children_nodes:
            list_item.children.append(node.to_leaf_node())

        unordered_list.children.append(list_item)

    return unordered_list


def build_ordered_list(text: str) -> HTMLNode:
    ordered_list = ParentNode("ol", [])

    if ordered_list.children is None:
        raise ValueError

    lines = text.split("\n")

    for line in lines:
        list_item = ParentNode("li", [])

        if list_item.children is None:
            raise ValueError

        children_nodes = split_text_to_text_nodes(line[3:])

        for node in children_nodes:
            list_item.children.append(node.to_leaf_node())

        ordered_list.children.append(list_item)

    return ordered_list
