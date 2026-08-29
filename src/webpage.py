import os

from block import BlockType
from markdown import markdown_to_blocks, markdown_to_html_node


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)

    title: str | None = None

    for block in blocks:
        if block.type != BlockType.HEADING1:
            continue

        if title is not None:
            raise SyntaxError("Multiple titles found")

        title = block.text[2:]

    if title is None:
        raise SyntaxError("No titles found")

    return title


def generate_page(source_file: str, destination_file: str, template_file: str) -> None:
    print(
        f"Generating page from {source_file} to {destination_file} using {template_file} as template."
    )

    markdown = read_file(source_file)

    title = extract_title(markdown)

    html = markdown_to_html_node(markdown).to_html()

    template = read_file(template_file)

    webpage = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    write_file(destination_file, webpage)


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        print(f"Opened {file_path} to read")
        result = file.read()

    print(f"Read {len(result)} characters")

    return result


def write_file(file_path: str, content: str) -> None:
    destination_dirs = os.path.dirname(file_path)
    os.makedirs(destination_dirs, exist_ok=True)

    with open(file_path, "w") as file:
        print(f"Opened {file_path} to write")
        length = file.write(content)

    print(f"Wrote {length} characters")
