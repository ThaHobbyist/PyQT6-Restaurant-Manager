from manage_db import add_menu_item

menu_items = [
    ("Pizza", 12.99),
    ("Burger", 8.99),
    ("Pasta", 10.99),
    ("Salad", 7.99),
    ("Soda", 1.99)
]

for item_name, price in menu_items:
    add_menu_item(item_name, price)