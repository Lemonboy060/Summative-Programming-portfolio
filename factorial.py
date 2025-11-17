from tkinter import *
from tkinter import messagebox

class factorial_frame():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(parent_frame, text = "Enter Number: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number's Factorial:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 122, y = 42)
    
        Button(parent_frame, text="Find Factorial", font = (20), command=self.factorio).place(x = 175, y = 150)

    def factorio(self):
        text = self.entry.get()
        if text.isdigit() == False:
            messagebox.showerror("Error", "Please enter a valid whole number.")
            return
        
        factorial_number = int(text)
        counter = 0
        total = self.calc_factorial(factorial_number)

        Label(self.parent_frame, text = total, bg = "light blue", font = (20), fg = "black").place(x= 160, y=80)

            
    def calc_factorial(self, mult_number, counter):
        if counter == 0:
            total = mult_number
            counter+1
        if mult_number == 0 or mult_number == 1:
            return 1
        else:
            total = mult_number * total
            self.calc_factorial(mult_number, counter)


