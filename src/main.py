from files import files_move_static
from webpage import generate_page

files_move_static()

generate_page("content/index.md", "public/index.html", "template.html")
