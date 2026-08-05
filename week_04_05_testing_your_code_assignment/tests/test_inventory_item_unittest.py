import unittest
from classes.inventory_item import InventoryItem


class TestInventoryItem(unittest.TestCase):

    def setUp(self):
        self.item = InventoryItem("Widget", 3, 9.99)

    def test_valid_item_creation(self):
        self.assertEqual(self.item.description, "Widget")
        self.assertEqual(self.item.quantity, 3)
        self.assertEqual(self.item.price, 9.99)

    def test_get_total_price(self):
        self.assertAlmostEqual(self.item.get_total_price(), 29.97)

    def test_invalid_description_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem("Widget#1", 3, 9.99)

    def test_invalid_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem("Widget", 2.5, 9.99)

    def test_invalid_price_raises_error(self):
        with self.assertRaises(ValueError):
            InventoryItem("Widget", 3, "free")


if __name__ == '__main__':
    unittest.main()
