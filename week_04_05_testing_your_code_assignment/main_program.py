from classes.order import Order
from classes.inventory_item import InventoryItem

order = Order(order_number=1001)

item1 = InventoryItem("Widget", 3, 9.99)
item2 = InventoryItem("Gadget", 1, 24.50)

order.add_item(item1)
order.add_item(item2)

print(f"Order #{order.order_number} - {order.order_date}")
for item in order.items:
    print(f"{item.description}: {item.quantity} x ${item.price} = ${item.get_total_price()}")
print(f"Order total: ${order.total:.2f}")

order.remove_item(item2)
print(f"After removing {item2.description}, order total: ${order.total:.2f}")
