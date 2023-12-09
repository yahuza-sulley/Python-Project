import yfinance as yf

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        stock_data = yf.Ticker(symbol)
        current_price = stock_data.history(period='1d')['Close'].iloc[-1]
        self.portfolio[symbol] = {'quantity': quantity, 'current_price': current_price}

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"{symbol} removed from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def track_performance(self):
        total_value = 0
        print("\nPortfolio Performance:")
        for symbol, data in self.portfolio.items():
            value = data['quantity'] * data['current_price']
            total_value += value
            print(f"{symbol}: Quantity - {data['quantity']}, Current Price - ${data['current_price']:.2f}, Value - ${value:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio_tracker = StockPortfolioTracker()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio_tracker.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            portfolio_tracker.remove_stock(symbol)
        elif choice == "3":
            portfolio_tracker.track_performance()
        elif choice == "4":
            print("Exiting the portfolio tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
