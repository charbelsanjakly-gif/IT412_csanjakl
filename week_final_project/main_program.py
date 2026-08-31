"""
main_program module

Customer database management system. Main entry point for the IT 412
final project. Provides a menu-driven interface for managing customer
records.
"""

from classes.database import Database
from classes.customer import Customer
from functions.file_handler import import_customer_file


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("CUSTOMER DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Import a new data file")
    print("2. Show data currently in database")
    print("3. Add a record to database")
    print("4. Edit a record")
    print("5. Delete a record")
    print("6. Quit the program")
    print("="*50)


def show_customers(database):
    """Display all customers in the database."""
    customers = database.get_all_customers()

    if not customers:
        print("\nNo customers in database.")
        return

    print(f"\n{'#':<5} {'First Name':<15} {'Last Name':<15} {'Company':<20} {'City':<15}")
    print("-" * 70)

    for i, customer in enumerate(customers):
        print(f"{i:<5} {customer.first_name:<15} {customer.last_name:<15} "
              f"{customer.company_name:<20} {customer.city:<15}")


def add_customer(database):
    """Add a new customer to the database."""
    print("\n--- Add New Customer ---")

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    company_name = input("Company name: ").strip()
    address = input("Address: ").strip()
    city = input("City: ").strip()
    county = input("County: ").strip()
    state = input("State (2 letter code): ").strip().upper()
    zip_code = input("Zip code: ").strip()
    phone1 = input("Phone 1: ").strip()
    phone2 = input("Phone 2 (optional): ").strip()
    email = input("Email: ").strip()

    customer = Customer(
        first_name, last_name, company_name, address,
        city, county, state, zip_code, phone1, phone2, email
    )

    if not customer.is_valid_name(first_name):
        print("Error: Invalid first name format.")
        return

    if not customer.is_valid_name(last_name):
        print("Error: Invalid last name format.")
        return

    if not customer.is_valid_state(state):
        print("Error: Invalid state code.")
        return

    if not customer.is_valid_zip(zip_code):
        print("Error: Invalid zip code format.")
        return

    if not customer.is_valid_phone(phone1):
        print("Error: Invalid phone 1 format.")
        return

    if phone2 and not customer.is_valid_phone(phone2):
        print("Error: Invalid phone 2 format.")
        return

    if not customer.is_valid_email(email):
        print("Error: Invalid email format.")
        return

    database.add_customer(customer)
    print(f"\nSuccessfully added {first_name} {last_name} to database.")


def edit_customer(database):
    """Edit an existing customer record."""
    print("\n--- Edit Customer ---")

    show_customers(database)

    try:
        index = int(input("\nEnter customer number to edit: "))
        customer = database.get_customer_by_index(index)

        if not customer:
            print("Error: Invalid customer number.")
            return

        print(f"\nEditing {customer.first_name} {customer.last_name}")
        print("1. First name")
        print("2. Last name")
        print("3. Email")
        print("4. Phone 1")
        print("5. Phone 2")

        field = input("Select field to edit (1-5): ").strip()

        if field == "1":
            customer.first_name = input("New first name: ").strip()
        elif field == "2":
            customer.last_name = input("New last name: ").strip()
        elif field == "3":
            customer.email = input("New email: ").strip()
        elif field == "4":
            customer.phone1 = input("New phone 1: ").strip()
        elif field == "5":
            customer.phone2 = input("New phone 2: ").strip()
        else:
            print("Invalid field selection.")
            return

        database.update_customer(index, customer)
        print("Customer updated successfully.")

    except ValueError:
        print("Error: Please enter a valid number.")


def delete_customer(database):
    """Delete a customer record."""
    print("\n--- Delete Customer ---")

    show_customers(database)

    try:
        index = int(input("\nEnter customer number to delete: "))
        customer = database.get_customer_by_index(index)

        if not customer:
            print("Error: Invalid customer number.")
            return

        confirm = input(f"Delete {customer.first_name} {customer.last_name}? (y/n): ").strip().lower()

        if confirm == "y":
            database.delete_customer(index)
            print("Customer deleted successfully.")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    """Main program loop."""
    database = Database()

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            filename = input("Enter filename to import: ").strip()
            import_customer_file(filename, database)

        elif choice == "2":
            show_customers(database)

        elif choice == "3":
            add_customer(database)

        elif choice == "4":
            edit_customer(database)

        elif choice == "5":
            delete_customer(database)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-6.")


if __name__ == "__main__":
    main()
