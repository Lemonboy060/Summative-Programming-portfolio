from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sorting_algorithms import sorting

class merge():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the merge class user interface

        Creates Labels and entry boxes, to allow user to enter array of elements
        to be sorted with merge sort

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
        self.sorting_order_dropbox = ttk.Combobox(self.parent_frame, values=sorting_order)

        self.sorting_order_dropbox.set("Select Order:")
        self.sorting_order_dropbox.place(x=10, y=55)

        Button(self.parent_frame, text ="Sort Values", font = (20), command=self.sorting_menu).place(x = 175, y = 165)

    def sorting_menu(self):
        """
        Intially used to split user's input into a valid array of integers

        Checks each of those values to ensure they are valid 

        Then calls merge_sort to sort array, and will then call reverse_array from
        the sorting_algorithms file to flip the array using a reverse bubble sort
        if the user selected for the array order to be descending
        
        Args:
        None

        Returns:
        None
        """
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
    
    def merge(self, array, left_array, right_array):
        """
        Docstring for merge
        
        :param self: Description
        :param array: Description
        :param left_array: Description
        :param right_array: Description
        """
        left_array_length = len(left_array)
        right_array_length = len(right_array)
        i_index = 0
        L_index = 0 
        r_index = 0

        while L_index < left_array_length and r_index < right_array_length:
            if left_array[L_index] < right_array[r_index]:
                array[i_index] = left_array[L_index]
                i_index += 1
                L_index += 1
            else:
                array[i_index] = right_array[r_index]
                i_index += 1
                r_index += 1

        while(L_index < left_array_length):
            array[i_index] = left_array[L_index]
            i_index += 1
            L_index += 1

        while(r_index < right_array_length):
            array[i_index] = right_array[r_index]
            i_index += 1
            r_index += 1

        return array

    def merge_sort(self, array):
        """
        Docstring for merge_sort
        
        :param self: Description
        :param array: Description
        """

        array_length = len(array)
        middle_of_array = array_length // 2

        if array_length <= 1:
            return array

        left_array = array[:middle_of_array]
        right_array = array[middle_of_array:]

        i_index = 0
        j_index = 0

        for i_index in range(i_index + 1, i_index < array_length):
            if i_index < middle_of_array:
                left_array[i_index] = array[i_index]
            else:
                right_array[i_index] = array[i_index]
                j_index += 1
        
        left_array = self.merge_sort(left_array)
        right_array = self.merge_sort(right_array)
        array = self.merge(array, left_array, right_array)
        return array
        
        
        


    