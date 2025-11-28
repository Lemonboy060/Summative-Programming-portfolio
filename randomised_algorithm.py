from tkinter import *

class randomised():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.deck_box = Text(self.parent_frame, width=90, height=5)
        self.deck_box.place(x = 10, y = 35)

        Button(self.parent_frame, text ="Output Cards", font = (20), command=self.create_deck).place(x = 175, y = 150)
        Button(self.parent_frame, text="Shuffle Cards", font = (20)).place(x = 295, y = 150)
    
    def create_deck(self):
        deck = []
        suits = ["♥", "♦", "♣", "♠"]
        cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

        for suit in suits:
            for card in cards:
                deck.append(f"{card}, {suit}")
        self.deck_box.insert(END, deck)
        print() 
    
    def shuffle_deck():
        print()