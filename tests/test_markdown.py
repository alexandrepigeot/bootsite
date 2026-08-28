import unittest

from src.block import Block, BlockType
from src.leafnode import LeafNode
from src.markdown import markdown_to_blocks, markdown_to_html_node
from src.parentnode import ParentNode


class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self) -> None:
        markdown = """
This is a paragraph

# This is a heading

## This is a heading

### This is a heading

#### This is a heading

##### This is a heading

###### This is a heading

```
This is code
```

> This is a quote
> This is a quote
> This is a quote

- This is a list
- This is a list
- This is a list

1. This is a list
2. This is a list
3. This is a list
"""
        expected_blocks: list[Block] = [
            Block("This is a paragraph", BlockType.PARAGRAPH),
            Block("# This is a heading", BlockType.HEADING1),
            Block("## This is a heading", BlockType.HEADING2),
            Block("### This is a heading", BlockType.HEADING3),
            Block("#### This is a heading", BlockType.HEADING4),
            Block("##### This is a heading", BlockType.HEADING5),
            Block("###### This is a heading", BlockType.HEADING6),
            Block(
                """```
This is code
```""",
                BlockType.CODE,
            ),
            Block(
                """> This is a quote
> This is a quote
> This is a quote""",
                BlockType.QUOTE,
            ),
            Block(
                """- This is a list
- This is a list
- This is a list""",
                BlockType.UNORDERED_LIST,
            ),
            Block(
                """1. This is a list
2. This is a list
3. This is a list""",
                BlockType.ORDERED_LIST,
            ),
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_to_html_node(self) -> None:
        markdown = """
This is a paragraph

# This is a heading

## This is a heading

### This is a heading

#### This is a heading

##### This is a heading

###### This is a heading

```
This is code
```

> This is a quote
> This is a quote
> This is a quote

- This is a list
- This is a list
- This is a list

1. This is a list
2. This is a list
3. This is a list
"""

        expected_node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("", "This is a paragraph")]),
                ParentNode("h1", [LeafNode("", "This is a heading")]),
                ParentNode("h2", [LeafNode("", "This is a heading")]),
                ParentNode("h3", [LeafNode("", "This is a heading")]),
                ParentNode("h4", [LeafNode("", "This is a heading")]),
                ParentNode("h5", [LeafNode("", "This is a heading")]),
                ParentNode("h6", [LeafNode("", "This is a heading")]),
                ParentNode("pre", [LeafNode("code", "This is code")]),
                ParentNode(
                    "blockquote",
                    [LeafNode("", "This is a quote\nThis is a quote\nThis is a quote")],
                ),
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode("", "This is a list")]),
                        ParentNode("li", [LeafNode("", "This is a list")]),
                        ParentNode("li", [LeafNode("", "This is a list")]),
                    ],
                ),
                ParentNode(
                    "ol",
                    [
                        ParentNode("li", [LeafNode("", "This is a list")]),
                        ParentNode("li", [LeafNode("", "This is a list")]),
                        ParentNode("li", [LeafNode("", "This is a list")]),
                    ],
                ),
            ],
        )

        self.assertEqual(markdown_to_html_node(markdown), expected_node)


if __name__ == "__main__":
    _ = unittest.main()
