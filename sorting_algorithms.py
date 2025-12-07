from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class sorting():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter array of numbers to sort, Seperated by commas: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=40)
        self.entry.place(x = 400, y = 29)

        sorting_order = ["Ascending", "Descending"]
        sorting_type = ["Selection", "Bubble"]
        self.sorting_order_dropbox = ttk.Combobox(self.parent_frame, values=sorting_order)
        self.sorting_type_dropbox = ttk.Combobox(self.parent_frame, values=sorting_type, width= 25)

        self.sorting_order_dropbox.set("Select Order:")
        self.sorting_order_dropbox.place(x=10, y=55)
        self.sorting_type_dropbox.set("Select Sorting Algorithm:")
        self.sorting_type_dropbox.place(x=160, y=55)

        Button(self.parent_frame, text ="Sort Values", font = (20), command=self.sorting_function).place(x = 175, y = 150)

    def sorting_function(self):
        user_array = []
        chosen_sort = self.sorting_type_dropbox.get()
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')

        if user_array_inputs == "":
            messagebox.showerror("Error", "Please enter a valid array of integers")
            return

        for strings in user_array_str:
            user_array.append(int(strings))

        if chosen_sort == "Bubble":
            sorted_array = self.bubble_sort(user_array)
        elif chosen_sort == "Selection":
            sorted_array = self.selection_order(user_array)
        else:
            sorted_array = self.bubble_sort(user_array)

        if self.sorting_order_dropbox.get() == "Descending":
            sorted_array = self.reverse_array(sorted_array)

        Label(self.parent_frame, text = f"Sorted Array: {sorted_array}", bg = "light blue", font = (20), fg = "black").place(x=10, y = 100)

    def bubble_sort(self, array):
        for values in range(len(array)-1):
            for elements in range(len(array)-1):
                if array[elements+1] < array[elements]:
                    array[elements], array[elements+1] = array[elements+1], array[elements]
        return array

    def selection_order(self, array):
        values=1
        for values in range(len(array)):
            temp = array[values]
            comparison_value = values-1

            for elements in range(len(array)):
                if comparison_value >= 0 and array[comparison_value] > temp:
                    array[comparison_value+1] = array[comparison_value]
                    comparison_value -= 1               
            
            array[comparison_value+1] = temp
        return array
    
    def reverse_array(self, array):
        for values in range(len(array)):
            for elements in range(len(array)-1):
                if array[elements+1] > array[elements]:
                    array[elements], array[elements+1] = array[elements+1], array[elements]
        return array