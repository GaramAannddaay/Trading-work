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