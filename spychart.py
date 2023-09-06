import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for SPY ETF for a full year
data = yf.download("SPY", start="2021-01-01", end="2023-09-05")

# Calculate 50-day and 200-day Simple Moving Averages (SMA)
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the SMAs
ax.plot(data['Close'], label='Close Price', color='blue')
ax.plot(data['SMA50'], label='50-day SMA', color='orange')
ax.plot(data['SMA200'], label='200-day SMA', color='red')

plt.title('50-day and 200-day SMAs for SPY ETF (1-Year Data)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
