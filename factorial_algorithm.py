from tkinter import *
from tkinter import messagebox

class factorial():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the factorial class user interface

        Creates Labels and Entry boxes, to allow user to enter a integer 
        Also a button to call the recursive_factorial function

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 

        Returns:
        None 
        """
        self.parent_frame = parent_frame 
        Label(self.parent_frame, text = "Enter Number: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number's Factorial:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 122, y = 42)
    
        Button(self.parent_frame, text="Find Factorial", font = (20), command=self.recursive_factorial).place(x = 175, y = 150)

    def recursive_factorial(self):
        """
        Intially used to get and assign the user's entered integer

        The integer is then checked if its a valid input, using .isdigit
        As it checks if the value is positive and a integer
            - If the input is not valid, a error message will pop up

        calc_factorial is then called and assigned to total, which will
        then be displayed in a Label

        Args:
        None 

        Returns:
        None 
        """
        text_box_entry = self.entry.get() 
        if text_box_entry.isdigit() == False: 
            messagebox.showerror("Error", "Please enter a valid whole number.")
            return
        
        factorial_number = int(text_box_entry)
        total = self.calc_factorial(factorial_number)

        Label(self.parent_frame, text = total, bg = "light blue", font = (20), fg = "black").place(x= 160, y=80)

            
    def calc_factorial(self, mult_number):
        """
        Recursive function which is called repeatedly to calculate the factorial of 
        the user chosen integer

        The integer is also checked whether its a 1 or 0 as both would return a 
        factorial of 1
        
        Args:
        mult_number (int): The integer entered by the user, which will be multiplied numerous times
        
        Returns:
        mult_number (int) * self.calc_factorial(mult_number-1): Recursively multiples mult_number
        by itself minus one until 0 or 1 is reached
        """
         
        if mult_number == 0 or mult_number == 1: 
            return 1
        else: 
            return mult_number * self.calc_factorial(mult_number-1)


