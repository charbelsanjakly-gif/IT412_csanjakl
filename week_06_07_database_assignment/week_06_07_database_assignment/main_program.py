"""
main_program module

Menu-driven bookstore inventory application. Connects to a MariaDB
database and lets the user view, add, sell, edit, and remove books
until they choose to exit.
"""

from classes.database import Database
from functions.book_operations import (
    show_all_books,
    add_book,
    record_sale,
    edit_book,
    remove_book,
)

# Database connection settings - update these to match your own
# XAMPP/MariaDB setup (host, username, password, and database name).
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'bookstore'

MENU_TEXT = """
===== Family Bookstore Inventory =====
1. Show all books
2. Add a Book
3. Record a book sale
4. Edit book details
5. Remove a book
6. Exit program
========================================
"""


def main():
    """Run the program's main menu loop until the user chooses to exit."""
    try:
        db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    except Exception as error:
        print(f"Could not connect to the database: {error}")
        return

    while True:
        print(MENU_TEXT)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            show_all_books(db)
        elif choice == '2':
            add_book(db)
        elif choice == '3':
            record_sale(db)
        elif choice == '4':
            edit_book(db)
        elif choice == '5':
            remove_book(db)
        elif choice == '6':
            print("Thanks for using the Family Bookstore Inventory. Goodbye!")
            db.close()
            break
        else:
            print("That's not a valid option. Please choose 1-6.\n")


if __name__ == '__main__':
    main()
