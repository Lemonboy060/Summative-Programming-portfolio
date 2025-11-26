from tkinter import *
from tkinter import messagebox

class factorial():
    def __init__(self, parent_frame): # Creates "Enter Number:" and "Number's Factorial:" Labels for the Factorial frame, factorials entry bar and the button to start the recursive_factorial function alos created
        self.parent_frame = parent_frame # Saves the parent_frame parameter into a self. variable, allowing to be accessed throughout the class in various Tkinter modules
        Label(self.parent_frame, text = "Enter Number: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number's Factorial:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 122, y = 42)
    
        Button(self.parent_frame, text="Find Factorial", font = (20), command=self.recursive_factorial).place(x = 175, y = 150)

    def recursive_factorial(self):
        text_box_entry = self.entry.get() # Retrieves the inputted the user inputted which was stored in entry
        if text_box_entry.isdigit() == False: # The .isdigit() function is used to check whether the inputted string is a whole number and not text or any other number like negatives, if it is then a error message pops up
            messagebox.showerror("Error", "Please enter a valid whole number.")
            return
        
        factorial_number = int(text_box_entry) # Converts text_box_entry string into an integer, which is stored as factorial_number
        total = self.calc_factorial(factorial_number)

        Label(self.parent_frame, text = total, bg = "light blue", font = (20), fg = "black").place(x= 160, y=80)

            
    def calc_factorial(self, mult_number): # Function uses mult_number parameter which is the orginal number the user inputted (factorial_number variable)
        if mult_number == 0 or mult_number == 1: # Checks if the number inputted was 0 or 1 as both would return 1
            return 1
        else: # Then chain of multiplcation starts, where the original number is repeatedly multipled by itself-1 as the function begins calling itself with the inputted_number-1, so 5*4*3*2*1
            return mult_number * self.calc_factorial(mult_number-1)


