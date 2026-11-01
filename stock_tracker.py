"""CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("Type 'done' when finished.\n")

    portfolio = {}   # stock -> quantity

    while True:
        stock = input("Stock name: ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found. Choose from the list above.\n")
            continue
        try:
            qty = int(input(f"Quantity of {stock}: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.\n")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"Added {qty} x {stock}.\n")

    if not portfolio:
        print("No stocks entered.")
        return

    total = 0
    lines = ["Stock,Quantity,Price,Value"]
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        value = qty * STOCK_PRICES[stock]
        total += value
        print(f"{stock}: {qty} x ${STOCK_PRICES[stock]} = ${value}")
        lines.append(f"{stock},{qty},{STOCK_PRICES[stock]},{value}")
    print(f"TOTAL INVESTMENT VALUE: ${total}")
    lines.append(f"TOTAL,,,{total}")

    if input("\nSave result to file? (y/n): ").strip().lower() == "y":
        choice = input("Format - txt or csv? ").strip().lower()
        ext = "csv" if choice == "csv" else "txt"
        with open(f"portfolio.{ext}", "w") as f:
            if ext == "csv":
                f.write("\n".join(lines) + "\n")
            else:
                f.write("Portfolio Summary\n-----------------\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} x ${STOCK_PRICES[stock]} = ${qty * STOCK_PRICES[stock]}\n")
                f.write(f"TOTAL: ${total}\n")
        print(f"Saved to portfolio.{ext}")


if __name__ == "__main__":
    main()
