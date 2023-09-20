import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbols
symbols = ["SPY", "MSFT", "NVDA", "AAPL", "AMZN", "GOOGL", "NFLX"]

# Create a dictionary to store data for each stock
stock_data = {}

# Download historical data for each stock
for symbol in symbols:
    stock_data[symbol] = yf.download(symbol, start="2013-09-01", end="2023-09-01")

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the closing prices for each stock
for symbol in symbols:
    ax.plot(stock_data[symbol]['Close'], label=f'{symbol} Close Price')

plt.title('Comparison of SPY, MSFT, and NVDA Closing Prices (Past 10 Years)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
