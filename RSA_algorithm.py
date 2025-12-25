from tkinter import *

class RSA():
    def __init__(self, parent_frame):     
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number of Palindrome Substring's:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Count Pailndromes", font = (20)).place(x = 175, y = 165)