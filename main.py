import os
import shutil


def create_folder(path: str, extension: str) -> str:
    """
    Creates a folder named after the given extension.

    :param path: Path to the folder where the file is located.
    :param extension: Extension of the file.
    :return: The path of the newly created folder.
    """

    # Set the folder name to the extension without the dot
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    """
    Sort the files based on their extension.

    :param source_path: Path where the files that need to be sorted are located.
    """

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)

