import requests

def get_exchange_rate(from_currency, to_currency):
  api_key = "aJikZSNMBcnaPO5QygrppGhp0KbFImH81"
  base_url = "https://api.apilayer.com/currency_data/convert?to={to}&from={from}&amount={amount}"
  params = {
    "app_id": api_key,
    "base": from_currency,
    "symbols": to_currency
  }
  response = requests.get(base_url, params=params)
  data = response.json()
  return data["rates"][to_currency]

def convert_currency(amount, from_currency, to_currency):
  exchange_rate = get_exchange_rate(from_currency, to_currency)
  return amount * exchange_rate

def main():
  # Get the amount to convert and the currencies to convert between
  amount = float(input("Enter the amount to convert: "))
  from_currency = input("Enter the currency to convert from (e.g. USD): ")
  to_currency = input("Enter the currency to convert to (e.g. EUR): ")

  # Convert the currency and print the result
  result = convert_currency(amount, from_currency, to_currency)
  print(f"{amount} {from_currency} is equal to {result} {to_currency}")

if __name__ == "__main__":
  main()
