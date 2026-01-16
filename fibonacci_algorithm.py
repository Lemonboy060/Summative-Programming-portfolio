from tkinter import *
from tkinter import messagebox

class fibonacci():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the fibonacci class user interface

        Creates Labels and Entry boxes, to allow user to enter a integer 
        Also a button to call the fibpnacci_creator function

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 

        Returns:
        None 
        """
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter number:", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number at Nth in Fibonacci's sequence:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Find Nth Number", font = (20), command=self.fibonacci_creator).place(x = 175, y = 165)
    
    def fibonacci_creator(self):
        """
        Gets the number the user entered and checks if its a valid input

        Assigns first_value and second_value as 0 and 1, as they are always
        the first two values in the fibonacci sequence
        
        Then will repeatedly reassign the first value as second value, and then
        reassign the second value as the sum of both, until it reaches then inputted number
        """
        nth_number = self.entry.get()
        if nth_number == "" or nth_number.isdigit() == False:
            messagebox.showerror("Error", "Please input valid number")
            return
        first_value, second_value = 0, 1
        for length in range(int(nth_number)-2):
            first_value, second_value = second_value, first_value + second_value
        Label(self.parent_frame, text = second_value, bg = "light blue", font = (20), fg = "black").place(x=300, y= 80)
