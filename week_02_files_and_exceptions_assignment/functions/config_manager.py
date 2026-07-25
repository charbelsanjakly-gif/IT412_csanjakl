"""Configuration logic for the server configuration program.

This module builds and edits the primary configuration and manages the list
of server configurations. Each server is a dictionary, and the servers are
held together in a list. File reads and writes are handled by the file_manager
module so the functions here can focus on the configuration data itself.
"""

from . import file_manager

# Values written to primary_config.json on first run. Every new server starts
# as a copy of these.
DEFAULT_PRIMARY_CONFIG = {
    "Safe Mode": "On",
    "Memory": "32MB",
    "Error Log": "logs/errors.log",
}


def load_primary_config(filepath):
    """Load the primary configuration, creating it with defaults if missing.

    On the first run the file will not exist, so it is created from
    DEFAULT_PRIMARY_CONFIG. The configuration dictionary is returned either
    way so the program always has a base to work from.
    """
    if not file_manager.file_exists(filepath):
        file_manager.save_json(filepath, DEFAULT_PRIMARY_CONFIG)
        print(f"Created default primary configuration at '{filepath}'.")
        return dict(DEFAULT_PRIMARY_CONFIG)

    config = file_manager.load_json(filepath)
    if not config:
        # Unreadable or empty file, so fall back to the defaults.
        return dict(DEFAULT_PRIMARY_CONFIG)
    return config


def save_servers(servers, filepath):
    """Back up the current server file, then save the server list to it.

    The existing file is copied to a backup before it is replaced, which
    covers the requirement to back the file up every time it is overwritten.
    Returns True if the save succeeded.
    """
    file_manager.backup_file(filepath)
    return file_manager.save_json(filepath, servers)


def add_server(primary_config, servers, filepath):
    """Add a server built from the primary configuration.

    A copy of the primary configuration is used as the starting point. The
    user is asked whether they want to change any of the values before the
    server is added to the list and the list is saved. The updated list is
    returned.
    """
    new_server = dict(primary_config)

    print("\nThe new server will start with these values:")
    _display_config(new_server)

    if _prompt_yes_no("Would you like to modify any of these values?"):
        _edit_values(new_server)

    servers.append(new_server)
    save_servers(servers, filepath)
    print("Server added.")
    return servers


def modify_server(servers, filepath):
    """Change one value on a server the user picks from the list.

    The user chooses a server, then chooses which key to change and enters a
    new value. The list is saved after the change. The list is returned.
    """
    if not servers:
        print("There are no servers to modify.")
        return servers

    index = _select_server(servers)
    if index is None:
        return servers

    server = servers[index]
    key = _select_key(server)
    if key is None:
        return servers

    new_value = input(f"Enter a new value for '{key}': ").strip()
    server[key] = new_value
    save_servers(servers, filepath)
    print(f"Updated '{key}' and saved changes.")
    return servers


def delete_server(servers, filepath):
    """Remove a server and all of its data from the list.

    The user picks a server and confirms the deletion. The server is removed
    and the list is saved. The updated list is returned.
    """
    if not servers:
        print("There are no servers to delete.")
        return servers

    index = _select_server(servers)
    if index is None:
        return servers

    if _prompt_yes_no("Are you sure you want to delete this server?"):
        servers.pop(index)
        save_servers(servers, filepath)
        print("Server deleted.")
    return servers


def modify_primary_config(primary_config, filepath):
    """Add, change, or delete keys in the primary configuration.

    A small menu lets the user add a key/value pair, change a value, delete a
    pair, or save. At least one key/value pair must always remain, so deleting
    the last one is blocked. Changes are only written to disk when the user
    chooses to save. The configuration dictionary is returned.
    """
    editing = True
    while editing:
        print("\n--- Modify Primary Configuration ---")
        _display_config(primary_config)
        print("1. Add a key/value pair")
        print("2. Modify a value")
        print("3. Delete a key/value pair")
        print("4. Save changes")
        print("5. Return to main menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            _add_primary_key(primary_config)
        elif choice == "2":
            _modify_primary_value(primary_config)
        elif choice == "3":
            _delete_primary_key(primary_config)
        elif choice == "4":
            if file_manager.save_json(filepath, primary_config):
                print("Primary configuration saved.")
        elif choice == "5":
            editing = False
        else:
            print("Invalid option. Please choose 1-5.")

    return primary_config


# ---------------------------------------------------------------------------
# Helper functions used by the operations above.
# ---------------------------------------------------------------------------

def _display_config(config):
    """Print each key and value in a configuration dictionary."""
    for key, value in config.items():
        print(f"  {key}: {value}")


def _prompt_yes_no(question):
    """Ask a yes/no question and return True when the answer is yes."""
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer in ("y", "yes")


def _select_key(config):
    """Ask the user to pick a key from config by number.

    Returns the chosen key, or None if the entry was not a valid choice.
    """
    keys = list(config.keys())
    print("\nSelect a key:")
    for number, key in enumerate(keys, start=1):
        print(f"  {number}. {key} (current value: {config[key]})")

    choice = input("Enter the number of the key: ").strip()
    try:
        position = int(choice)
    except ValueError:
        print("Invalid entry: please enter a number.")
        return None

    if 1 <= position <= len(keys):
        return keys[position - 1]
    print("Invalid selection: number out of range.")
    return None


def _select_server(servers):
    """Ask the user to pick a server from the list by number.

    Each server is shown with its values so similar servers can be told
    apart. Returns the list index of the chosen server, or None if the entry
    was not valid.
    """
    print("\nExisting servers:")
    for number, server in enumerate(servers, start=1):
        summary = ", ".join(f"{key}: {value}" for key, value in server.items())
        print(f"  {number}. {summary}")

    choice = input("Enter the number of the server: ").strip()
    try:
        position = int(choice)
    except ValueError:
        print("Invalid entry: please enter a number.")
        return None

    if 1 <= position <= len(servers):
        return position - 1
    print("Invalid selection: number out of range.")
    return None


def _edit_values(config):
    """Let the user change existing values in config one at a time."""
    editing = True
    while editing:
        key = _select_key(config)
        if key is not None:
            new_value = input(f"Enter a new value for '{key}': ").strip()
            config[key] = new_value
            print(f"Updated '{key}'.")
        editing = _prompt_yes_no("Change another value?")


def _add_primary_key(config):
    """Add a new key/value pair to the primary configuration."""
    key = input("Enter the new key name: ").strip()
    if key == "":
        print("Key name cannot be empty.")
    elif key in config:
        print("That key already exists. Use modify instead.")
    else:
        value = input(f"Enter the value for '{key}': ").strip()
        config[key] = value
        print(f"Added '{key}'.")


def _modify_primary_value(config):
    """Change the value of an existing primary configuration key."""
    key = _select_key(config)
    if key is not None:
        value = input(f"Enter a new value for '{key}': ").strip()
        config[key] = value
        print(f"Updated '{key}'.")


def _delete_primary_key(config):
    """Delete a key from the primary configuration, keeping at least one."""
    if len(config) <= 1:
        print("Cannot delete: the primary configuration must keep at least "
              "one key/value pair.")
        return
    key = _select_key(config)
    if key is not None:
        del config[key]
        print(f"Deleted '{key}'.")
