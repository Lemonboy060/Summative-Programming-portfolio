from tkinter import *

class search():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        Label(self.parent_frame, text = "Enter array of numbers to analyse, Seperated by commas: ", bg = "light blue", font = (20), fg = "black").place(x=10, y = 25)
        self.entry = Entry(parent_frame, width=40)
        self.entry.place(x = 420 , y = 29)

        self.statistic_box = Text(self.parent_frame, width=65, height=5)
        self.statistic_box.place(x = 10, y = 55)
        self.statistic_box.config(state = "disabled")

        Button(self.parent_frame, text = "Analyse Array", font = (20), command=self.analyse_statistics).place(x = 175, y = 150)

    def analyse_statistics(self):
        user_array = []
        user_array_inputs = self.entry.get()
        user_array_str = user_array_inputs.split(',')
        
        for strings in user_array_str:
            user_array.append(int(strings))

        smallest_value = self.smallest_value(user_array)
        largest_value = self.largest_value(user_array)
        mode = self.mode_of_array(user_array)

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
        print()

    def IQF(self, array):
        print()