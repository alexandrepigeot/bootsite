import re
from typing import override

LINK_PATTERN: str = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


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
        return f"Link({self.text, self.url})"

    def to_markdown(self) -> str:
        return f"[{self.text}]({self.url})"


def extract_links(text: str) -> list[Link]:
    matches: list[(str)] = re.findall(LINK_PATTERN, text)

    links: list[Link] = []

    for match in matches:
        links.append(Link(match[0], match[1]))

    return links
