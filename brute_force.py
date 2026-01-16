from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class merge():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the merge class user interface

        Creates Labels and entry boxes, to allow user to enter array of elements
        to be sorted with merge sort

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 
        """

        self.parent_frame = parent_frame
        self.sort_order = False
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
        """

        user_array = []
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')

        if user_array_inputs == "":
            messagebox.showerror("Error", "Please enter a valid array of integers")
            return

        for strings in user_array_str:
            user_array.append(int(strings))

        if self.sorting_order_dropbox.get() == "Descending":
            self.sort_order = True

        sorted_array = self.merge_sort(user_array)
        
        Label(self.parent_frame, text = f"Sorted Array: {sorted_array}", bg = "light blue", font = (20), fg = "black").place(x=10, y = 100)

    def merge_sort(self, array):
        """
        The function sorts an unsorted array
        
        it finds the middle of the array to be sorted and splits it into two arrays, 
        being the left and right array

        If values overlap between the left and right arrays they are check and moved
        
        The left and right arrays are then recurisvely called to split the array down to
        one element

        Args:
        array (list[int]): Users given array to sort

        Returns:
        sorted_array (list[int]): Users now sorted array
        """

        array_length = len(array)
        middle_of_array = array_length // 2

        if array_length <= 1:
            return array

        left_array = array[0:middle_of_array]
        right_array = array[middle_of_array:]
       
        left_array = self.merge_sort(left_array)
        right_array = self.merge_sort(right_array)

        if self.sort_order == True:
            sorted_array = self.merge_arrays_reverse(left_array, right_array)
        else:
            sorted_array = self.merge_arrays(left_array, right_array)

        return sorted_array
        
    def merge_arrays(self, left_array, right_array):
        """
        Merges all the arrays, by comparing various indexes of the array to check whether 
        values are higher or lower

        Args:
        left_array (list[int]): left hand side of the array once split
        right_array (list[int]): right hand side of the array once split

        Returns:
        sorted_array(list[int]): All arrays combined into one, in ascending order
        """
        left_array_length = len(left_array)
        right_array_length = len(right_array)
        sorted_array = []
        L_array_index = 0 
        r_array_index = 0

        while L_array_index < left_array_length and r_array_index < right_array_length:
            if left_array[L_array_index] <= right_array[r_array_index]:
                sorted_array.append(left_array[L_array_index])
                L_array_index += 1
            else:
                sorted_array.append(right_array[r_array_index])
                r_array_index += 1

        while(L_array_index < left_array_length):
            sorted_array.append(left_array[L_array_index])
            L_array_index += 1

        while(r_array_index < right_array_length):
            sorted_array.append(right_array[r_array_index])
            r_array_index += 1

        return sorted_array
    
    def merge_arrays_reverse(self, left_array, right_array):
        """
        Merges all the arrays, by comparing various indexes of the array to check whether 
        values are higher or lower, this owever check if the left array value is larger then 
        the right array, which puts the sorted array in descending order

        Args:
        left_array (list[int]): left hand side of the array once split
        right_array (list[int]): right hand side of the array once split

        Returns:
        sorted_array(list[int]): All arrays combined into one, in descending order
        """
        left_array_length = len(left_array)
        right_array_length = len(right_array)
        sorted_array = []
        L_array_index = 0 
        r_array_index = 0

        while L_array_index < left_array_length and r_array_index < right_array_length:
            if left_array[L_array_index] >= right_array[r_array_index]:
                sorted_array.append(left_array[L_array_index])
                L_array_index += 1
            else:
                sorted_array.append(right_array[r_array_index])
                r_array_index += 1

        while(L_array_index < left_array_length):
            sorted_array.append(left_array[L_array_index])
            L_array_index += 1

        while(r_array_index < right_array_length):
            sorted_array.append(right_array[r_array_index])
            r_array_index += 1

        return sorted_array
        


    