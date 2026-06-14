# 1 creating a list
tickers = ["AAPL", "TSLA", "MSFT", "NVDA", "AMZN"]
print(tickers)

#2 frabbing one item (indexing)
print(tickers[0])   # AAPL (first item)
print(tickers[2])   # MSFT (third item)
print(tickers[1])   # TSLA (second item)
print(tickers[4])   # AMZN (first item)
print(tickers[3])   # NVDA (fourth item)

#3 looking through the list
for ticker in tickers:
    print(ticker)

#4 doing something with each one
prices = [182.5, 245.3, 415.2, 788.1, 195.4]
for i in range(len(tickers)):
    print(f"{tickers[i]} costs ${prices[i]:.2f}")    

#5 adding, removing and checking
tickers.append("GOOG")   # add to the end
tickers.remove("TSLA")   # remove by name
print("AAPL" in tickers)   # true - is in the list?
print(len(tickers))      # how many ticker total?
print(tickers)