# Import paketa
import pickle
import pandas
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

# Ucitavanje dataseta
data = pandas.read_csv('data.csv')

# Inicijalizacija Random forest regresionog modela
model = RandomForestRegressor()

# Zavisne varijable
X = data[['Year','Mileage','Model']]

# Nezavisna varijabla
Y = data[['Price']]

# Postavljanje training i test setova
X_train, X_test,Y_train,Y_test  = train_test_split(X, Y, test_size = 0.2)

# Postavljanje trening setova u model
model.fit(X_train,Y_train.values.ravel())

# Cuvanje modela u vidu fajla
pickle.dump(model, open('finalized_model.sav', 'wb'))

# Predikcija testnih vrijednosti
Y_pred = model.predict(X_test)

# Score - 77.234%
print("Score : "+str(model.score(X_test,Y_test)))

# Mean squared error - 6184720.411
print("Mean squared error : "+str(mean_squared_error(Y_test,Y_pred)))

# Mean absolute error - 1830.085
print("Mean absolute error : "+str(mean_absolute_error(Y_test,Y_pred)))
