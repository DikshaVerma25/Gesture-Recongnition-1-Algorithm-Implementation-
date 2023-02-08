#Importing the libraries
from tkinter import *
import tkinter as tk

points = []

#Initializing and creating the canvas
root = tk.Tk()
root.title("Group 21")

canvas = Canvas(root, width=700, height=700)
canvas.pack()


def mouseclickevent(event):
    global x, y
    x, y = event.x, event.y
    points.append((x, y))
    
def draw(event):
    global x, y
    canvas.create_line((x, y, event.x, event.y),fill='red',width=4)
    x = event.x
    y = event.y

canvas.bind("<Button-1>", mouseclickevent)
canvas.bind("<B1-Motion>", draw)


#Adding eraser button
erase_button = Button(root, text="Erase", command=lambda: canvas.delete("all"))
erase_button.pack()


for elements in points:
    print(elements)
    
root.mainloop()
