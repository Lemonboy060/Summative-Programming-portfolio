from tkinter import *

class fibonacci():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter number:", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number at Nth in Fibonacci's sequence:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Find Nth Number", font = (20), command=self.fibonacci_creator).place(x = 175, y = 150)
    
    def fibonacci_creator(self):
        nth_number = self.entry.get()
        first_value, second_value = 0, 1
        for length in range(int(nth_number)-2):
            first_value, second_value = second_value, first_value + second_value
        Label(self.parent_frame, text = second_value, bg = "light blue", font = (20), fg = "black").place(x=300, y= 80)
