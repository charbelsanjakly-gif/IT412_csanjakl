from functions.validators import validate_description, validate_price, validate_quantity


class InventoryItem:
    """Represents a single item on an order: description, quantity, and pricing."""

    def __init__(self, description, quantity, price):
        if not validate_description(description):
            raise ValueError("Description must contain only alphanumeric characters.")
        if not validate_quantity(quantity):
            raise ValueError("Quantity must be a whole number.")
        if not validate_price(price):
            raise ValueError("Price must be a valid float value.")

        self.description = description
        self.quantity = int(quantity)
        self.price = float(price)

    def get_total_price(self):
        """Return the total price for this item (quantity * price)."""
        return self.quantity * self.price
