import tkinter as tk
from tkinter import ttk
#from tkinter.ttk import *

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Converter")
#window.iconbitmap("icon.ico")
window.attributes("-alpha", 0.5)

p1 = tk.PhotoImage(file = "icon.png")
window.iconphoto(False, p1)

# menu
menu = tk.Menu(window)
# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="Close", command=window.destroy)
menu.add_cascade(label="File", menu=file_menu)
window.configure(menu = menu)

# style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black",
                background="red")
# label to km
label_km = ttk.Label(text=" Insert Km :", style="BW.TLabel")
label_km.pack()
# entry fild ...........
entry_fild = ttk.Entry(window,
                       background="red")
entry_fild.pack()
# close button
close_btn = ttk.Button(window, text="Close", command=window.destroy)
close_btn.pack()

# run
window.mainloop()
