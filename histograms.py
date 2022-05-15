import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('cars.csv')

# Colors
plt.rcParams["figure.facecolor"] = "#1A1A1A"
plt.rcParams['axes.facecolor'] = '#1A1A1A'
plt.rcParams["xtick.color"] = "#FF87D7"
plt.rcParams["ytick.color"] = "#FF87D7"

# Histogram 1 - Price
data.hist('Price',bins=10,color='#FF87D7',ec='white')
plt.grid(False)

# Histogram 2 - Mileage
data.hist('Mileage',bins=10,color='#FF87D7',ec='white')
plt.grid(False)

# Histogram 3 - Year
data.hist('Year',bins=data['Year'].value_counts().index.to_list().__len__(),color='#FF87D7',ec='white')
plt.grid(False)

plt.show()