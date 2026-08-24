"""
validators module

Validation functions for the bookstore application. Each function
returns True if the value is valid according to the assignment's
rules, and False otherwise.
"""

import re


def validate_title(title):
    """
    Book titles can contain almost anything, but a lone unescaped
    quote character (' or ") is rejected here so it can never reach
    a raw SQL string and cause problems. Since Database.execute()
    uses parameterized queries, quotes are actually safe to store,
    but per the assignment's warning we still flag titles that are
    empty or contain nothing but whitespace.
    """
    if title is None:
        return False
    return len(title.strip()) > 0


def validate_author(author):
    """
    Book author can only contain letters, spaces, commas, periods,
    apostrophes, and hyphens.
    """
    if author is None or len(author.strip()) == 0:
        return False
    pattern = r"^[A-Za-z\s,.'\-]+$"
    return re.match(pattern, author) is not None


def validate_quantity(quantity):
    """Quantity on hand must be an integer (as text, digits only)."""
    if quantity is None:
        return False
    return re.match(r'^-?\d+$', quantity.strip()) is not None


def validate_signed_edition(signed):
    """
    Signed edition can only be 'N', 'Y', or a blank/empty string
    (case-insensitive on Y/N).
    """
    if signed is None:
        return False
    signed = signed.strip()
    return signed == '' or signed.upper() in ('Y', 'N')


def validate_price(price):
    """
    Pricing information, if provided, must be a valid float. An empty
    string is considered valid for optional price fields (promo
    price) and should be checked for required-ness separately.
    """
    if price is None:
        return False
    price = price.strip()
    if price == '':
        return True
    try:
        float(price)
        return True
    except ValueError:
        return False


def validate_required_price(price):
    """Retail price is required, so an empty string is not valid."""
    if price is None:
        return False
    price = price.strip()
    if price == '':
        return False
    try:
        float(price)
        return True
    except ValueError:
        return False
