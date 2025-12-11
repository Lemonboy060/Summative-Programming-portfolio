from tkinter import *
from palindrome_algorithm import palindrome
from factorial_algorithm import factorial
from fibonacci_algorithm import fibonacci
from randomised_algorithm import randomised
from sorting_algorithms import sorting
from search_algorithm import search
from brute_force import merge
from RSA_algorithm import RSA

class Algorithm_factory:
    def __init__(self):
        self.frames_dict = {"Search": lambda frame: search(frame),
                            "Sorting": lambda frame: sorting(frame),
                            "RSA": lambda frame: RSA(frame),
                            "Factorial": lambda frame: factorial(frame),
                            "Randomised": lambda frame: randomised(frame),
                            "Brute force": lambda frame: merge(frame),
                            "Fibonacci": lambda frame: fibonacci(frame),
                            "Palindrome": lambda frame: palindrome(frame)
                            }
    
    def call_frame(self, algorithm_name, frame):
        function = self.frames_dict.get(algorithm_name)
        function(frame)
