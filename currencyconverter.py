import urllib.request
import json

def convert_currency(amount, from_currency, to_currency):
    # Make an HTTP GET request to the currency exchange rate API
    with urllib.request.urlopen(f"https://api.exchangerate-api.com/v4/latest/{from_currency}") as response:
        # Read the response data
        data = response.read()

    # Convert the response data to a Python dictionary
    data = json.loads(data)

    # Get the exchange rate for the given currencies
    exchange_rate = data['rates'][to_currency]

    # Convert the amount of the from_currency to the to_currency
    return amount * exchange_rate

# type currency you want to exchange here:
amount = 100
from_currency = "USD"
to_currency = "EUR"
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
