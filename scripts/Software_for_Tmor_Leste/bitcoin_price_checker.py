import requests

def get_bitcoin_price(currency):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data["bitcoin"][currency]
        return price
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching Bitcoin price:", e)
        return None

def main():
    print("Welcome to the Bitcoin Price Checker!")
    while True:
        currency = input("Enter the currency code (e.g., USD, EUR, GBP) or 'q' to quit: ")
        if currency.lower() == 'q':
            break
        price = get_bitcoin_price(currency.lower())
        if price is not None:
            print(f"The current price of Bitcoin in {currency.upper()} is: {price}")
        print()

if __name__ == "__main__":
    main()