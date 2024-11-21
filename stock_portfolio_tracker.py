import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity, purchase_price):
        """Add a stock to the portfolio."""
        if ticker in self.portfolio:
            print(f"{ticker} is already in your portfolio. Updating the quantity and purchase price.")
            self.portfolio[ticker]['quantity'] += quantity
            self.portfolio[ticker]['purchase_price'] = purchase_price
        else:
            self.portfolio[ticker] = {
                'quantity': quantity,
                'purchase_price': purchase_price
            }

    def remove_stock(self, ticker):
        """Remove a stock from the portfolio."""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"{ticker} has been removed from your portfolio.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def get_current_prices(self):
        """Fetch current prices for all stocks in the portfolio."""
        tickers = list(self.portfolio.keys())
        prices = {}
        for ticker in tickers:
            stock = yf.Ticker(ticker)
            prices[ticker] = stock.history(period="1d")['Close'][-1]
        return prices

    def calculate_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        current_prices = self.get_current_prices()
        total_value = 0
        print("\nPortfolio Summary:")
        for ticker, details in self.portfolio.items():
            quantity = details['quantity']
            purchase_price = details['purchase_price']
            current_price = current_prices[ticker]
            stock_value = current_price * quantity
            total_value += stock_value

            print(f"{ticker}: Quantity = {quantity}, Purchase Price = ${purchase_price:.2f}, "
                  f"Current Price = ${current_price:.2f}, Value = ${stock_value:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        return total_value

# Main Program
def main():
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Value")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            portfolio.add_stock(ticker, quantity, purchase_price)
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == "3":
            portfolio.calculate_portfolio_value()
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
