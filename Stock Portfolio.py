import yfinance as yf


portfolio = {}

def add_stock(symbol, quantity):
    """Add stock to portfolio"""
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity
    print(f"Added {quantity} shares of {symbol}.")

def remove_stock(symbol, quantity):
    """Remove stock from portfolio"""
    if symbol in portfolio and portfolio[symbol] >= quantity:
        portfolio[symbol] -= quantity
        if portfolio[symbol] == 0:
            del portfolio[symbol]
        print(f"Removed {quantity} shares of {symbol}.")
    else:
        print(f"Can't remove {quantity} shares of {symbol}.")

def view_portfolio():
    """View portfolio with stock prices"""
    if portfolio:
        total_value = 0
        for symbol, quantity in portfolio.items():
            stock = yf.Ticker(symbol)
            data = stock.history(period="1d")
            if data.empty:
                print(f"No data for {symbol}")
                continue
            price = data['Close'].iloc[-1]
            value = price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total portfolio value: ${total_value:.2f}")
    else:
        print("Your portfolio is empty!")

def main():
    """Run the portfolio tracker"""
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input(f"How many shares of {symbol}: "))
            add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            quantity = int(input(f"How many shares of {symbol} to remove: "))
            remove_stock(symbol, quantity)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Thank you for using the Stock Portfolio Tracker! Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
