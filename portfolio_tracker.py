import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['Time Series (5min)']

def calculate_portfolio_value(portfolio):
    total_value = 0
    for symbol, name in portfolio.items():
        stock_data = get_stock_data(symbol)
        latest_close_price = float(list(stock_data.values())[0]['4. close'])
        total_value += latest_close_price
        print(f"{name} ({symbol}): ${latest_close_price:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = {
        'AAPL': 'Apple Inc.',
        'MSFT': 'Microsoft Corporation',
        'GOOGL': 'Alphabet Inc. (Google)',
        'AMZN': 'Amazon.com Inc.',
        'TSLA': 'Tesla Inc.',
        # Add more stocks and their symbols here
    }

    calculate_portfolio_value(portfolio)

if __name__ == '__main__':
    main()
