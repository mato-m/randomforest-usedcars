from tkinter import *
from tkinter import ttk,messagebox
import pandas
import predict




root = Tk()
root.resizable(False,False)
root.title("Predikcija")
frm = ttk.Frame(root, padding=10)
frm.grid()

yearEntry = IntVar()
mileageEntry = IntVar()

carModelEntry = StringVar()
data = pandas.read_csv('cars.csv')
data=data.sample(20)
data= data.sort_values('Model')
carModels = data['Model'].unique()

ttk.Label(frm, text="Godište").grid(column=0, row=0)
ttk.Entry(frm, textvariable=yearEntry).grid(column=1,row=0)
ttk.Label(frm, text="Kilometraža").grid(column=0, row=1)
ttk.Entry(frm, textvariable=mileageEntry).grid(column=1,row=1)
ttk.Label(frm, text="Model").grid(column=0, row=2)
ttk.OptionMenu(frm,carModelEntry,"Izaberite model",*carModels).grid(column=1,row=2)

def callback_error(self, *args):
    messagebox.showerror('Error', 'Greška, pokušajte ponovo!')

Tk.report_callback_exception = callback_error
def btnPredict():
    year = yearEntry.get()
    mileage = mileageEntry.get()
    carModel = carModelEntry.get()
    if(year<1996 or year >2022):
            messagebox.showerror("Greška", "Godište mora biti između 1996. i 2022.")
            return
    if mileage<0:
            messagebox.showerror("Greška", "Kilometraža mora biti pozitivan cijeli broj")
            return
    if carModel=='Izaberite model':
        messagebox.showerror("Greška", "Niste izabrali model automobila")
        return
    result = str(round(predict.predictPrice(year,mileage,carModel),2))
    messagebox.showinfo("Rezultat","Predviđena cijena za ovaj automobil je : " + result+"$")


ttk.Button(frm, text="Predvidi", command=btnPredict).grid(column=0,columnspan=2, row=3)
root.mainloop()