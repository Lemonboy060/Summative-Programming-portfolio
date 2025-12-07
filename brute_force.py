from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sorting_algorithms import sorting

class merge():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter array of numbers to sort, Seperated by commas: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=40)
        self.entry.place(x = 400, y = 29)

        sorting_order = ["Ascending", "Descending"]
        self.sorting_order_dropbox = ttk.Combobox(self.parent_frame, values=sorting_order)

        self.sorting_order_dropbox.set("Select Order:")
        self.sorting_order_dropbox.place(x=10, y=55)

        Button(self.parent_frame, text ="Sort Values", font = (20)).place(x = 175, y = 150)

    def sorting_menu(self):
        user_array = []
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')

        if user_array_inputs == "":
            messagebox.showerror("Error", "Please enter a valid array of integers")
            return

        for strings in user_array_str:
            user_array.append(int(strings))

        sorted_array = self.merge_sort(user_array)

        if self.sorting_order_dropbox.get() == "Descending":
            sorted_array = sorting.reverse_array(self, sorted_array)
        
        Label(self.parent_frame, text = f"Sorted Array: {sorted_array}", bg = "light blue", font = (20), fg = "black").place(x=10, y = 100)

    def merge_sort(self, array):
        pass

    