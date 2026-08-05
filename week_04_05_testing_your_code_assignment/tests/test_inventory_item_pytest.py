import pytest
from classes.inventory_item import InventoryItem


@pytest.fixture
def item():
    return InventoryItem("Widget", 3, 9.99)


def test_valid_item_creation(item):
    assert item.description == "Widget"
    assert item.quantity == 3
    assert item.price == 9.99


def test_get_total_price(item):
    assert item.get_total_price() == pytest.approx(29.97)


def test_invalid_description_raises_error():
    with pytest.raises(ValueError):
        InventoryItem("Widget#1", 3, 9.99)


def test_invalid_quantity_raises_error():
    with pytest.raises(ValueError):
        InventoryItem("Widget", 2.5, 9.99)


def test_invalid_price_raises_error():
    with pytest.raises(ValueError):
        InventoryItem("Widget", 3, "free")
