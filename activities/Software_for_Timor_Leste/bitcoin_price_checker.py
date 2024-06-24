import requests
import json
from datetime import datetime

def get_bitcoin_price(currency='usd'):
    """
    Fetch the current Bitcoin price in the specified currency.
    
    :param currency: The currency to fetch the price in (default: USD)
    :return: A tuple containing the price and last updated time
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}&include_last_updated_at=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        price = data['bitcoin'][currency]
        last_updated = datetime.fromtimestamp(data['bitcoin']['last_updated_at']).strftime('%Y-%m-%d %H:%M:%S')
        
        return price, last_updated
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None, None

def main():
    print("Welcome to the Bitcoin Price Checker!")
    
    while True:
        currency = input("Enter the currency to check the Bitcoin price (e.g., usd, eur, jpy) or 'q' to quit: ").lower()
        
        if currency == 'q':
            print("Thank you for using the Bitcoin Price Checker. Goodbye!")
            break
        
        price, last_updated = get_bitcoin_price(currency)
        
        if price is not None:
            print(f"The current Bitcoin price is {price:,.2f} {currency.upper()}")
            print(f"Last updated: {last_updated}")
        else:
            print("Unable to fetch the Bitcoin price. Please try again.")
        
        print()  # Empty line for readability

if __name__ == "__main__":
    main()