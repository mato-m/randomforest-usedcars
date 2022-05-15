# Import paketa
import pandas
from sklearn import preprocessing

# Ucitavanje dataseta
data = pandas.read_csv('cars.csv')
data = data.loc[data['Price']<=30000]
data = data.loc[data['Mileage']<=30000]
data = data.loc[data['Year']>=2010]
data.to_csv('cars.csv',index=False)

# Uklanjanje nepotrebnih kolona
data = data.drop(columns=['Make','Vin','State','City'])


# Pretvaranje string kolone u brojeve
leCarModel = preprocessing.LabelEncoder()
data['Model']=leCarModel.fit_transform(data['Model'])

# Cuvanje obradjenog dataseta u csv formatu
data.to_csv('data.csv',index=False)