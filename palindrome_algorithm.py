from tkinter import *

class palindrome():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the palindrome class user interface

        Creates Labels and entry boxes, to allow user to enter palindrome for counting as
        well as creating button to start count_palindromes_substrings function

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 

        Returns:
        None 
        """

        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number of Palindrome Substring's:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Count Pailndromes", font = (20), command=self.count_palindromes_substrings).place(x = 175, y = 165)

    def count_palindromes_substrings(self):
        """
        Counts the palindrome substrings in the string entered by the user
        and displays the result in the the user inteface 

        Args:
        None

        Returns:
        None
        """

        self.user_string = self.entry.get()
        palindrome_count = 0
        self.memory = {}

        for letter in range(len(self.user_string)):
            for letter2 in range(letter, len(self.user_string)):
                if self.is_Palindrome(letter, letter2):
                    palindrome_count +=1 

        Label(self.parent_frame, text = palindrome_count, bg = "light blue", font = (20), fg = "black").place(x=260, y=80)

    def is_Palindrome(self, left, right):
            """
            Docstring for is_Palindrome
            
            Args:
            left (int):
            right (int): 

            Return:

            """
            if(left, right) in self.memory:
                return self.memory[(left, right)]
            
            elif left == right:
                self.memory[(left, right)] = True
                return True
            
            elif left + 1 == right:
                self.memory[(left, right)] = (self.user_string[left] == self.user_string[right])
                return self.memory[(left, right)]

            elif self.user_string[left] == self.user_string[right] and self.is_Palindrome(left+1, right-1):
                self.memory[(left, right)] = True
            else:
                self.memory[(left, right)] = False
            
            return self.memory[(left, right)]