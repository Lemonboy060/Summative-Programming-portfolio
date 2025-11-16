from tkinter import *

class factorial_frame():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(parent_frame, text = "Enter Number: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number's Factorial:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 122, y = 42)

        Button(parent_frame, text="Find Factorial", font = (20)).place(x = 175, y = 150)