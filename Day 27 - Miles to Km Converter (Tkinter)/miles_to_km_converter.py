from tkinter import *
from tkinter.tix import COLUMN

window = Tk()
window.title("Miles to Km Converter!")
window.minsize(width=200, height=200)
window.config(padx= 20, pady= 20)

def convert():
    mile = float(miles_entry.get())
    km = round(mile*1.6, 1)
    convert_km.config(text= km)



miles_entry = Entry(width=10)
miles_entry.grid(row= 0, column= 1)

miles = Label(text="Miles")
miles.grid(row= 0, column= 2)

equals = Label(text="equals to")
equals.grid(row = 1, column=0)

convert_km = Label(text= 0)
convert_km.grid(row = 1, column= 1)

km = Label(text= "Km")
km.grid(row= 1, column= 2)

button = Button(text="Calculate", command=convert)
button.grid(row= 2, column= 1)


window.mainloop()