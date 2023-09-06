import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for AAPL for the past 90 days
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="120d")

# Extract the date and closing price
date = hist.index
close_price = hist['Close']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(date, close_price, label='AAPL Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price (in USD)')
plt.title('AAPL Close Price for the Past 120 Days')
plt.grid(True)
plt.legend()
plt.show()
