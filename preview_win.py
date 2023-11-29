from tkinter import *
from PIL import (Image, ImageTk)

def show_preview(path):

    root = Tk()  # create a root widget
    root.title("Tk Example")
    #may have to change path
    img = Image.open(f"./{path}")
    img = ImageTk.PhotoImage(img)
    label = Label(root, image=img)
    label.pack()
    root.mainloop()