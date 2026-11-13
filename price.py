def final_price(menu_price, delivery_fee):
    if menu_price >= 400:
        discount = menu_price * 0.15
    else:
        discount = 0
    return menu_price - discount + delivery_fee

menu_a = int(input("App A menu price: "))
delivery_a = int(input("App A delivery fee: "))
menu_b = int(input("App B menu price: "))
delivery_b = int(input("App B delivery fee: "))

price_a = final_price(menu_a, delivery_a)
price_b = final_price(menu_b, delivery_b)

print("App A:", price_a)
print("App B:", price_b)

if price_a < price_b:
    print("App A is cheaper by", price_b - price_a)
elif price_b < price_a:
    print("App B is cheaper by", price_a - price_b)
else:
    print("Both apps cost the same")