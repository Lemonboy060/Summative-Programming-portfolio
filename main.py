from tkinter import *

class interface:
    def __init__(self, root):
        self.root = root
        self.all_algo = ["Search","Sorting","RSA","Recursion","Randomised","Brute force","Fibonacci","Palindrome"]
        self.all_frames = []
        self.root.title("Algorithm Interface")
        self.root.geometry("1200x800")

        self.create_frames()
        self.create_widgets()

        self.show_frame(self.main_menu_frame)

    def show_frame(self, frame):
        frame.tkraise()

    def create_frames(self):
        self.main_menu_frame = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        self.all_frames.append(self.main_menu_frame)

        # for algorithm in self.all_algo:
        #     self.algorithm = Frame(self.root, bg = "light blue", width = 1200, height = 800)
        #     self.all_frames.append(self.algorithm)

        for frame in self.all_frames:
            frame.pack()
    
    def create_widgets(self, y_pos = 50):
        Label(self.main_menu_frame, text = "Main menu - Select Algorithm", font = (20), bg = "light blue", ).place(x = 10)
        for algorithm in self.all_algo:
            Button(self.main_menu_frame, text = f"{algorithm} Algorithm", font = (20)).place(x = 10, y = y_pos)
            y_pos += 50

if __name__ == "__main__":
    root = Tk()           
    app = interface(root) 
    root.mainloop()       
