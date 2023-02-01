import tkinter as tk
from tkinter import filedialog
from main_1 import test
from main_1 import image_add
import main_1
from tkinter import *
from PIL import ImageTk, Image

window = tk.Tk()
window.title('face regonization app')
window.geometry("1000x1000")
window.config(background = "magenta")
name_var=tk.StringVar()

def names_call():
    t = Text(window)
    for x in main_1.known_face_names:
        t.insert(END,"● "+ x + '\n')
    t.place(x=850, y=100)
names_call()   
    
def delete():
    d1.destroy()
    d2.destroy()
    d3.destroy()

def browsephotos():
    global img,filename,d1,d2,d3
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.jpeg*"),("Text files","*.jpg*"),("all files","*.*")))
    label_1.configure(text="Photo selected: "+filename)
    img = Image.open(filename)
    width,height=img.size
    small_width=(int(width*0.25))
    small_height=(int(height*0.25))
    img=img.resize((small_width, small_height))
    img = ImageTk.PhotoImage(img)
    d1=tk.Label(window, image = img)
    d1.place(x=200,y=200)
    d2=tk.Entry(window,textvariable = name_var, font=('calibre',10,'normal'))
    d2.place(x=200,y=550)
    d3=tk.Button(window,text = "SUBMIT",command=lambda:[submit(),image_add(filename,names),names_call()])
    d3.place(x=200,y=600)
    tk.Button(window,text = "DONE",command=delete).place(x=300,y=600)

def submit():
    global names
    names=name_var.get()
    names_call()

label_1=tk.Label(window,text = "ADD FACE ID HERE",width = 200, height = 4,fg = "blue")
label_1.place(x=0,y=0)
tk.Label(window,text = "Known Face Names").place(x=850,y=74)
tk.Button(window,text = "Browse Photos",command =browsephotos).place(x=650,y=80)
tk.Button(window,text = "TEST",command =test).place(x=1,y=80)
tk.Label(window,text = "Hint : To close the window press {} ".format("Q")).place(x=50,y=85)



window.mainloop()