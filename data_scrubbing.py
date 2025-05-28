
import pandas as pd
 

data = pd.read_csv("AAPL.csv")

# dropping unwanted columns
data.drop(['Close'],axis="columns",inplace=True)

# removing target data 
target = data['Open'].copy()
new_data = data.copy()
new_data.drop(['Open','Date'],axis="columns", inplace=True)

# creating x and y arrays
x = new_data[:-1]
y = target.shift(-1)
y.dropna(inplace=True)
