from files import files_move_static
from webpage import generate_page

files_move_static()

generate_page("content/index.md", "public/index.html", "template.html")
generate_page(
    "content/blog/glorfindel/index.md",
    "public/blog/glorfindel/index.html",
    "template.html",
)
generate_page(
    "content/blog/majesty/index.md", "public/blog/majesty/index.html", "template.html"
)
generate_page(
    "content/blog/tom/index.md", "public/blog/tom/index.html", "template.html"
)
generate_page("content/contact/index.md", "public/contact/index.html", "template.html")
