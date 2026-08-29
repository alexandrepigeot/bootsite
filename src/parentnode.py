from typing import override

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    @override
    def to_html(self) -> str:
        if self.tag == "":
            raise ValueError("Empty tag")

        if self.children is None:
            raise ValueError("Children can't be None")

        content: str = ""

        for child in self.children:
            content += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"
