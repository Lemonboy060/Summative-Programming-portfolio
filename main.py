from tkinter import *
from tkinter import messagebox
from palindrome_algorithm import palindrome
from factorial_algorithm import factorial
from fibonacci_algorithm import fibonacci
from randomised_algorithm import randomised
from sorting_algorithms import sorting
from search_algorithm import search
from brute_force import merge
from RSA_algorithm import RSA


class interface:
    def __init__(self, root):
        """
        intialising function used to create the tkinter window using root 

        also intialises all the algorithm names, frame dictionary and all 
        the frames to go in the dictionary as well as all the buttons to traverse

        Args:
        root (Tk): Main Tkinter function used to create all tkinter widgets and frames
        """
        self.root = root
        self.mediator = mediator_pattern(self.root)
        self.all_algo = ["Search","Sorting","RSA","Factorial","Randomised","Brute force","Fibonacci","Palindrome"]
        self.frames_dict = {}

        self.root.title("Algorithm Interface")
        self.root.geometry("1200x800")

        self.create_intial_frame()
        self.create_button_widgets()
        for algos in self.all_algo:
            self.create_all_frames(algos)

        self.show_frame("Main menu")

    def show_frame(self, frame_name):
        """
        Core function which is used to show the current frame being accessed to the user
        Accesses the actual frame stored in the fram dictionary so it can be used

        Args:
        frame_name (string):The name of the current frame/function which is being accessed
        """

        frame = self.frames_dict[frame_name] 
        frame.tkraise()

    def create_intial_frame(self):
        """
        Creates the main menu frame, which all the buttons to navigate to other frames are
        stored within 
        
        Then the main menu frame and its name are stored in the frames dictionary to be
        accessed later
        """

        self.main_menu_frame = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.frames_dict["Main menu"] = self.main_menu_frame

    def create_all_frames(self, algorithm_name):
        """
        Intialises all the frames and adds them to the frame dictionary with their names
        so they may be accessed later 

        Then depending on what algorithm/frame is being accessed then the function can
        call that frames class
        
        Args:
        algorithm_name (string): Specific name of the algorithm/frame being created
        """
        self.frame = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frames_dict[algorithm_name] = self.frame

        factory = factory_superclass()
        factory.create_frame(algorithm_name, self.frame, self.mediator)

        Label(self.frame, text = f"{algorithm_name} Algorithm", bg = "light blue", font = (20), fg = "black").place(x = 10)
        Button(self.frame, text="Back to Main Menu", font = (20), command=lambda: self.show_frame("Main menu")).place(x = 10, y = 165)

    
    def create_button_widgets(self):
        """
        Creates all the button widgets for the mainmenu frame, allowing the user to traverese to
        different frames/classes

        new_algo is created in the button creation line in order to correctly assign each button the
        correct algorithm frame to show, otherwise all the buttons default to the palindrome frame
        """

        y_pos = 50
        Label(self.main_menu_frame, text = "Main menu - Select Algorithm", font = (20), bg = "light blue", fg = "black").place(x = 10)

        for algorithm in self.all_algo:
            new_button = Button(self.main_menu_frame, text = f"{algorithm} Algorithm", font = (20), command=lambda new_algo=algorithm: self.show_frame(new_algo))
            new_button.place(x = 10, y = y_pos)
            y_pos += 50

class factory_superclass():
    """
    The factory_superclass is part of the factory design pattern and is designed to 
    create/initialise all the required classes and objects that the program would require

    The factory class also incoprates both the composite and mediator patterns, where all
    the classes/frames are categorised and some are intialsed with the mediator, if certain
    functions are required
    """
    def create_frame(self, algorithm_name, frame, mediator):
        """
        creat_frame goes through all the possible frames that are avalible and intialises them

        They are also categorised as part of the comnposite pattern
        
        Args:
        algorithm_name (string): The specific name of the algorithm being intalised
        frame (Frame): The frame of the algorithm being intialised
        mediator (mediator_pattern): The mediator pattern
        """

        self.mediator = mediator

        sorting_algorithms = composite_grouping("sorting")
        calculating_algorithms = composite_grouping("Calculating")
        encryption_algorithms = composite_grouping("encryption")
        random_algorithms = composite_grouping("random")

        if algorithm_name == "Palindrome":
            palindrome(frame)
            calculating_algorithms.append(algorithm_name)
        elif algorithm_name == "Factorial":
            factorial(frame)
            calculating_algorithms.append(algorithm_name)
        elif algorithm_name == "Fibonacci":
            fibonacci(frame)
            calculating_algorithms.append(algorithm_name)
        elif algorithm_name == "Randomised":
            randomised(frame)
            random_algorithms.append(algorithm_name)
        elif algorithm_name == "Sorting":
            sorting(frame)
            sorting_algorithms.append(algorithm_name)
        elif algorithm_name == "Search":
            search(frame)
            sorting_algorithms.append(algorithm_name)
        elif algorithm_name == "Brute force":
            merge(frame)
            sorting_algorithms.append(algorithm_name)
        elif algorithm_name == "RSA":
            RSA(frame, self.mediator)
            encryption_algorithms.append(algorithm_name)
        else:
            messagebox.showerror("Error")

class composite_grouping():
    """
    The composite grouping class is part of the composite design pattern and categorises
    different algorithms to four types of algorithm: sorting, Calculating, encryption, 
    random
    """
    def __init__(self, category):
        self.category = category
        self.category_nodes = []

    def append(self,algorithm_name):
        """
        Adds a specific algorithm to their corresponging category
        
        Args:
        algorithm_name(string): name of the algorithm being added to a category
        """
        self.category_nodes.append(algorithm_name)

class mediator_pattern():
    """
    Part of the mediator design pattern and acts as a mediator for other classes to 
    perform specific functions,  which for this class is to desiable or enable specific 
    buttons in other classes
    """
    def __init__(self, root):
        self.root = root
        self.buttons = {}
    
    def add_buttons(self, button_name, tkinter_button):
        """
        Registers specific buttons to the buttons list so they may be enabled or disable
        
        Args:
        button_name(string): The specific name of the button
        tikinter_button(Button): The actual button 
        """
        self.buttons[button_name] = tkinter_button
    
    def disable_button(self, button_name):
        """
        Disables a specific button within the buttons dictionary
        
        Args:
        button_name(string): Name of the button to be disabled
        """
        self.buttons[button_name]["state"] = "disabled"
    
    def enable_button(self, button_name):
        """
        Enables a specific button within the buttons dictionary

        Args:
        button_name(string): Name of the button to be enabled
        """
        self.buttons[button_name]["state"] = "normal"

if __name__ == "__main__":
    root = Tk()           
    app = interface(root) 
    root.mainloop()       


