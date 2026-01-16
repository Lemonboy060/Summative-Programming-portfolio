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
        factory.create_frame(algorithm_name, self.frame)

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
    def create_frame(self, algorithm_name, frame):
        if algorithm_name == "Palindrome":
            palindrome(frame)
        elif algorithm_name == "Factorial":
            factorial(frame)
        elif algorithm_name == "Fibonacci":
            fibonacci(frame)
        elif algorithm_name == "Randomised":
            randomised(frame)
        elif algorithm_name == "Sorting":
            sorting(frame)
        elif algorithm_name == "Search":
            search(frame)
        elif algorithm_name == "Brute force":
            merge(frame)
        elif algorithm_name == "RSA":
            RSA(frame)
        else:
            messagebox.showerror("Error")

if __name__ == "__main__":
    root = Tk()           
    app = interface(root) 
    root.mainloop()       


