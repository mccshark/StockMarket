import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

# Define the stock symbols
symbols = ["SPY", "MSFT", "NVDA", "AAPL", "AMZN", "GOOGL", "NFLX"]

# Prompt the user for the number of years
years = int(input("Enter the number of years for the chart: "))

# Prompt the user for the number of months
months = int(input("Enter the number of months for the chart: "))

# Calculate the start date based on the user input
end_date = datetime.now()
start_date = end_date - timedelta(days=365 * years) - timedelta(days=30 * months)
end_date_str = end_date.strftime("%Y-%m-%d")
start_date_str = start_date.strftime("%Y-%m-%d")

# Create a dictionary to store data for each stock
stock_data = {}

# Download historical data for each stock within the specified date range
for symbol in symbols:
    stock_data[symbol] = yf.download(symbol, start=start_date_str, end=end_date_str)

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the closing prices for each stock
for symbol in symbols:
    ax.plot(stock_data[symbol]['Close'], label=f'{symbol} Close Price')

# Annotate the last price for each stock
for symbol in symbols:
    last_price = stock_data[symbol]['Close'].iloc[-1]
    ax.annotate(f'${last_price:.2f}', 
                xy=(stock_data[symbol].index[-1], last_price), 
                xytext=(-70, 20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.title(f'Comparison of Stock Closing Prices ({years} Years and {months} Months)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()