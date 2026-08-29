import os
import shutil

STATIC_DIR = "static"
PUBLIC_DIR = "public"


def files_move_static() -> None:
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
        print(f"Removed {PUBLIC_DIR}")

    os.mkdir(PUBLIC_DIR)
    print(f"Created {PUBLIC_DIR}")

    copy_directory(STATIC_DIR, PUBLIC_DIR)


def copy_directory(source: str, destination: str) -> None:
    source_files = os.listdir(source)

    for source_file in source_files:
        source_file_path = os.path.join(source, source_file)
        destination_file_path = os.path.join(destination, source_file)

        if os.path.isfile(source_file_path):
            _ = shutil.copy(source_file_path, destination_file_path)

            print(f"{source_file_path} is a file. Copied to {destination_file_path}")

        if os.path.isdir(source_file_path):
            print(
                f"{source_file_path} is a directory. Copying to {destination_file_path}..."
            )

            os.mkdir(destination_file_path)

            copy_directory(source_file_path, destination_file_path)
