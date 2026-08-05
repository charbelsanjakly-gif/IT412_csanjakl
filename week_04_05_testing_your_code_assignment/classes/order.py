from datetime import date


class Order:
    """Represents a customer order: date, order number, item list, and running total."""

    def __init__(self, order_number, order_date=None):
        self.order_number = order_number
        self.order_date = order_date if order_date else date.today()
        self.items = []
        self.total = 0.0

    def add_item(self, item):
        """Add an InventoryItem to the order and update the total."""
        self.items.append(item)
        self.total += item.get_total_price()

    def remove_item(self, item):
        """Remove an InventoryItem from the order and update the total."""
        if item in self.items:
            self.items.remove(item)
            self.total -= item.get_total_price()
