import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for Gold and S&P 500 for the past 10 years
gold_data = yf.download("GC=F", start="2013-09-01", end="2023-09-01")
spx_data = yf.download("^GSPC", start="2013-09-01", end="2023-09-01")

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting Gold and S&P 500 spot prices
ax.plot(gold_data['Close'], label='Gold Spot Price', color='gold')
ax.plot(spx_data['Close'], label='S&P 500 Spot Price', color='blue')

plt.title('Gold Spot Price vs S&P 500 Spot Price (Past 10 Years)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
