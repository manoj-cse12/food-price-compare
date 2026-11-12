dish = input("Enter the dish name: ")
menu_price = int(input("Enter the menu price: "))
delivery_fee = int(input("Enter the delivery fee: "))

total = menu_price + delivery_fee

if total >= 400:
    total = total - total * 0.15

print("The total price for", dish, "is:", total)