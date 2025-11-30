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
        fibonacci_number_storage = [0, 1]
        for length in range(int(nth_number)-2):
            next = fibonacci_number_storage[length-1] + fibonacci_number_storage[length-2]
            fibonacci_number_storage.append(next)
        i = 0
        for element in fibonacci_number_storage:
            fibonacci_number_storage[i] = int(fibonacci_number_storage[i])
            i += 1
        Label(self.parent_frame, text = fibonacci_number_storage[nth_number], bg = "light blue", font = (20), fg = "black").place(x=290, y= 80)
