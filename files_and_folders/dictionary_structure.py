"""
This script recursively analyzes the structure of a directory and prints
a visual representation of its folder and file hierarchy.

Main Components:
- check_dictionary_structure(base_path): Recursively scans a given directory
  and returns a nested dictionary representing its structure.
- print_dictionary_structure(dictionary, indent=0): Takes the nested dictionary
  and prints a formatted tree-like view of the folder and file structure.

Usage:
- Set the TEST_PATH variable to the desired directory path.
- Run the script to display the structure.

Example Output:
    root_folder/
      file1.txt
      file2.md
      subfolder/
        file3.py
        nested_folder/
          file4.txt
"""

import os


TEST_PATH = ""


def check_dictionary_structure(base_path):
    """
    Recursively analyzes the directory structure starting from the given base path
    and returns a nested dictionary that represents the folder and file hierarchy.

    Each directory is represented as a dictionary with two keys:
    - "folder": a nested dictionary of subdirectories
    - "file": a list of filenames in that directory

    Args:
        base_path (str): The absolute or relative path to the root directory
                         whose structure should be analyzed.

    Returns:
        dict: A nested dictionary representing the directory and file layout.
              Structure example:
              {
                  "root_folder": {
                      "folder": {
                          "subfolder1": {
                              "folder": {...},
                              "file": [...]
                          },
                          ...
                      },
                      "file": ["file1.txt", "file2.md", ...]
                  }
              }

    Notes:
        - Only immediate files and directories are scanned at each level.
        - The function is recursive and processes all nested subdirectories.
    """

    current_path_location = os.path.basename(base_path)
    subfolder_dict = {}
    final_dict = {}
    folder_list = [
        folder
        for folder in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, folder))
    ]
    file_list = [
        file
        for file in os.listdir(base_path)
        if os.path.isfile(os.path.join(base_path, file))
    ]

    for folder in folder_list:
        full_path = os.path.join(base_path, folder)
        if os.path.isdir(full_path):
            subfolder_dict.update(check_dictionary_structure(full_path))

    final_dict[current_path_location] = {
        "folder": subfolder_dict,
        "file": file_list,
    }

    return final_dict


def print_dictionary_structure(dictionary, indent=0):
    """
    Recursively prints a visual representation of a nested dictionary
    that describes a folder structure.

    The dictionary should follow this structure:
        {
            "folder_name": {
                "folder": {
                    "subfolder1": {...},
                    ...
                },
                "file": [
                    "file1.ext",
                    "file2.ext",
                    ...
                ]
            }
        }

    Args:
        dictionary (dict): A nested dictionary representing folders and files.
        indent (int): Current indentation level (used internally for recursion).

    Example:
        >>> sample = {
        ...     "project": {
        ...         "folder": {
        ...             "src": {
        ...                 "folder": {},
        ...                 "file": ["main.py"]
        ...             }
        ...         },
        ...         "file": ["README.md"]
        ...     }
        ... }
        >>> print_dictionary_structure(sample)
        project/
          src/
            main.py
          README.md
    """

    for base_key in dictionary.keys():
        print(" " * indent + f"{base_key}/")
        for sub_key, sub_value in dictionary[base_key].items():
            if sub_key == "folder":
                print_dictionary_structure(sub_value, indent + 2)
            elif sub_key == "file":
                for file in sub_value:
                    print(" " * (indent + 2) + f"{file}")


if __name__ == "__main__":

    result = check_dictionary_structure(TEST_PATH)
    print_dictionary_structure(result)
