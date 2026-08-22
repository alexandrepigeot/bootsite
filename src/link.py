from typing import override


class Link:
    def __init__(self, text: str, url: str) -> None:
        self.text: str = text
        self.url: str = url

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Link):
            return False

        return (self.text, self.url) == (other.text, other.url)

    @override
    def __repr__(self) -> str:
        return f"LinkNode({self.text}, {self.url})"

    def to_markdown(self) -> str:
        return f"[{self.text}]({self.url})"
