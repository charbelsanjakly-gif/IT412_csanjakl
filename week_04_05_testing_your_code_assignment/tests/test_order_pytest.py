import pytest
from classes.order import Order
from classes.inventory_item import InventoryItem


@pytest.fixture
def order():
    return Order(order_number=1001)


@pytest.fixture
def items():
    return InventoryItem("Widget", 3, 9.99), InventoryItem("Gadget", 1, 24.50)


def test_add_item_updates_total(order, items):
    item1, _ = items
    order.add_item(item1)
    assert order.total == pytest.approx(29.97)
    assert item1 in order.items


def test_add_multiple_items_updates_total(order, items):
    item1, item2 = items
    order.add_item(item1)
    order.add_item(item2)
    assert order.total == pytest.approx(54.47)


def test_remove_item_updates_total(order, items):
    item1, item2 = items
    order.add_item(item1)
    order.add_item(item2)
    order.remove_item(item2)
    assert order.total == pytest.approx(29.97)
    assert item2 not in order.items
