import yfinance as yf

ticker = "NVDA"
stock = yf.Ticker(ticker)
price_data = stock.history(period="max")
print(price_data)
price_data.to_csv("nvda_prices.csv")

ticker = 'BTC-USD'
crypto = yf.Ticker(ticker)
price_data = crypto.history(period='1mo')
print(price_data.head())
price_data.to_csv("BTC-USD_prices.csv")

ticker = 'ETH-USD'
crypto = yf.Ticker(ticker)
price_data = crypto.history(period='max')
print(price_data.head())
price_data.to_csv("ETH-USD_prices.csv")