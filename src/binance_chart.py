import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # Use a non-interactive backend

def get_binance_klines(symbol, interval='1d', limit=100):
    """
    Fetches k-line/candlestick data from the Binance API.

    Args:
        symbol (str): The trading symbol (e.g., "BTCUSDT").
        interval (str, optional): The interval for the k-lines. Defaults to '1d'.
        limit (int, optional): The number of k-lines to fetch. Defaults to 100.

    Returns:
        list: A list of k-line data, or None if the request fails.
    """
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def plot_price_chart(data, symbol):
    """
    Plots a price chart from k-line data and saves it to a file.

    Args:
        data (list): A list of k-line data from the Binance API.
        symbol (str): The trading symbol for labeling the chart.
    """
    if not data:
        print("No data to plot.")
        return

    df = pd.DataFrame(data, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])

    # Convert timestamp to datetime and numeric columns to float
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df['close'] = pd.to_numeric(df['close'])

    plt.figure(figsize=(12, 6))
    plt.plot(df['open_time'], df['close'], label=f'{symbol} Close Price')
    plt.title(f'{symbol} Price History')
    plt.xlabel('Date')
    plt.ylabel('Price (USDT)')
    plt.grid(True)
    plt.legend()

    chart_filename = f'{symbol.lower()}_chart.png'
    plt.savefig(chart_filename)
    print(f"Chart saved as {chart_filename}")

def main():
    """
    Main function to fetch k-line data and generate a price chart.
    """
    symbol = "BTCUSDT"
    klines = get_binance_klines(symbol, interval='1d', limit=365) # Get daily data for the last year

    if klines:
        plot_price_chart(klines, symbol)

if __name__ == "__main__":
    main()
