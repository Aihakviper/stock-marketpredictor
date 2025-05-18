import yfinance as yf

ticker = "DXY"
data = yf.download(ticker, start="2018-01-01", end="2024-12-31")
print(data.head())

data.to_csv("aapl_stock_data.csv")

import matplotlib.pyplot as plt

data["Close"].plot(figsize=(12, 6), title=f"{ticker} Closing Price")
plt.grid(True)
plt.show()
