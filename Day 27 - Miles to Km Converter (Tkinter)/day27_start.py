
import tkinter

def button_clicked():
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("My First GUI Program!")
window.minsize(width= 500, height= 300)

my_label = tkinter.Label(text= "I am a Label!", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

new_button = tkinter.Button(text="New???")
new_button.grid(row= 0, column= 2)




my_button = tkinter.Button(text= "Click me!", command= button_clicked)
my_button.grid(row= 1, column= 1)

input = tkinter.Entry(width=10)
input.grid(row= 3, column= 3)

window.mainloop()

