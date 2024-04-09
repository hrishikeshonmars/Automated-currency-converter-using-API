import requests

API_KEY = 'fca_live_HzkVgZF9zPJqwsgz152205K5lKjhE00bwKlRUZSw'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "EUR", "AUD", "CNY", "CAD", "INR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("invalid currency")
        return None

while True:
    base = input("enter the base currency (q for quit):").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    amount = float(input("enter the amount to convert:"))

    for ticker, rate in data.items():
        converted_amount = amount * rate
        print(f"{amount} {base} is equal to {converted_amount} {ticker}")