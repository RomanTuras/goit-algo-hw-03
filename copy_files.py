import os
import shutil
import sys

def copy_files(source_dir, destination_dir):
    '''
    Copying files from source category to destination with sorting by type
    Params: 
        1-st - path to source directory
        2-nd - path to destination directory (default - dist)
    '''
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                copy_files(item_path, destination_dir)
            else:
                filename, extension = os.path.splitext(item)
                subdir = os.path.join(destination_dir, extension[1:])
                if not os.path.exists(subdir):
                    os.makedirs(subdir)
                new_file_path = os.path.join(subdir, item)
                shutil.copy2(item_path, new_file_path)
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до вихідної директорії")
        sys.exit(1)
    source_directory = sys.argv[1]

    if len(sys.argv) < 3:
        destination_directory = "dist"
    else:
        destination_directory = sys.argv[2]

    copy_files(source_directory, destination_directory)
    print("Копіювання завершено")
