#Importing the libraries 
from tkinter import *
import tkinter as tk

#Initializing and creating the canvas
root = tk.Tk()
root.title("Group 21")

canvas = Canvas(root, width=1000, height=5000)
canvas.pack()


def mouseclickevent(event):
    global x, y
    x, y = event.x, event.y
def draw(event):
    global x, y
    canvas.create_line(x, y, event.x, event.y)
    x = event.x
    y = event.y

canvas.bind("<Button-1>", mouseclickevent)
canvas.bind("<B1-Motion>", draw)
# Create a button widget
erase_button = Button(root, text="Erase", command=lambda: canvas.delete("all"))
erase_button.pack()

root.mainloop()