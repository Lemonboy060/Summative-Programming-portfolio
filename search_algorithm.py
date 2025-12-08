from tkinter import *
from tkinter import messagebox
from sorting_algorithms import sorting

class search():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter array of numbers to analyse, Seperated by commas: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=40)
        self.entry.place(x = 420 , y = 29)

        self.statistic_box = Text(self.parent_frame, width=65, height=6)
        self.statistic_box.place(x = 10, y = 55)
        self.statistic_box.config(state = "disabled")

        Button(self.parent_frame, text = "Analyse Array", font = (20), command=self.analyse_statistics).place(x = 175, y = 165)

    def analyse_statistics(self):
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
        Docstring for smallest_value
        
        :param self: Description
        :param array: Description
        """

        smallest_value = array[0]
        for value in array:
            if value < smallest_value:
                smallest_value = value
        return smallest_value
    
    def largest_value(self, array):
        """
        Docstring for largest_value
        
        :param self: Description
        :param array: Description
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
        mode (int): The most common value in the array
        """

        frequency_dictionary = {}
        most_freq = 0
        mode = None
        for value in array:
            if value not in frequency_dictionary:
                frequency_dictionary[value] = 1
            else:
                frequency_dictionary[value] += 1
        for value_freq in frequency_dictionary:
            if frequency_dictionary[value_freq] > most_freq:
                most_freq = frequency_dictionary[value_freq]
                mode = value_freq
        return mode

    def median_of_array(self, array):
        """
        Finds the median of an unordered array, calls bubble sort
        from the sorting class to order the array
        
        Args:
        array (list[int]): An unsorted array of user inputs

        Returns:
        median (int): The centre of the orgianlly unordered array
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