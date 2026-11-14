import csv
import streamlit as st

PLATFORM_FEES = {"Swiggy": 6, "Zomato": 8}


def final_price(menu_price, delivery_fee, min_order, percent_off, cap, platform_fee):
    if menu_price >= min_order:
        discount = min(menu_price * percent_off / 100, cap)
    else:
        discount = 0
    return menu_price - discount + delivery_fee + platform_fee


st.title("Food Price Comparison")

with open("prices.csv") as file:
    rows = list(csv.DictReader(file))

dishes = sorted(set(row["dish"] for row in rows))
dish = st.selectbox("Choose a dish", dishes)

results = []
cheapest_app = ""
cheapest_price = None

for row in rows:
    if row["dish"] == dish:
        price = final_price(
            int(row["menu_price"]),
            int(row["delivery_fee"]),
            int(row["min_order"]),
            int(row["percent_off"]),
            int(row["cap"]),
            PLATFORM_FEES.get(row["app"], 0),
        )
        results.append({"App": row["app"], "Final price": price})
        if cheapest_price is None or price < cheapest_price:
            cheapest_price = price
            cheapest_app = row["app"]

for item in results:
    st.write(f"{item['App']}: ₹{item['Final price']:.2f}")

st.success(f"Cheapest: {cheapest_app} at ₹{cheapest_price:.2f}")

