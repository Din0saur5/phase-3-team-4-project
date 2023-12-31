from tkinter import *
from PIL import (Image, ImageTk)


def show_preview(pic):

    root = Tk()  # create a root widget
    root.title(f"{pic.title}")
    def get_image_dimensions(path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                return width, height
        except IOError as e:
            print(f"Error opening the image: {e}")
            return None
    #may have to change path
    path = f"./{pic.preview}"
    img = ImageTk.PhotoImage(file=path)
    width, height = get_image_dimensions(path)
    root.geometry(f"{width}x{height}")
    my_canvas = Canvas(root, height=height, width=width)
    my_canvas.pack(fill="both", expand=True)
    
    my_canvas.create_image(0,0, image=img, anchor="nw")
    
    def resizer(e):
        global img1, resized_bg, new_img
        img1 = Image.open(f"./{path}")
        resized_bg = img1.resize((e.width,e.height), Image.ADAPTIVE)
        new_img = ImageTk.PhotoImage(resized_bg)
        my_canvas.create_image(0,0, image=new_img, anchor="nw")
# Define a function to close the window
    def close():
        root.destroy()
        #root.quit()
    

    root.bind('<Configure>', resizer)
   
    root.mainloop()
    

if __name__ == '__main__':
    show_preview()