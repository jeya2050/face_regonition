import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import torch

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

label_1= tk.Label(window,text = "ADD FACE ID HERE",width = 150, height = 4,fg = "blue")
label_1.place(x=1,y=2)
def display_image():
    global img
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image = img).place(x=200,y=200)

def test():
    global img
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.jpeg*"),("all files","*.*")))
    label_1.configure(text="Photo selected: "+filename)
    img = Image.open(filename)
    width,height=img.size
    small_width=(int(width*0.25))
    small_height=(int(height*0.25))
    img=img.resize((small_width, small_height))
    display_image()
    


button_explore = tk.Button(window,text = "Browse Photos",command =test)
button_explore.place(x=10,y=20)
#Start the GUI
window.mainloop()