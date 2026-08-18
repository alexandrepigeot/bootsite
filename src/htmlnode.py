from __future__ import annotations

from typing import override


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        result = ""

        if self.props is None:
            return result

        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'

        return result

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, HTMLNode):
            return False

        return (self.tag, self.value, self.children, self.props) == (
            other.tag,
            other.value,
            other.children,
            other.props,
        )

    @override
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
