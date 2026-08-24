# Weeks 6 and 7 - Python Database Assignment

Family bookstore inventory application backed by a MariaDB database.

## Setup

1. Start Apache and MySQL/MariaDB in the XAMPP control panel.
2. Install the PyMySQL driver: `pip install PyMySQL`
3. In phpMyAdmin (or the MariaDB CLI), create a database named `bookstore`.
4. Run `sql/create_table.sql` against that database to create the `Books` table.
   (`sql/bookstore_export.sql` is a full export of the database, including
   sample data, if you'd rather import that instead.)
5. Open `main_program.py` and update `DB_HOST`, `DB_USER`, `DB_PASSWORD`,
   and `DB_NAME` at the top of the file to match your local MariaDB setup.

## Running the program

```
python main_program.py
```

## Running the tests

```
python -m unittest tests.test_validators_unittest -v
python -m pytest tests/test_validators_pytest.py -v
```

## Project structure

- `main_program.py` — menu loop and entry point
- `classes/database.py` — `Database` class wrapping the PyMySQL connection
- `functions/validators.py` — input validation functions
- `functions/book_operations.py` — the logic behind each menu option
- `tests/` — unittest and pytest test suites for the validators
- `docs/` — Pydoc-generated HTML documentation for every module
- `sql/create_table.sql` — creates the `Books` table
- `sql/bookstore_export.sql` — full database export with sample data
