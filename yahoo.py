# pip install yfinance
import yfinance as yf

def get_stock_data(ticker_symbol, start_date, end_date):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data

# Example usage:
data = get_stock_data("AAPL", "2022-01-01", "2022-12-31")
print(data)