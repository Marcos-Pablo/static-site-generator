from copy_dir import copy_dir
from get_content import generate_pages_recursive
import os, shutil, sys

static_dir_path = "./static"
content_dir_path = "./content"
public_dir_path = "./docs"
template_path = "./template.html"
base_path = sys.argv[1] if len(sys.argv) >= 2 else "/"

def main():
    print(base_path)
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    copy_dir(static_dir_path, public_dir_path)
    generate_pages_recursive(content_dir_path, template_path, public_dir_path, base_path)

main()
