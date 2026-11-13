import csv

def final_price(menu_price, delivery_fee, min_order, percent_off):
    if menu_price >= min_order:
        discount = menu_price * percent_off / 100
    else:
        discount = 0
    return menu_price - discount + delivery_fee

dish = input("Enter the dish name: ")

cheapest_app = ""
cheapest_price = None

with open("prices.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["dish"] == dish:
            price = final_price(
                int(row["menu_price"]),
                int(row["delivery_fee"]),
                int(row["min_order"]),
                int(row["percent_off"]),
            )
            print(row["app"], price)
            if cheapest_price is None or price < cheapest_price:
                cheapest_price = price
                cheapest_app = row["app"]

if cheapest_price is None:
    print("Dish not found")
else:
    print("Cheapest:", cheapest_app, "at", cheapest_price)