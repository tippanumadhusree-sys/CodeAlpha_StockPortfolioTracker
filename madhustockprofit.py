Stock prices dictionary

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 320
}

total_investment = 0


stock_name = input("Enter stock name: ").upper()

quantity = int(input("Enter quantity: "))


if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("Stock:", stock_name)
    print("Price per share:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total_investment)

else:
    print("Stock not found")
