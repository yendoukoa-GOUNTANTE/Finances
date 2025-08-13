import requests

def get_binance_price(symbol):
    """
    Fetches the latest price for a given symbol from the Binance API.

    Args:
        symbol (str): The trading symbol (e.g., "BTCUSDT").

    Returns:
        str: The latest price as a string, or None if the request fails.
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data.get('price')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to fetch and display the BTC/USDT price.
    """
    symbol = "BTCUSDT"
    price = get_binance_price(symbol)

    if price:
        print(f"The latest price of {symbol} is: {price}")

if __name__ == "__main__":
    main()
