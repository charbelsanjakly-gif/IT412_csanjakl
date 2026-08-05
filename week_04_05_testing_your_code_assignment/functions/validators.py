def validate_description(description):
    """Return True if description contains only alphanumeric characters and spaces."""
    return all(char.isalnum() or char.isspace() for char in description) and description.strip() != ''


def validate_price(price):
    """Return True if price can be represented as a float."""
    try:
        float(price)
        return True
    except (TypeError, ValueError):
        return False


def validate_quantity(quantity):
    """Return True if quantity is a whole number."""
    try:
        return float(quantity).is_integer()
    except (TypeError, ValueError):
        return False
