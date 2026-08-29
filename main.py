import sys

from src.files import files_move_static
from src.webpage import generate_pages

if sys.argv[1] != "":
    basepath = sys.argv[1]

else:
    basepath = "/"

files_move_static("static", "docs")

generate_pages("content", "docs", "template.html", basepath)
