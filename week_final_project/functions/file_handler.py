"""
file_handler module

Contains functions for importing and parsing customer data from files.
"""

from classes.customer import Customer


def parse_customer_line(line):
    """
    Parse a single line from the customer export file.

    The file format uses ## as delimiters. Expected format:
    ##first##\##last##\##company##\##address##\##city##\##county##\##state##\##zip##\##phone1##\##phone2##\##email##\####\####

    Args:
        line -- a single line from the customer export file

    Returns:
        A Customer object if parsing succeeds, None otherwise
    """
    try:
        # Split by ## and filter out empty strings
        parts = [p.strip() for p in line.split("##")]
        parts = [p for p in parts if p]  # Remove empty values

        # Check we have at least the required fields
        if len(parts) < 11:
            return None

        # Create customer with parsed data
        customer = Customer(
            first_name=parts[0],
            last_name=parts[1],
            company_name=parts[2],
            address=parts[3],
            city=parts[4],
            county=parts[5],
            state=parts[6],
            zip_code=parts[7],
            phone1=parts[8],
            phone2=parts[9],
            email=parts[10]
        )

        return customer
    except Exception as e:
        print(f"Error parsing line: {e}")
        return None


def import_customer_file(filename, database):
    """
    Import customers from a text file into the database.

    Clears the database before importing. Skips the header line.

    Args:
        filename -- path to the customer export file
        database -- Database object to populate

    Returns:
        Number of customers imported
    """
    count = 0

    try:
        # Clear existing data
        database.clear_all()

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Skip header line (first line)
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue

            customer = parse_customer_line(line)
            if customer:
                database.add_customer(customer)
                count += 1

        print(f"Successfully imported {count} customers.")
        return count

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error importing file: {e}")
        return 0
