import unittest

from src.block import Block, BlockType, block_to_block_type, markdown_to_blocks


class TestBlock(unittest.TestCase):
    def test_eq(self) -> None:
        block1 = Block("block", BlockType.PARAGRAPH)
        block2 = Block("block", BlockType.PARAGRAPH)

        self.assertEqual(block1, block2)

    def test_eq_different_text(self) -> None:
        block1 = Block("block", BlockType.PARAGRAPH)
        block2 = Block("different block", BlockType.PARAGRAPH)

        self.assertNotEqual(block1, block2)

    def test_eq_different_type(self) -> None:
        block1 = Block("block", BlockType.PARAGRAPH)
        block2 = Block("block", BlockType.HEADING1)

        self.assertNotEqual(block1, block2)

    def test_block_to_block_type(self) -> None:
        paragraph = "This is a paragraph"
        heading1 = "# This is a heading"
        heading2 = "## This is a heading"
        heading3 = "### This is a heading"
        heading4 = "#### This is a heading"
        heading5 = "##### This is a heading"
        heading6 = "###### This is a heading"
        code = """```
This is code
```
"""
        quote = """> This is a quote
> This is a quote
> This is a quote
"""
        unordered_list = """- This is a list
- This is a list
- This is a list
"""
        ordered_list = """1. This is a list
2. This is a list
3. This is a list
"""

        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(heading1), BlockType.HEADING1)
        self.assertEqual(block_to_block_type(heading2), BlockType.HEADING2)
        self.assertEqual(block_to_block_type(heading3), BlockType.HEADING3)
        self.assertEqual(block_to_block_type(heading4), BlockType.HEADING4)
        self.assertEqual(block_to_block_type(heading5), BlockType.HEADING5)
        self.assertEqual(block_to_block_type(heading6), BlockType.HEADING6)
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)

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


if __name__ == "__main__":
    _ = unittest.main()
