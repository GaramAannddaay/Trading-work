import yfinance as yf
import pandas as pd
import plotly.express as px

tickers = {"NVDA": "NVDA", "BTC-USD": "BTC-USD", "S&P 500": "^GSPC"}

closes = {}
for label, ticker in tickers.items():
    history = yf.Ticker(ticker).history(period="1y")
    closes[label] = history["Close"]

prices = pd.DataFrame(closes)
prices.index = pd.to_datetime(prices.index, utc=True)
prices = prices.ffill().dropna()

# turn each price into "% change since day 1" so they can be compared on one chart
performance = (prices / prices.iloc[0] - 1) * 100

fig = px.line(
    performance,
    x=performance.index,
    y=performance.columns,
    title="Price Performance - Last Year (NVDA vs BTC-USD vs S&P 500)",
)
fig.update_layout(yaxis_title="% Change", xaxis_title="Date", legend_title="Ticker")
fig.write_html("nvda_last_year.html")
