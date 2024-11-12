import requests
import time

# API configuration
API_KEY = 'your_api_key'  # Replace with your actual API key
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio data structure
portfolio = {}

# Function to fetch real-time stock price
def fetch_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        latest_time = list(data['Time Series (5min)'].keys())[0]
        latest_price = float(data['Time Series (5min)'][latest_time]['1. open'])
        return latest_price
    except KeyError:
        print(f"Error fetching data for {symbol}. Please check the symbol or try again later.")
        return None

# Function to add a stock to the portfolio
def add_stock(symbol, shares):
    price = fetch_stock_price(symbol)
    if price:
        portfolio[symbol] = {'shares': shares, 'price': price}
        print(f"Added {shares} shares of {symbol} at ${price:.2f} each.")

# Function to remove a stock from the portfolio
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from your portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")

# Function to calculate total portfolio value
def calculate_portfolio_value():
    total_value = 0
    for symbol, info in portfolio.items():
        current_price = fetch_stock_price(symbol)
        if current_price:
            stock_value = info['shares'] * current_price
            total_value += stock_value
            print(f"{symbol}: {info['shares']} shares at ${current_price:.2f} = ${stock_value:.2f}")
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    return total_value

# Main menu
def main():
    print("Welcome to the Stock Portfolio Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add stock to portfolio")
        print("2. Remove stock from portfolio")
        print("3. View portfolio value")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            calculate_portfolio_value()
        elif choice == '4':
            print("Exiting the Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()
