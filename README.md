# World Bank and Binance API Integrations

This project contains Python scripts to fetch data from the World Bank API and the Binance API.

## World Bank Data Fetcher

This script fetches data from the World Bank API and displays it in the console.

### Description

The script uses the World Bank's public API to retrieve data for a specific indicator. The default example fetches the total population for all countries for the years 2015-2020. The data is then printed to the console in a formatted table.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the World Bank script, execute the `main.py` file:

```bash
python src/main.py
```

---

## Binance Integrations

This project also includes scripts to interact with the Binance API.

### Binance Price Ticker

This script fetches the latest price of a cryptocurrency trading pair from the Binance API and displays it in the console.

**Usage:**

```bash
python src/binance_integration.py
```

### Binance Price Chart

This script fetches historical k-line data for a trading pair and generates a price chart, which is saved as a PNG image.

**Usage:**

```bash
python src/binance_chart.py
```

This will create a file named `btcusdt_chart.png` in the root directory. You can change the symbol and other parameters in the `main` function of `src/binance_chart.py`.
