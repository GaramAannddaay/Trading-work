# 1 reading a CSV file
import csv

with open("stocks.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2 reading as dictionaries (easier to use)
with open("stocks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# 3 using the data (math on it)
with open("stocks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        ticker = row["ticker"]
        price = float(row["price"])
        qty = int(row["qty"])
        total = price * qty
        print(f"{ticker}: ${total:.2f}")

import csv

# 1. Read all rows into memory first
with open("stocks.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    fieldnames = reader.fieldnames

# 2. Find and update AAPL's price
for row in rows:
    if row["ticker"] == "AAPL":
        row["price"] = "180.00"

# 3. Write everything back to the same file
with open("stocks.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)