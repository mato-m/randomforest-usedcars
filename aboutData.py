import pandas
data = pandas.read_csv('cars.csv') # učitavanje dataseta

print(data.shape) # 852122 reda i 8 kolona

print(data.dtypes) # tipovi podataka
# Price, Year - integer
# Mileage - float
# City, State, Vin, Make, Model - string

print(data.isnull().sum()) # 0 null vrijednosti u svakom redu