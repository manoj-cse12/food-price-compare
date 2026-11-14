import csv
import streamlit as st

def final_price(menu_price, delivery_fee, min_order, percent_off):
    if menu_price >= min_order:
        discount = menu_price * percent_off / 100
    else:
        discount = 0
    return menu_price - discount + delivery_fee

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
        )
        results.append({"App": row["app"], "Final price": price})
        if cheapest_price is None or price < cheapest_price:
            cheapest_price = price
            cheapest_app = row["app"]

for item in results:
    st.write(item["App"], ": ₹", item["Final price"])

st.success("Cheapest: " + cheapest_app + " at ₹" + str(cheapest_price))