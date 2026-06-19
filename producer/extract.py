import requests
from config import logger, headers, url
from typing import List, Dict

def connect_to_api() -> List[Dict]:
    """
    Connects to AlphaVantage API to fetch stock market dat for predefined list of stocks.

    Sends HTTP GET requests to the API for each stock in the 'stocks' list and collects the response data

    in JSON format. Handles errors and logs the progress.
    """

    stocks = ['TSLA', 'MSFT', 'GOOGL', 'MC']
    json_response = []

    for stock in range(0, len(stocks)):
        querystring = {"function":"TIME_SERIES_INTRADAY",
                    "symbol":f"{stocks[stock]}",
                    "outputsize":"compact",
                    "interval":"5min",
                    "datatype":"json"}

        try:

            response = requests.get(url, headers=headers, params=querystring)

            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Stocks {stocks[stock]} loaded successfully")

            json_response.append(data)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error on stock: {e}")
            break
    return json_response

def extract_json(response: List[Dict]) -> List[Dict[str, str]]:
    """
    Extracts relevant stock data from the API response JSON and formats it into a list of records

    Processes the JSON response retuned by 'connect_to_api()' and extracts stock data such as symbol, date, open, close, high, low
    and returns a formatted list of records.
    """

    records = []

    for data in response:
        symbol = data['Meta Data']['2. Symbol']

        for date_str, metrics in data['Time Series (5min)'].items():
            record = {
                "symbol": symbol,
                "date": date_str,
                "open": metrics["1. open"],
                "close": metrics["4. close"],
                "high": metrics["2. high"],
                "low": metrics["3. low"]
            }

            records.append(record)
    return records