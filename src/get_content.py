import os
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    items = os.listdir(dir_path_content)
    for item in items:
        if os.path.isfile(f"{dir_path_content}/{item}"):
            file_name = None
            file_extension = None

            for i in range(len(item) - 1, -1, -1):
                if item[i] == ".":
                    file_name = item[:i]
                    file_extension = item[i + 1:]
                    break
            
            if file_extension != "md":
                print("Ignoring non markdown file: ", item)
                continue

            markdown_file = open(f"{dir_path_content}/{item}")
            markdown = markdown_file.read()
            markdown_file.close()

            html_node = markdown_to_html_node(markdown)
            html = html_node.to_html()
            title = extract_title(markdown)
            
            template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

            file = open(f"{dest_dir_path}/{file_name}.html", "w")
            file.write(template)
            file.close()
        else:
            generate_pages_recursive(f"{dir_path_content}/{item}", template_path, f"{dest_dir_path}/{item}")

def generate_page(from_path, template_path, dest_path):
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

