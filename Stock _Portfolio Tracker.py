# Step 1: Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Step 2: Initialize portfolio dictionary
portfolio = {}

# Step 3: Ask user how many stocks they want to enter
num_stocks = int(input("📊 How many different stocks do you want to add? "))

# Step 4: Collect stock names and quantities
for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name not in stock_prices:
        print(f"⚠️ {stock_name} is not in the price list. Skipping.")
        continue
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = quantity

# Step 5: Calculate total investment
total_investment = 0
print("\n🧾 Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Step 6: Optional — Save to a .txt file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_investment}\n")
    print("✅ Summary saved to 'portfolio_summary.txt'")
