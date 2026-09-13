"""file_handler module - Import and export functions for customer data.

This module provides functionality to import customer data from text files,
export to JSON and CSV formats, and detect duplicate records.
"""
import json, csv
from classes.customer import Customer

def parse_customer_line(line):
    """Parse a single line from the customer export file.
    
    The customer export file uses ## as field delimiters.
    Format: first_name##last_name##company##address##city##county##state##zip##phone1##phone2##email####
    
    Args:
        line (str): A single line from the customer export file
        
    Returns:
        Customer: A Customer object if parsing succeeds, None otherwise
        
    Raises:
        None (returns None on error instead)
    """
    try:
        parts = [p.strip() for p in line.split("##")]
        parts = [p for p in parts if p]
        if len(parts) < 11: return None
        return Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10])
    except: return None

def is_duplicate(customer, existing_customers):
    """Check if a customer already exists in the database.
    
    Compares first name, last name, and email (case-insensitive).
    
    Args:
        customer (Customer): The customer to check
        existing_customers (list): List of existing Customer objects
        
    Returns:
        bool: True if duplicate found, False otherwise
    """
    for existing in existing_customers:
        if (customer.first_name.lower() == existing.first_name.lower() and customer.last_name.lower() == existing.last_name.lower() and customer.email.lower() == existing.email.lower()): return True
    return False

def import_customer_file(filename, database):
    """Import customers from a text file into the database.
    
    Clears the database before importing. Skips the header line.
    Skips duplicate records and reports count.
    
    Args:
        filename (str): Path to the customer export file
        database (Database): Database object to populate
        
    Returns:
        int: Number of customers successfully imported
        
    Raises:
        Exception: Caught and reported as error message
    """
    count, duplicates = 0, 0
    try:
        database.clear_all()
        with open(filename, "r", encoding="utf-8") as f: lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            customer = parse_customer_line(line)
            if customer:
                if is_duplicate(customer, database.get_all_customers()): duplicates += 1
                else: database.add_customer(customer); count += 1
        print(f"Successfully imported {count} customers.")
        if duplicates > 0: print(f"Skipped {duplicates} duplicate records.")
        return count
    except FileNotFoundError: print(f"Error: File '{filename}' not found."); return 0
    except Exception as e: print(f"Error importing file: {e}"); return 0

def export_to_json(database, filename):
    """Export customers to JSON file.
    
    Exports first name and both phone numbers to customer_phone.json format.
    
    Args:
        database (Database): Database object containing customers
        filename (str): Path to output JSON file
        
    Returns:
        int: Number of customers exported, 0 if error or no data
        
    Raises:
        Exception: Caught and reported as error message
    """
    customers = database.get_all_customers()
    if not customers: print("No customers to export."); return 0
    try:
        data = [{"first_name": c.first_name, "phone1": c.phone1, "phone2": c.phone2} for c in customers]
        with open(filename, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
        print(f"Successfully exported {len(data)} customers to {filename}")
        return len(data)
    except Exception as e: print(f"Error exporting to JSON: {e}"); return 0

def export_to_csv(database, filename):
    """Export customers to CSV file.
    
    Exports first name, last name, county, and state to customer_location.csv format.
    
    Args:
        database (Database): Database object containing customers
        filename (str): Path to output CSV file
        
    Returns:
        int: Number of customers exported, 0 if error or no data
        
    Raises:
        Exception: Caught and reported as error message
    """
    customers = database.get_all_customers()
    if not customers: print("No customers to export."); return 0
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["First Name", "Last Name", "County", "State"])
            for customer in customers: writer.writerow([customer.first_name, customer.last_name, customer.county, customer.state])
        print(f"Successfully exported {len(customers)} customers to {filename}")
        return len(customers)
    except Exception as e: print(f"Error exporting to CSV: {e}"); return 0
