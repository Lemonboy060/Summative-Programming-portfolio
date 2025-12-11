from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class sorting():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the sorting class user interface
        Labels and Entry boxes, to allow user to enter an array 
        Dropboxes, letting the user choose which sort and sorting order

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 

        Returns:
        None 
        """

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

        Button(self.parent_frame, text ="Sort Values", font = (20), command=self.sorting_menu).place(x = 175, y = 150)

    def sorting_menu(self):
        """
        Intially used to split user's input into a valid array of integers

        Checks each of those values to ensure they are valid 

        Then depending what sorting algorithm the user chose, bubble_sort
        or selection_sort will be called to sort the array

        If the user had chose for the sorted array to be displayed in descending
        order, reverse_array will be called

        New sorted array is displayed in a new Label

        Args:
        None

        Returns:
        None   
        """

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
            sorted_array = self.selection_sort(user_array)
        else:
            sorted_array = self.bubble_sort(user_array)

        if self.sorting_order_dropbox.get() == "Descending":
            sorted_array = self.reverse_array(sorted_array)

        Label(self.parent_frame, text = f"Sorted Array: {sorted_array}", bg = "light blue", font = (20), fg = "black").place(x=10, y = 100)

    def bubble_sort(self, array):
        """
        Sorts the users array of integers using bubble sort

        Repeatedly loops through the array, comparing adjacent numbers
        swapping them if the number ahead of the first number is smaller

        Args:
        array (list[int]): The users orginally unnsorted array of numbers

        Returns:
        array (list[int]): The users orginally unnsorted array of numbers, now sorted
        """

        for values in range(len(array)-1):
            for elements in range(len(array)-1):
                if array[elements+1] < array[elements]:
                    array[elements], array[elements+1] = array[elements+1], array[elements]
        return array

    def selection_sort(self, array):
        """
        Sorts the users array of integers using selection sort

        Repeatedly loops through the array, looking for the smallest value
        in the unsorted part of the array iteration, then swapping it with
        the first value of the unsorte part of the array

        Args:
        array (list[int]): The users originally unsorted array of numbers

        Returns:
        array (list[int]): The users originally unsorted array of numbers, now sorted
        """

        for i_index in range(len(array)):
            minimum = i_index
            for j_index in range(i_index +1, len(array)):
                if array[minimum] > array[j_index]:
                    minimum = j_index
            temp = array[i_index]
            array[i_index] = array[minimum]
            array[minimum] = temp
        return array
    
    def reverse_array(self, array):
        """
        Reverses the array, essentially putting the array in descending order

        Uses a reversed bubble sort, Repeatedly loops through the array, 
        comparing adjacent numbers swapping them if the number ahead of the 
        first number is larger

        Args:
        array (list[int]): Ordered array in acending order

        Returns:
        array (list[int]): A order array in descending order
        """

        for values in range(len(array)):
            for elements in range(len(array)-1):
                if array[elements+1] > array[elements]:
                    array[elements], array[elements+1] = array[elements+1], array[elements]
        return array