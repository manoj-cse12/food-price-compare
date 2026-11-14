# Food Price Comparison

Compares the final price of a dish on Swiggy and Zomato after applying each
app's offer, delivery fee and platform fee, and shows which one is cheapest.

**Live demo:** https://food-price-compare-ryzzotv6shwh9geccgim88.streamlit.app/

![App screenshot](screenshot.png)
## Why I built this

The menu price on a delivery app is not what you pay. Each app has its own
discount rules (minimum order, percent off, maximum discount), delivery fee
and platform fee. An app with a higher menu price can still be cheaper
overall, so this tool works out the real total for each app.

## How it works

For each app, the final price is:

    menu price - discount + delivery fee + platform fee

- The discount applies only if the menu price meets the app's minimum order.
- The discount is a percentage of the menu price, limited by a maximum cap.

**Example:** Masala Dosa costs 120 on Swiggy and 110 on Zomato. Swiggy's offer
needs a 150 minimum order, so there is no discount there. Zomato's 15% offer
applies, so Zomato is cheaper even though the dosa is priced lower on both.

## Run it on your computer

1. Install Python 3
2. Install Streamlit: `pip install streamlit`
3. Run: `python -m streamlit run app.py`
4. Open http://localhost:8501

## Files

- `app.py`: the Streamlit web app and the price calculation
- `prices.csv`: dish prices and offers for each app
- `requirements.txt`: the packages needed to run it

## About the data

The prices and offers in `prices.csv` are **sample data for learning**, not
live prices from Swiggy or Zomato. To compare real prices, edit the CSV with
the values you see on each app.

## Built with

Python, Streamlit and the built-in `csv` module.

## Ideas for improvement

- Add more apps and restaurants
- Let users submit prices they see
- Add taxes and packaging charges