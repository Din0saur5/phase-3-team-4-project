from tkinter import *

root = Tk()  # create a root widget
root.title("Tk Example")
root.configure(background="yellow")
bg = PhotoImage(file="../gallery_photos/Figs.jpg")
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()