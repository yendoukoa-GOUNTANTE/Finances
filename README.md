# World Bank Data Fetcher

This script fetches data from the World Bank API and displays it in the console.

## Description

The script uses the World Bank's public API to retrieve data for a specific indicator. The default example fetches the total population for all countries for the years 2015-2020. The data is then printed to the console in a formatted table.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script, simply execute the `main.py` file:

```bash
python src/main.py
```

The script will fetch the data and print it to the console. You can modify the `indicator` and `date_range` variables in the `main` function in `src/main.py` to fetch different data.
