import unittest
from classes.order import Order
from classes.inventory_item import InventoryItem


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order(order_number=1001)
        self.item1 = InventoryItem("Widget", 3, 9.99)
        self.item2 = InventoryItem("Gadget", 1, 24.50)

    def test_add_item_updates_total(self):
        self.order.add_item(self.item1)
        self.assertAlmostEqual(self.order.total, 29.97)
        self.assertIn(self.item1, self.order.items)

    def test_add_multiple_items_updates_total(self):
        self.order.add_item(self.item1)
        self.order.add_item(self.item2)
        self.assertAlmostEqual(self.order.total, 54.47)

    def test_remove_item_updates_total(self):
        self.order.add_item(self.item1)
        self.order.add_item(self.item2)
        self.order.remove_item(self.item2)
        self.assertAlmostEqual(self.order.total, 29.97)
        self.assertNotIn(self.item2, self.order.items)


if __name__ == '__main__':
    unittest.main()
