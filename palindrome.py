from tkinter import *

class palindrome_frame():
    def __init__(self, parent_frame):
        Label(parent_frame, text = "Enter Palindrome: ", bg = "light blue", font = (20), fg = "black").place(x=10, y=40)

        Label(parent_frame, text = f"Number of Palindrome Substrings: ", bg = "light blue", font = (20), fg = "black").place(x = 10, y = 80)

        self.entry = Entry(parent_frame)
        self.entry.place(x = 142, y = 42)

        Button(parent_frame, text="Count Pailndrome's", font = (20), command=lambda: self.count_palindromes()).place(x = 175, y = 150)

    def count_palindromes(self):
        print()
        