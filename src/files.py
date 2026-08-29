import os
import shutil


def files_move_static(static_dir: str, public_dir: str) -> None:
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print(f"Removed {public_dir}")

    os.mkdir(public_dir)
    print(f"Created {public_dir}")

    copy_directory(static_dir, public_dir)


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
