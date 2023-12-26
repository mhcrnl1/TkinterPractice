import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("My Tkinter Window")

# Set the window size
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!")

# Pack the label into the window
label.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
