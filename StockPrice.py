# --- Stock Portfolio Tracker ---

# Step 1: Hardcode some stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "AMZN": 130,   # Amazon
    "MSFT": 330    # Microsoft
}

# Step 2: Take user input
portfolio = {}  # to store stock name and quantity

print("Enter your stock holdings.")
print("Type 'done' when finished.\n")

while True:
    stock_name = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Step 3: Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
print("-----------------------")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("-----------------------")
print(f"💰 Total Investment Value: ${total_investment}")

# Step 4 (Optional): Save results to a text file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        file.write("-----------------------\n")
        file.write(f"Total Investment Value: ${total_investment}\n")
    print("✅ Portfolio summary saved as 'portfolio_summary.txt'.")
else:
    print("✅ Program ended without saving.")