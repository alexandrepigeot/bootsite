from typing import override


class Image:
    def __init__(self, alt: str, url: str) -> None:
        self.alt: str = alt
        self.url: str = url

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Image):
            return False

        return (self.alt, self.url) == (other.alt, other.url)

    @override
    def __repr__(self) -> str:
        return f"ImageNode({self.alt}, {self.url})"

    def to_markdown(self) -> str:
        return f"![{self.alt}]({self.url})"
