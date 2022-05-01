# Import paketa
import pandas
from sklearn import preprocessing

# Ucitavanje dataseta
data = pandas.read_csv('cars.csv')

# Uklanjanje nepotrebnih kolona
data = data.drop(columns=['Make','Vin','State','City'])


# Pretvaranje string kolone u brojeve
leCarModel = preprocessing.LabelEncoder()
data['Model']=leCarModel.fit_transform(data['Model'])

# Cuvanje obradjenog dataseta u csv formatu
data.to_csv('data.csv',index=False)