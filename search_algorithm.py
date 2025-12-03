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
        user_array = []
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')

        if user_array_inputs == "":
            messagebox.showerror("Error", "Please enter a valid array of integers")
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
        smallest_value = array[0]
        for value in array:
            if value < smallest_value:
                smallest_value = value
        return smallest_value
    
    def largest_value(self, array):
        largest_value = array[0]
        for value in array:
            if value > largest_value:
                largest_value = value
        return largest_value

    def mode_of_array(self, array):
        frequency_dictionary = {}
        most_freq = 0
        for value in array:
            if value != frequency_dictionary:
                frequency_dictionary[value] = 1
            else:
                frequency_dictionary[value] += 1
        for value_freq in frequency_dictionary:
            if frequency_dictionary[value_freq] > most_freq:
                most_freq = frequency_dictionary[value_freq]
                mode = value_freq
        return mode

    def median_of_array(self, array):
        sorted_array = sorting.bubble_sort(self, array)
        middle_of_array = (len(sorted_array) // 2)
        if len(sorted_array) % 2 == 0:
            median = (sorted_array[middle_of_array-1] + sorted_array[middle_of_array]) / 2
        else:
            median = sorted_array[middle_of_array]
        return median

    def IQF(self, array):
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