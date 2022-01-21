# 
# :: Tutorial >> https://www.youtube.com/watch?v=YXPyB4XeYLA
from tkinter import *

root = Tk()

# :: 1. define thing, creating a label widget
myLabel = Label(root, text="Hello World!")

# :: 2. put in on screen, showing it onto the screen
myLabel.pack()


root.mainloop()