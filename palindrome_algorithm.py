from tkinter import *

class palindrome():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the palindrome class user interface

        Creates Labels and entry boxes, to allow user to enter palindrome for counting as
        well as creating button to start count_palindromes_substrings function

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 
        """

        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number of Palindrome Substring's:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Count Pailndromes", font = (20), command=self.count_palindromes_substrings).place(x = 175, y = 165)

    def count_palindromes_substrings(self):
        """
        Counts the palindrome substrings in the string entered by the user by 
        calling is_palindrome function to check if parts of the string are palindromes 
        and displays the result in the the user inteface 
        """

        self.user_string = self.entry.get()
        palindrome_count = 0
        self.memory = {}

        for i_index in range(len(self.user_string)):
            for j_index in range(i_index, len(self.user_string)):
                if self.is_Palindrome(i_index, j_index):
                    palindrome_count +=1 

        Label(self.parent_frame, text = palindrome_count, bg = "light blue", font = (20), fg = "black").place(x=260, y=80)

    def is_Palindrome(self, left, right):
            """
            Checks whether a certain part of the string entered by the user is a palindrome

            Uses memorisation in memory dictionary to ensure each substring is checked once 
            and not numerous times
            
            Args:
            left (int): First index of the substring
            right (int): Last index of the substring

            Return:
            self.memory[(left, right)] (bool): Represents whether a specific substring is a plaindrome or not
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