# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 300,
    "AMZN": 170
}

total = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    stock = input("Enter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        value = stock_prices[stock] * quantity
        total += value
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)
file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total))
file.close()
print("Result saved to portfolio.txt")