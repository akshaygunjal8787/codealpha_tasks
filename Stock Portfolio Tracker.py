# Step 1: Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 140,   # Google
    "AMZN": 190,   # Amazon
    "MSFT": 330    # Microsoft
}

portfolio = {}  # To store user's stock and quantity

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices (USD):")

# Step 2: Display available stocks
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Step 3: Take user input
while True:
    stock_name = input("\nEnter stock symbol to buy (e.g., AAPL): ").upper()

    # Validate stock name
    if stock_name not in stock_prices:
        print("Invalid stock symbol. Please choose from the list above.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name} shares: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    # Store in portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Ask user if they want to add more stocks
    choice = input("Do you want to add another stock? (yes/no): ").lower()
    if choice != "yes":
        break

# Step 4: Calculate total investment
total_value = 0
print("\n Your Stock Portfolio Summary:")
print("-" * 35)
print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value'}")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock:<10}{qty:<10}${price:<10}${value}")

print("-" * 35)
print(f"Total Investment Value: ${total_value}")

# Step 5: Ask to save results to file
save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    # Choose file format
    file_type = input("Enter file type (txt/csv): ").lower()
    
    if file_type == "txt":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-" * 35 + "\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                file.write(f"{stock}: {qty} shares @ ${price} each = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}")
        print(" Summary saved as 'portfolio_summary.txt'")
    
    elif file_type == "csv":
        import csv
        with open("portfolio_summary.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total_value])
        print(" Summary saved as 'portfolio_summary.csv'")
    
    else:
        print(" Invalid file type. File not saved.")

print("\n Thank you for using the Stock Portfolio Tracker!")
