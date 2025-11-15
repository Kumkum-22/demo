menu={
    "pizza": 50,
    "burger": 30,
    'pasta': 40,
    'salad': 20,
    'dessert': 25   
}
print("Welcome to the Hotel!")
print("Menu:\n Pizza: $50 \n Burger: $30 \n Pasta: $40 \n Salad: $20 \n Dessert: $25")
order_total=0
item=input("Please enter the item you want to order: ")
if item in menu:
    order_total+=menu[item]
    print(f"{item} added to your order. Current total: ${order_total}")
else:
    print("Sorry, we don't have that item on the menu.")
more=input("Would you like to order another item? (yes/no): ")
if more=="yes":
    item=input("Please enter the second item you want to order: ")
    if item in menu:
        order_total+=menu[item]
        print(f"{item} added to your order. Current total: ${order_total}")
    else:
        print("Ordered{item} is not available.")
print(f"Your final order total is: ${order_total}")