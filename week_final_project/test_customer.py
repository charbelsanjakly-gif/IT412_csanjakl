"""test_customer module"""
import unittest
from classes.customer import Customer
class TestCustomerValidation(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", "Doe", "Acme Corp", "123 Main St", "Detroit", "Wayne", "MI", "48201", "5551234567", "5559876543", "john@example.com")
    def test_valid_name(self):
        self.assertTrue(self.customer.is_valid_name("John"))
        self.assertTrue(self.customer.is_valid_name("Mary-Jane"))
    def test_invalid_name(self):
        self.assertFalse(self.customer.is_valid_name("John123"))
    def test_valid_phone(self):
        self.assertTrue(self.customer.is_valid_phone("5551234567"))
    def test_invalid_phone(self):
        self.assertFalse(self.customer.is_valid_phone("123"))
    def test_valid_email(self):
        self.assertTrue(self.customer.is_valid_email("john@example.com"))
    def test_invalid_email(self):
        self.assertFalse(self.customer.is_valid_email("invalid.email"))
    def test_valid_state(self):
        self.assertTrue(self.customer.is_valid_state("MI"))
    def test_invalid_state(self):
        self.assertFalse(self.customer.is_valid_state("XX"))
    def test_valid_zip(self):
        self.assertTrue(self.customer.is_valid_zip("48201"))
    def test_invalid_zip(self):
        self.assertFalse(self.customer.is_valid_zip("123"))
if __name__ == "__main__": unittest.main()
