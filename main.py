import os
import shutil


def create_folder(path: str, extension: str) -> str:
    """
    Creates a folder named after the given extension
    :param path: path to the folder where the file is located
    :param extension: extension of the file
    :return: the path of the newly created folder
    """

    # Set the folder name to the extension without the dot
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path
