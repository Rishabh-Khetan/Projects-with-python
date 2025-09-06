from tkinter import *
from tkinter.ttk import *


from time import strftime

root = Tk()
root.title("Clock")

def time():
    str= strftime('%H:%M:%S %p')
    lable.config(text=str)
    lable.after(1000,time)

lable = Label(root, font=("ATC Laurel Black", 80), background = "pink" , foreground = "blue")
lable.pack(anchor="center") 
 
time()

mainloop()


