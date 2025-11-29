from tkinter import *
from random import *

class randomised():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.deck_box = Text(self.parent_frame, width=65, height=5)
        self.deck_box.place(x = 10, y = 35)
        self.deck_box.config(state = "disabled")

        Button(self.parent_frame, text ="Output Cards", font = (20), command=self.create_deck).place(x = 175, y = 150)
        Button(self.parent_frame, text="Shuffle Cards", font = (20), command=self.shuffle_deck).place(x = 295, y = 150)
    
    def create_deck(self):
        self.deck_box.config(state = "normal")
        self.deck_box.delete("1.0", END)
        self.deck = []
        suits = ["♥", "♦", "♣", "♠"]
        cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for card in cards:
                self.deck.append(f" {card}{suit} ")
        for card in self.deck:
            self.deck_box.insert(END, card)
        self.deck_box.config(state = "disabled")
    
    def shuffle_deck(self):
        self.deck_box.config(state = "normal")
        self.deck_box.delete("1.0", END)

        for number in range(len(self.deck)):
            random_element = randint(0, number+1)
            self.deck[number],self.deck[random_element] = self.deck[random_element], self.deck[number]
        for card in self.deck:
            self.deck_box.insert(END, card)
        self.deck_box.config(state = "disabled")
        
