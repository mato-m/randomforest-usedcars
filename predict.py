import pickle
import pandas
from newData import leCarModel

def predictPrice(godiste=0,kilometraza=0,carModel=0):
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    carModel = leCarModel.transform([carModel])[0]
    niz = pandas.DataFrame([[
    godiste,
    kilometraza,
    carModel
    ]],columns=['Year','Mileage','Model'])
    return loaded_model.predict(niz)[0]