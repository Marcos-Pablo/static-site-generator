from copy_static import copy_from_static_to_public
from get_content import generate_page, generate_pages_recursive

def main():
    copy_from_static_to_public()
    # generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")

main()
