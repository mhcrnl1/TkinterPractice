from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

user_input = Entry(width=10, font=("Times New Roman", 13, "bold"))
user_input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Times New Roman", 13, "bold"))
miles.grid(column=2, row=0)

is_eq_to = Label(text="is equal to", font=("Times New Roman", 13, "bold"))
is_eq_to.grid(column=0, row=1)

converted_val = Label(text=0, font=("Times New Roman", 13, "bold"))
converted_val.grid(column=1, row=1)

km = Label(text="Km", font=("Times New Roman", 13, "bold"))
km.grid(column=2, row=1)


def converter():
    converted_val.config(text=int(user_input.get()) * 1.60934)


button = Button(text="Calculate", command=converter, font=("Times New Roman", 13, "bold"))
button.grid(column=1, row=2)

window.mainloop()
