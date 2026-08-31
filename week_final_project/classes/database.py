"""
database module

Contains the Database class which manages a collection of customers
stored in memory.
"""


class Database:
    """
    Manages an in-memory database of customer records.

    Provides methods to add, retrieve, update, and delete customer records.
    """

    def __init__(self):
        """Initialize an empty customer database."""
        self.customers = []

    def add_customer(self, customer):
        """
        Add a customer to the database.

        Args:
            customer -- a Customer object to add
        """
        self.customers.append(customer)

    def get_all_customers(self):
        """
        Retrieve all customers from the database.

        Returns:
            List of all Customer objects
        """
        return self.customers

    def get_customer_by_index(self, index):
        """
        Retrieve a customer by index.

        Args:
            index -- the index of the customer

        Returns:
            Customer object at the index, or None if not found
        """
        if 0 <= index < len(self.customers):
            return self.customers[index]
        return None

    def update_customer(self, index, customer):
        """
        Update a customer at a specific index.

        Args:
            index -- the index of the customer to update
            customer -- the updated Customer object

        Returns:
            True if successful, False otherwise
        """
        if 0 <= index < len(self.customers):
            self.customers[index] = customer
            return True
        return False

    def delete_customer(self, index):
        """
        Delete a customer at a specific index.

        Args:
            index -- the index of the customer to delete

        Returns:
            True if successful, False otherwise
        """
        if 0 <= index < len(self.customers):
            del self.customers[index]
            return True
        return False

    def clear_all(self):
        """Clear all customers from the database."""
        self.customers = []

    def get_customer_count(self):
        """
        Get the total number of customers in the database.

        Returns:
            Number of customers
        """
        return len(self.customers)
