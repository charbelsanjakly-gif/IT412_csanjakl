"""
book_operations module

Contains the functions that back each menu option in the bookstore
application: showing books, adding a book, recording a sale, editing
a book, and removing a book. Each function collects and validates
user input, then talks to the database through a Database object.
"""

from functions.validators import (
    validate_title,
    validate_author,
    validate_quantity,
    validate_signed_edition,
    validate_price,
    validate_required_price,
)


def get_valid_input(prompt, validator):
    """
    Repeatedly prompt the user until they provide input that passes
    the given validator function, then return that input.
    """
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print("That value isn't valid. Please try again.")


def show_all_books(db):
    """
    Show option #1: print every book in the database, one at a time,
    in an easy-to-read format for non-technical users.
    """
    try:
        books = db.fetch_all("SELECT * FROM Books")
    except Exception as error:
        print(f"There was a problem reading the books: {error}")
        return

    if not books:
        print("\nThere are no books in the database yet.\n")
        return

    print("\n----- Book Inventory -----")
    for book in books:
        signed = book['Signed_Edition'] if book['Signed_Edition'] else 'N/A'
        promo = f"${book['Promo_Price']:.2f}" if book['Promo_Price'] is not None else 'N/A'
        print(f"\nBook ID:        {book['Book_ID']}")
        print(f"Title:          {book['Title']}")
        print(f"Author:         {book['Author']}")
        print(f"Quantity:       {book['Quantity']}")
        print(f"Signed Edition: {signed}")
        print(f"Promo Price:    {promo}")
        print(f"Retail Price:   ${book['Retail_Price']:.2f}")
    print("\n---------------------------\n")


def add_book(db):
    """Menu option #2: collect, validate, and insert a new book."""
    print("\n--- Add a Book ---")
    title = get_valid_input("Book title: ", validate_title)
    author = get_valid_input(
        "Book author (letters, spaces, , . ' - only): ", validate_author
    )
    quantity = get_valid_input("Quantity on hand: ", validate_quantity)
    signed = get_valid_input(
        "Signed edition? (Y/N, or leave blank): ", validate_signed_edition
    )
    promo_price = get_valid_input(
        "Promotional price (or leave blank): ", validate_price
    )
    retail_price = get_valid_input("Retail price: ", validate_required_price)

    signed_value = signed.strip().upper() if signed.strip() != '' else None
    promo_value = float(promo_price) if promo_price.strip() != '' else None

    try:
        db.execute(
            "INSERT INTO Books (Title, Author, Quantity, Signed_Edition, "
            "Promo_Price, Retail_Price) VALUES (%s, %s, %s, %s, %s, %s)",
            (title, author, int(quantity), signed_value, promo_value,
             float(retail_price))
        )
        print("\nBook added successfully.\n")
    except Exception as error:
        print(f"There was a problem adding the book: {error}")


def _find_book_by_title(db, title):
    """Helper: look up a single book by title, or None if not found."""
    return db.fetch_one("SELECT * FROM Books WHERE Title = %s", (title,))


def record_sale(db):
    """
    Menu option #3: ask which book was sold and how many copies, then
    subtract that quantity from the inventory. Inventory is never
    allowed to go negative.
    """
    print("\n--- Record a Book Sale ---")
    title = input("Title of the book that was sold: ")
    book = _find_book_by_title(db, title)

    if book is None:
        print("No book with that title was found.\n")
        return

    quantity_sold = get_valid_input(
        "How many copies were sold? ", validate_quantity
    )
    quantity_sold = int(quantity_sold)

    if quantity_sold <= 0:
        print("Quantity sold must be a positive number.\n")
        return

    if quantity_sold > book['Quantity']:
        print(
            f"Only {book['Quantity']} copies are on hand. "
            "Sale cannot be recorded.\n"
        )
        return

    new_quantity = book['Quantity'] - quantity_sold
    try:
        db.execute(
            "UPDATE Books SET Quantity = %s WHERE Book_ID = %s",
            (new_quantity, book['Book_ID'])
        )
        print(f"\nSale recorded. New quantity on hand: {new_quantity}\n")
    except Exception as error:
        print(f"There was a problem recording the sale: {error}")


# Maps a friendly field name to (database column, validator function)
_EDITABLE_FIELDS = {
    '1': ('Title', 'Title', validate_title),
    '2': ('Author', 'Author', validate_author),
    '3': ('Quantity', 'Quantity', validate_quantity),
    '4': ('Signed Edition', 'Signed_Edition', validate_signed_edition),
    '5': ('Promo Price', 'Promo_Price', validate_price),
    '6': ('Retail Price', 'Retail_Price', validate_required_price),
}


def edit_book(db):
    """
    Menu option #4: ask which book to edit, then which field, then
    collect and validate the new value for that field.
    """
    print("\n--- Edit Book Details ---")
    title = input("Title of the book to edit: ")
    book = _find_book_by_title(db, title)

    if book is None:
        print("No book with that title was found.\n")
        return

    print("Which field would you like to edit?")
    for key, (label, _, _) in _EDITABLE_FIELDS.items():
        print(f"  {key}. {label}")
    choice = input("Enter the number of the field: ").strip()

    if choice not in _EDITABLE_FIELDS:
        print("That's not a valid field choice.\n")
        return

    label, column, validator = _EDITABLE_FIELDS[choice]
    new_value = get_valid_input(f"New {label}: ", validator)

    if column == 'Quantity':
        db_value = int(new_value)
    elif column == 'Signed_Edition':
        db_value = new_value.strip().upper() if new_value.strip() != '' else None
    elif column in ('Promo_Price', 'Retail_Price'):
        db_value = float(new_value) if new_value.strip() != '' else None
    else:
        db_value = new_value

    try:
        db.execute(
            f"UPDATE Books SET {column} = %s WHERE Book_ID = %s",
            (db_value, book['Book_ID'])
        )
        print("\nBook updated successfully.\n")
    except Exception as error:
        print(f"There was a problem updating the book: {error}")


def remove_book(db):
    """
    Menu option #5: ask which book to remove, confirm with the user,
    then delete it from the database.
    """
    print("\n--- Remove a Book ---")
    title = input("Title of the book to remove: ")
    book = _find_book_by_title(db, title)

    if book is None:
        print("No book with that title was found.\n")
        return

    confirm = input(
        f"Are you sure you want to remove '{book['Title']}'? (Y/N): "
    ).strip().upper()

    if confirm != 'Y':
        print("Removal cancelled.\n")
        return

    try:
        db.execute("DELETE FROM Books WHERE Book_ID = %s", (book['Book_ID'],))
        print("\nBook removed successfully.\n")
    except Exception as error:
        print(f"There was a problem removing the book: {error}")
