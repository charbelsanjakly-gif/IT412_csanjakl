"""Server Configuration Manager.

Entry point for the program. It loads the primary and server configurations
and runs the menu loop. The heavy lifting is done by the file_manager and
config_manager modules, so this file mainly holds the menus and passes the
user's choice on to the right function.

Before any servers exist the short menu is shown. Once at least one server has
been added the full menu with all of the options appears.
"""

from functions import file_manager, config_manager

PRIMARY_CONFIG_FILE = "primary_config.json"
SERVER_CONFIG_FILE = "server_configs.json"


def print_empty_menu():
    """Show the menu used when no servers have been added yet."""
    print("\n===== Server Configuration Manager =====")
    print("1. Add a new server")
    print("2. Modify Primary Configuration")
    print("3. Exit Program")


def print_full_menu():
    """Show the menu used once one or more servers exist."""
    print("\n===== Server Configuration Manager =====")
    print("1. Add a new server")
    print("2. Modify the configuration of an existing server")
    print("3. Delete an existing server")
    print("4. Modify Primary Configuration")
    print("5. Save server configuration data")
    print("6. Exit Program")


def main():
    """Load the configuration files and run the menu loop."""
    # Load the primary configuration, creating defaults the first time.
    primary_config = config_manager.load_primary_config(PRIMARY_CONFIG_FILE)

    # Load any saved servers. Start with an empty list if the file is not
    # there yet or could not be read.
    if file_manager.file_exists(SERVER_CONFIG_FILE):
        servers = file_manager.load_json(SERVER_CONFIG_FILE)
        if servers is None:
            servers = []
    else:
        servers = []

    running = True
    while running:
        # The menu shown depends on whether any servers exist.
        if servers:
            print_full_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                servers = config_manager.add_server(
                    primary_config, servers, SERVER_CONFIG_FILE)
            elif choice == "2":
                servers = config_manager.modify_server(
                    servers, SERVER_CONFIG_FILE)
            elif choice == "3":
                servers = config_manager.delete_server(
                    servers, SERVER_CONFIG_FILE)
            elif choice == "4":
                primary_config = config_manager.modify_primary_config(
                    primary_config, PRIMARY_CONFIG_FILE)
            elif choice == "5":
                config_manager.save_servers(servers, SERVER_CONFIG_FILE)
                print("Server configuration data saved.")
            elif choice == "6":
                running = False
            else:
                print("Invalid option. Please choose 1-6.")
        else:
            print_empty_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                servers = config_manager.add_server(
                    primary_config, servers, SERVER_CONFIG_FILE)
            elif choice == "2":
                primary_config = config_manager.modify_primary_config(
                    primary_config, PRIMARY_CONFIG_FILE)
            elif choice == "3":
                running = False
            else:
                print("Invalid option. Please choose 1-3.")

    print("Exiting program. Goodbye.")


if __name__ == "__main__":
    # Exit cleanly if the user presses Ctrl+C or the input stream closes.
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting program. Goodbye.")
