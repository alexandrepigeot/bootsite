from typing import override

from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    @override
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    @override
    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("Tag can't be None")

        if self.tag == "":
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
