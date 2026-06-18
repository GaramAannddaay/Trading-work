# 1 basic function
def greet():
    print("Markets are open")

greet()   # call it

# 2 function with inputs (parameters)
def pct_return(buy_price, sell_price):
    return (sell_price - buy_price) / buy_price * 100
result = pct_return(100, 120)
print(f"{result:.2f}%")   # 20.00%

# 3 using it for real trades
print(pct_return(150.00, 182.50))   # AAPL
print(pct_return(200.00, 175.00))   # TSLA (loss)
print(pct_return(400.00, 425.30))   # MSFT

# 4 function with lable
def pct_return(buy_price, sell_price, ticker = "unknown"):
    result = (sell_price - buy_price) / buy_price * 100
    direction = "PROFIT" if result > 0 else "loss"
    print(f"{ticker}: {result:.2f}% - {direction}")

pct_return(150.00, 182.50, "AAPL")
pct_return(200.00, 175.00, "TSLA")
pct_return(400.00, 425.30)      # no ticker given, uses "unknow"

# 5 scan whole portfolio using a function
portfolio = {
    "AAPL": (150.00, 185.50),
    "TSLA": (200.00, 175.00),
    "MSFT": (400.00, 425.30),
    "NVDA": (500.00, 788.10),
}

def pct_return(buy, sell):
    return (sell-buy) / buy * 100

for ticker, (buy, sell) in portfolio.items():
    r = pct_return(buy, sell)
    signal = "profit" if r > 0 else "loss"
    print(f"{ticker}: {r:.2f}% ({signal})")
          