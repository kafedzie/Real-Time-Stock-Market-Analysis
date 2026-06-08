import requests
from config import logger, headers, url

def connect_to_api():
    stocks = ['TSLA', 'MSFT', 'GOOGL']
    json_response = []
    for stock in range(0, len(stocks)):
        querystring = {"function":"TIME_SERIES_INTRADAY",
                    "symbol":f"{stocks[stock]}",
                    "outputsize":"compact",
                    "interval":"5min",
                    "datatype":"json"}

    try

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())