import requests

def get_world_bank_data(indicator, country_code="all", date_range="2010:2020"):
    """
    Fetches data from the World Bank API.

    Args:
        indicator (str): The indicator ID to fetch data for.
        country_code (str, optional): The country code. Defaults to "all".
        date_range (str, optional): The date range. Defaults to "2010:2020".

    Returns:
        list: A list of data points, or None if the request fails.
    """
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={date_range}&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if len(data) > 1 and data[1] is not None:
            return data[1]
        else:
            print("No data found for the given parameters.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to fetch and display World Bank data.
    """
    # Example: Total population (SP.POP.TOTL) for all countries from 2015 to 2020
    indicator = "SP.POP.TOTL"
    data = get_world_bank_data(indicator, date_range="2015:2020")

    if data:
        # Sort data by country name and then by year
        sorted_data = sorted(data, key=lambda x: (x['country']['value'], x['date']))

        print(f"Data for indicator: {sorted_data[0]['indicator']['value']}")
        print("-" * 70)
        print(f"{'Country':<35} | {'Year':<10} | {'Population':<20}")
        print("-" * 70)

        for entry in sorted_data:
            country = entry['country']['value']
            year = entry['date']
            value = entry['value']

            if value is not None:
                population_str = f"{value:,.0f}"
            else:
                population_str = "N/A"

            print(f"{country:<35} | {year:<10} | {population_str:<20}")

        print("-" * 70)

if __name__ == "__main__":
    main()
