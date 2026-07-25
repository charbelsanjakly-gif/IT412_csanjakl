"""File-handling helpers for the server configuration program.

Everything that touches the file system lives here: checking whether a file
exists, reading JSON, writing JSON, and making a backup copy before a file is
replaced. The rest of the program works with plain dictionaries and lists and
lets this module deal with the disk.
"""

import json
import os
import shutil


def file_exists(filepath):
    """Return True if filepath points to an existing file."""
    return os.path.isfile(filepath)


def load_json(filepath):
    """Read a JSON file and return the data it contains.

    Returns the parsed dictionary or list on success. If the file is missing,
    is not valid JSON, or cannot be read, a message is shown and None is
    returned so the caller can decide how to recover.
    """
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Notice: '{filepath}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filepath}' does not contain valid JSON.")
        return None
    except OSError as error:
        print(f"Error reading '{filepath}': {error}")
        return None


def save_json(filepath, data):
    """Write data to filepath as formatted JSON.

    Returns True if the write succeeded, or False if an operating system
    error stopped the file from being written.
    """
    try:
        with open(filepath, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except OSError as error:
        print(f"Error writing to '{filepath}': {error}")
        return False


def backup_file(filepath):
    """Copy filepath to a backup before it gets overwritten.

    The backup keeps the same name with '_backup' added before the extension,
    so 'server_configs.json' becomes 'server_configs_backup.json'. If the file
    does not exist yet there is nothing to copy and the function returns False.
    """
    if not file_exists(filepath):
        return False

    root, extension = os.path.splitext(filepath)
    backup_path = f"{root}_backup{extension}"

    try:
        shutil.copy(filepath, backup_path)
        return True
    except OSError as error:
        print(f"Error creating backup of '{filepath}': {error}")
        return False
