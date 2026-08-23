import unittest

from src.blocktype import BlockType, block_to_blocktype


class TestBlockType(unittest.TestCase):
    def test_heading_block_type(self) -> None:
        blocks: list[str] = [
            "# heading",
            "## heading",
            "### heading",
            "#### heading",
            "##### heading",
            "###### heading",
        ]

        for block in blocks:
            self.assertEqual(BlockType.HEADING, block_to_blocktype(block))

    def test_code_block_type(self) -> None:
        block = """```
        some code comes here
        ```
        """

        self.assertEqual(BlockType.CODE, block_to_blocktype(block))

    def test_quote_block_type(self) -> None:
        block = """> quote
        > quote
        > quote"""

        self.assertEqual(BlockType.QUOTE, block_to_blocktype(block))

    def test_unordered_list_block_type(self) -> None:
        block = """- list
        - list
        - list"""

        self.assertEqual(BlockType.UNORDERED_LIST, block_to_blocktype(block))

    def test_ordered_list_block_type(self) -> None:
        block = """1. list
        2. list
        3. list"""

        self.assertEqual(BlockType.ORDERED_LIST, block_to_blocktype(block))

    def test_paragraph_block_type(self) -> None:
        block = "This is a paragraph!"

        self.assertEqual(BlockType.PARAGRAPH, block_to_blocktype(block))
