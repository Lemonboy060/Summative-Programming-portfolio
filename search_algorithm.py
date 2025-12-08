from tkinter import *
from tkinter import messagebox
from sorting_algorithms import sorting

class search():
    def __init__(self, parent_frame):
        """
        Creates all necessary widgets for the search class user interface

        Creates Labels and entry boxes, to allow user to enter array
        and creates text box for statictics of the array to be placed in

        Args:
        parent_frame (tkinter.Frame): The class's frame, which will contain all the relevant widgets 

        Returns:
        None 
        """

        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter array of numbers to analyse, Seperated by commas: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=40)
        self.entry.place(x = 420 , y = 29)

        self.statistic_box = Text(self.parent_frame, width=65, height=6)
        self.statistic_box.place(x = 10, y = 55)
        self.statistic_box.config(state = "disabled")

        Button(self.parent_frame, text = "Analyse Array", font = (20), command=self.analyse_statistics).place(x = 175, y = 165)

    def analyse_statistics(self):
        """
        Intially used to split user's input into a valid array of integers

        Then used to call all relevant functions to find the smallest and largest
        value, mode, median first IQF and third IQF

        all relevant variables are then inserted into statistic_box text box

        Args:
        None

        Returns:
        None     
        """

        self.statistic_box.config(state = "normal")
        self.statistic_box.delete("1.0", END)
        user_array = []
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')

        if user_array_inputs == "":
            messagebox.showerror("Error", "Please input valid number")
            return
        
        for strings in user_array_str:
            user_array.append(int(strings))

        smallest_value = self.smallest_value(user_array)
        largest_value = self.largest_value(user_array)
        mode = self.mode_of_array(user_array)
        median = self.median_of_array(user_array)
        first_IQF, Third_IQF = self.IQF(user_array)

        self.statistic_box.insert(END, f"Smallest Value: {smallest_value}\n")
        self.statistic_box.insert(END, f"Largest Value: {largest_value}\n")
        self.statistic_box.insert(END, f"Mode: {mode}\n")
        self.statistic_box.insert(END, f"Median: {median}\n")
        self.statistic_box.insert(END, f"First IQF: {first_IQF}\n")
        self.statistic_box.insert(END, f"Thrid IQF: {Third_IQF}\n")

        self.statistic_box.config(state = "disabled")

    def smallest_value(self, array):
        """
        Finds the smallest given value in an unordered array
        
        Args:
        array (list[int]): An unsorted array of user inputs

        Returns:
        smallest_value (int): lowest value in the array
        """

        smallest_value = array[0]

        for value in array:
            if value < smallest_value:
                smallest_value = value

        return smallest_value
    
    def largest_value(self, array):
        """
        Finds the largest given value in an unordered array
        
        Args:
        array (list[int]): An unsorted array of user inputs

        Returns:
        largest_value (int): Highest value in the array
        """

        largest_value = array[0]

        for value in array:
            if value > largest_value:
                largest_value = value

        return largest_value

    def mode_of_array(self, array):
        """
        Finds the mode of an unordered array

        Args:
        array (list[int]): An unsorted array of user inputs

        Returns: 
        mode_list (list[int]): The most common value in the array
            - If there is one frequent value, that one value will be returned in the list
            - If there is multiple values with the same frequency, they will all be returned in the list
            - If there is no frequent value, "No Mode" will be returned

        """
        frequency_dictionary = {}
        most_freq = 0
        mode_list = []

        for value in array:
            if value not in frequency_dictionary:
                frequency_dictionary[value] = 1
            else:
                frequency_dictionary[value] += 1

        for value_freq in frequency_dictionary:
            if frequency_dictionary[value_freq] > most_freq:
                most_freq = frequency_dictionary[value_freq]

        if most_freq == 1:
            return "No Mode"
        
        for element in frequency_dictionary:
            if frequency_dictionary[element] == most_freq:
                mode_list.append(element)

        return mode_list

    def median_of_array(self, array):
        """
        Finds the median of an orginally unordered array, calls bubble sort
        from the sorting class to order the array, as the median cannot
        be found in a unordered array
        
        Args:
        array (list[int]): An unsorted array of user inputs

        Returns:
        median (int): The centre of the originally unordered array
        """

        sorted_array = sorting.bubble_sort(self, array)
        middle_of_array = (len(sorted_array) // 2)

        if len(sorted_array) % 2 == 0:
            median = (sorted_array[middle_of_array-1] + sorted_array[middle_of_array]) / 2
        else:
            median = sorted_array[middle_of_array]

        return median

    def IQF(self, array:list[int]) -> int: 
        """
        IQF (Interquartile function), finds the first and thrid quartile
        of an unordered array
        
        Args:
        array (list[int]): An unsorted array of user inputs

        Returns:
        IQF1 (int): The median of the lower half of the originally unordered array
        IQF3 (int): The median of the upper half of the originally unordered array
        """

        sorted_array = sorting.bubble_sort(self, array)
        middle_of_array = (len(sorted_array) // 2)

        if len(sorted_array) % 2 == 0:
            lower_half_array = sorted_array[0:middle_of_array]
            upper_half_array = sorted_array[middle_of_array:]
        else:
            lower_half_array = sorted_array[0:middle_of_array]
            upper_half_array = sorted_array[middle_of_array+1:]

        IQF1 = self.median_of_array(lower_half_array)
        IQF3 = self.median_of_array(upper_half_array)

        return IQF1, IQF3