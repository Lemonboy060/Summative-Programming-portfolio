from tkinter import *
from random import *
from tkinter import messagebox

class randomised():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the randomised class user interface

        Creates Labels, buttons and a text box, so the randomised deck may be outputted to the 
        user

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 
        """

        self.parent_frame = parent_frame
        self.deck_created = False
        self.deck_box = Text(self.parent_frame, width=65, height=5)
        self.deck_box.place(x = 10, y = 35)
        self.deck_box.config(state = "disabled")

        Button(self.parent_frame, text ="Output Cards", font = (20), command=self.create_deck).place(x = 175, y = 165)
        Button(self.parent_frame, text="Shuffle Cards", font = (20), command=self.shuffle_deck).place(x = 295, y = 165)
    
    def create_deck(self):
        """
        deck is created so it may be randomised later
        
        All suits and card values are interated through, so one of each may be generated
        """
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
        self.deck_created = True
        self.deck_box.config(state = "disabled")
    
    def shuffle_deck(self):
        """
        Simple function used to shuffle the deck of cards once the deck has been generated

        The shuffle works by using the fisher yates shuffle, which will just swap two 
        elements in the deck array, to make the shuffle truely random, the cards are swapped at least
        52 times with each other, using random numbers to swap random cards

        all cards in the deck are then appended to deck box, in order to be presented to the user
        """
        if self.deck_created == False:
            messagebox.showerror("Error", "Please output deck before shuffling")
            return
        self.deck_box.config(state = "normal")
        self.deck_box.delete("1.0", END)

        for number in range(len(self.deck)):
            random_element = randint(0, number+1)
            self.deck[number],self.deck[random_element] = self.deck[random_element], self.deck[number]
        for card in self.deck:
            self.deck_box.insert(END, card)
        self.deck_box.config(state = "disabled")
        
