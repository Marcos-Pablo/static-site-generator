import os, shutil

def copy_from_static_to_public():
    def copy_dir(source_path: str, destination_path: str):
        items = os.listdir(source_path)
        for item in items:
            if os.path.isfile(f"{source_path}/{item}"):
                shutil.copy(f"{source_path}/{item}", destination_path)
            else:
                os.mkdir(f"{destination_path}/{item}")
                copy_dir(f"{source_path}/{item}", f"{destination_path}/{item}")

    shutil.rmtree("./public/")
    os.mkdir("./public/")
    copy_dir("./static/", "./public/")

def main():
    copy_from_static_to_public()

main()
