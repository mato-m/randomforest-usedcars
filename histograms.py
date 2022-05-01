import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('cars.csv')
data.hist('Price',bins=120)
data.hist('Mileage',bins=150)
data.hist('Year',bins=data['Year'].value_counts().index.to_list().__len__())
plt.show()