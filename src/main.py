from files import files_move_static
from webpage import generate_pages

files_move_static()

generate_pages("content", "public", "template.html")
