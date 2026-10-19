# =========================================================
# PROJECT: Stock Portfolio Performance Tracker
# INTERNSHIP: Datheon Python Programming Internship
# DEVELOPER: Auwal Mohammed Bello
# LANGUAGE: Python
# NOTE: Prices are sample data, not live market prices.
# =========================================================

import csv

portfolio = [
    {
        "ticker": "AAPL",
        "buy_price": 175.00,
        "quantity": 10,
        "current_price": 182.50
    },
    {
        "ticker": "MSFT",
        "buy_price": 400.00,
        "quantity": 5,
        "current_price": 420.00
    },
    {
        "ticker": "GOOGL",
        "buy_price": 150.00,
        "quantity": 8,
        "current_price": 145.00
    }
]

total_invested = 0.0
total_market_value = 0.0
rows = []

print("=" * 55)
print("STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 55)

print("Note: Prices are sample prices, not live market data.\n")

for stock in portfolio:
    ticker = stock["ticker"]
    buy_price = stock["buy_price"]
    quantity = stock["quantity"]
    current_price = stock["current_price"]

    invested = buy_price * quantity
    market_value = current_price * quantity
    profit_loss = market_value - invested

    if invested:
        percentage = (profit_loss / invested) * 100
    else:
        percentage = 0

    total_invested += invested
    total_market_value += market_value

    rows.append({
        "Ticker": ticker,
        "Buy Price": f"{buy_price:.2f}",
        "Quantity": quantity,
        "Current Price": f"{current_price:.2f}",
        "Invested": f"{invested:.2f}",
        "Market Value": f"{market_value:.2f}",
        "Profit/Loss": f"{profit_loss:.2f}",
        "Return (%)": f"{percentage:.2f}"
    })

    print(f"Stock: {ticker}")
    print(f"  Total invested: ${invested:,.2f}")
    print(f"  Current value:  ${market_value:,.2f}")
    print(f"  Profit/Loss:    ${profit_loss:,.2f}")
    print(f"  Return:          {percentage:.2f}%")
    print("-" * 40)

total_profit_loss = total_market_value - total_invested

if total_invested:
    total_return = (total_profit_loss / total_invested) * 100
else:
    total_return = 0

print("\nPORTFOLIO SUMMARY")
print("=" * 40)
print(f"Total invested:     ${total_invested:,.2f}")
print(f"Total market value: ${total_market_value:,.2f}")
print(f"Total profit/loss:  ${total_profit_loss:,.2f}")
print(f"Total return:        {total_return:.2f}%")

csv_file = "portfolio_summary.csv"

with open(csv_file, "w", newline="") as file:
    fieldnames = [
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested",
        "Market Value",
        "Profit/Loss",
        "Return (%)"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nPortfolio report saved to: {csv_file}")
