import json
from pathlib import Path
from typing import List, Union


def create_file_if_not_exists(file_path: str) -> None:
    """
    Checks if a file exists at the given path, and creates it if it doesn't.
    :param file_path: the path of the file to check/create, which can be relative or absolute.
    :return: None
    """
    Path(file_path).touch()


def get_json_file_contents(file_path: str) -> Union[List, None]:
    """
    Reads and return the contents of a JSON file.
    :param file_path: The path where the JSON file is located.
    :return: The contents of the file, or None if there if the file is empty or not found.
    """
    try:
        json_file = open(file_path)
    except IOError:
        return None
    try:
        file_contents = json.load(json_file)
    except ValueError:
        file_contents = None
    json_file.close()
    return file_contents