import os, shutil

def copy_dir(source_dir_path: str, dest_dir_path: str):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_dir(from_path, dest_path)
