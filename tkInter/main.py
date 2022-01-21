# 
# :: Tutorial >> https://www.youtube.com/watch?v=YXPyB4XeYLA
# :: 30m
from tkinter import *

root = Tk()

def myClick():
    myLabel3 = Label(root, text="Hello World!")
    myLabel3.pack()

# :: 1. define thing, creating a label widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Some other text")

myButton = Button(root, text="Click", padx=50, command=myClick)
# :: 2. put in on screen, showing it onto the screen
# myLabel.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

myButton.pack()


# :: create program
root.mainloop()