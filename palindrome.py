from tkinter import *

class palindrome_frame():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)
        Label(self.parent_frame, text = f"Number of Palindrome Substring's:", bg = "light blue", font = (20), fg = "black").place(x=10, y=80)
        self.entry = Entry(parent_frame, width=50)
        self.entry.place(x = 142, y = 42)

        Button(parent_frame, text="Count Pailndromes", font = (20), command=self.count_palindromes_substrings).place(x = 175, y = 150)

    def count_palindromes_substrings(self):
        user_string = self.entry.get()
        memory = {}

        def is_Palindrome(left, right):
            if(left, right) in memory:
                return memory[(left, right)]
            
            if left == right:
                memory[(left, right)] = True
                return True
            
            if left + 1 == right:
                memory[(left, right)] = (user_string[left] == user_string[right])
                return memory[(left, right)]

            if user_string[left] == user_string[right] and is_Palindrome(left+1, right-1):
                memory[(left, right)] = True
            elif user_string[left] != user_string[right] and is_Palindrome(left+1, right-1) == False:
                memory[(left,right)] = False
            else:
                memory[(left, right)] = False
            
            return memory[(left, right)]
        
        p_count = 0
        for letter in range(len(user_string)):
            for letter2 in range(letter, len(user_string)):
                if is_Palindrome(letter, letter2):
                    p_count +=1 

        Label(self.parent_frame, text = p_count, bg = "light blue", font = (20), fg = "black").place(x=260, y=80)
    
        