import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd

ticker = "DXY"
data = pd.read_csv("dxy_stock_data.csv")

# dropping unwanted columns
data.drop(['High','Low','Volume'],axis="columns",inplace=True)

# removing target data 
target = data['Open']
new_data = data

new_data.drop(['Open'],axis="columns",inplace=True)
print(data.head())

# creating x and y arrays
x = new_data.values
y = target.values


#plotting graphs
data["Close"].plot(figsize=(12, 6), title=f"{ticker} Closing Price")
plt.grid(True)
plt.show()

target.plot(figsize=(12, 6), title=f"{ticker} Opening Price")
plt.grid(True)
plt.show()

#spilitting data
x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)














