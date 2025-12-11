from tkinter import *
from palindrome_algorithm import palindrome
from factorial_algorithm import factorial
from fibonacci_algorithm import fibonacci
from randomised_algorithm import randomised
from sorting_algorithms import sorting
from search_algorithm import search
from brute_force import merge
from RSA_algorithm import RSA
"""
Imports all algorithm classes from their files
"""

class Algorithm_factory:
    """
    The algorithm_factory class, is an implementation of the factory method 
    design pattern, and is responsible for calling the various algorithm classes
    
    The design pattern provides an interface for creating objects, which in this 
    case is the different algorithms and their frames, where each algorithm has their 
    class mapped do it in a dictionary
    """
    def __init__(self):
        """
        Intialises the frames dictionary mapping each of the algorithms to their frames 
        and functions

        Args:
        None

        Returns:
        none
        """
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
        """
        Executes the user interface function, associated with each algorithm 
        
        Args:
        algorithm_name (str): The name of the algorithm chosen by the user
        frame (tkinter.Frame): The chosen frame which the current frames widgets will be placed

        Returns:
        None
        """
        function = self.frames_dict.get(algorithm_name)
        function(frame)
