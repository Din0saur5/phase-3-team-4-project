from tkinter import *
from PIL import (Image, ImageTk)


def show_preview(pic):

    root = Tk()  # create a root widget
    root.title(f"{pic.title}")
    root.geometry("800x1000")
    #may have to change path
    path = f"./{pic.preview}"
    img = ImageTk.PhotoImage(file=path)
    my_canvas = Canvas(root, height=800, width=1000)
    my_canvas.pack()
    
    my_canvas.create_image(0,0, image=img, anchor="nw")
    
    def resizer(e):
        img = Image.open(f"./{path}")
        e.height
        e.width
# Define a function to close the window
    def close():
        root.destroy()
        #root.quit()
    
    Button(root, text= "Close the Window", font=("Calibri",14,"bold"), command=close).pack(pady=20)
   
    root.bind('<Configure>', resizer)
   
    root.mainloop()
    

if __name__ == '__main__':
    show_preview()