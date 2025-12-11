from tkinter import *
from Algorithm_factory_pattern import Algorithm_factory


class interface:
    def __init__(self, root):
        self.root = root
        self.factory = Algorithm_factory()
        self.all_algo = ["Search","Sorting","RSA","Factorial","Randomised","Brute force","Fibonacci","Palindrome"]
        self.frames_dict = {}

        self.root.title("Algorithm Interface")
        self.root.geometry("1200x800")

        self.create_intial_frame()
        for algos in self.all_algo:
            self.create_all_frames(algos)

        self.create_widgets()
        self.show_frame("Main menu")

    def show_frame(self, frame_name):
        frame = self.frames_dict[frame_name] 
        frame.tkraise()

    def create_intial_frame(self):
        self.main_menu_frame = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.frames_dict["Main menu"] = self.main_menu_frame

    def create_all_frames(self, algorithm_name):
        self.frame = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frames_dict[algorithm_name] = self.frame

        self.factory.call_frame(algorithm_name, self.frame)
        
        Label(self.frame, text = f"{algorithm_name} Algorithm", bg = "light blue", font = (20), fg = "black").place(x = 10)
        Button(self.frame, text="Back to Main Menu", font = (20), command=lambda: self.show_frame("Main menu")).place(x = 10, y = 165)
    
    def create_widgets(self, y_pos = 50):
        Label(self.main_menu_frame, text = "Main menu - Select Algorithm", font = (20), bg = "light blue", fg = "black").place(x = 10)
        for algorithm in self.all_algo:
            Button(self.main_menu_frame, text = f"{algorithm} Algorithm", font = (20), command=lambda a=algorithm: self.show_frame(a)).place(x = 10, y = y_pos)
            y_pos += 50

if __name__ == "__main__":
    root = Tk()           
    app = interface(root) 
    root.mainloop()       
