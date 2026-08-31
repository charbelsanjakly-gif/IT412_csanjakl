# IT 412 Final Project - Customer Database Management System

## Overview
A Python-based customer database management system for importing, viewing, and managing customer records.

## Folder Structure

```
week_final_project/
├── classes/
│   ├── __init__.py
│   ├── customer.py    (Customer class with validation)
│   └── database.py    (Database class for managing records)
├── functions/
│   └── file_handler.py    (Import and parsing functions)
├── main_program.py    (Main menu and program logic)
└── README.md
```

## Features (Initial Submission)
- Import customer data from text files
- Display all customers in database
- Add new customer records
- Edit existing records
- Delete records with confirmation
- Basic field validation (names, phone, email, state, zip)

## Running the Program
```bash
python main_program.py
```

## Usage
1. Select option 1 to import customer data
2. Use option 2 to view all customers
3. Options 3-5 for adding, editing, deleting records
4. Option 6 to exit

## Validation Rules (Implemented)
- Names: letters, spaces, apostrophes, dashes
- Phone: 10 digits or 12 characters with dashes/periods
- Email: standard email format
- State: valid US state abbreviation
- Zip: 4-5 digits

## Future Enhancements
- Export to JSON and CSV files
- Duplicate detection and removal
- SQLite database integration
- Comprehensive test suite (unittest and pytest)
