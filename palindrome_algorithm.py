from tkinter import *

class palindrome():
    def __init__(self, parent_frame):     
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number of Palindrome Substring's:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=35)
        self.entry.place(x = 142, y = 42)

        Button(self.parent_frame, text="Count Pailndromes", font = (20), command=self.count_palindromes_substrings).place(x = 175, y = 165)

    def count_palindromes_substrings(self):
        user_string = self.entry.get()
        palindrome_count = 0
        memory = {}

        def is_Palindrome(left, right):
            if(left, right) in memory:
                return memory[(left, right)]
            
            elif left == right:
                memory[(left, right)] = True
                return True
            
            elif left + 1 == right:
                memory[(left, right)] = (user_string[left] == user_string[right])
                return memory[(left, right)]

            elif user_string[left] == user_string[right] and is_Palindrome(left+1, right-1):
                memory[(left, right)] = True
            else:
                memory[(left, right)] = False
            
            return memory[(left, right)]
        
        for letter in range(len(user_string)):
            for letter2 in range(letter, len(user_string)):
                if is_Palindrome(letter, letter2):
                    palindrome_count +=1 

        Label(self.parent_frame, text = palindrome_count, bg = "light blue", font = (20), fg = "black").place(x=260, y=80)