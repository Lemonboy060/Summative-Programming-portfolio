from tkinter import *

class randomised():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        deck_box = Text(self.parent_frame, width=60, height=3)
        deck_box.place(x = 10, y = 35)

        Button(self.parent_frame, text ="Output Cards", font = (20)).place(x = 175, y = 150)
        Button(self.parent_frame, text="Shuffle Cards", font = (20)).place(x = 295, y = 150)
    
    def create_deck():
        print()
    
    def shuffle_deck():
        print()