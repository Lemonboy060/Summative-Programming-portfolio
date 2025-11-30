from tkinter import *
from tkinter import ttk

class sorting():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter sequence of numbers to sort: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 260, y = 29)

        sorting_order = ["Ascending", "Descending"]
        sorting_type = ["Selection", "Bubble"]
        sorting_order_dropbox = ttk.Combobox(self.parent_frame, values=sorting_order)
        sorting_type_dropbox = ttk.Combobox(self.parent_frame, values=sorting_type, width= 25)

        sorting_order_dropbox.set("Select Order:")
        sorting_order_dropbox.place(x=10, y=55)
        sorting_type_dropbox.set("Select Sorting Algorithm:")
        sorting_type_dropbox.place(x=160, y=55)


        Button(self.parent_frame, text ="Sort Values", font = (20)).place(x = 175, y = 150)