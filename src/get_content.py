import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, base_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, base_path)

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    file = open(dest_path, "w")
    file.write(template)
    file.close()

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]

    raise ValueError("Markdowns must start with a h1 header")

