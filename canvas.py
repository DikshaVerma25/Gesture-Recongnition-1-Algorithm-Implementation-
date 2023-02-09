#Importing the libraries
from tkinter import *
import tkinter as tk
import math
from typing import List
# importing the controller class which has function to process the candidates and the templates
import controller as cntrl
numUnistrokes = 16


object1=cntrl.Recognizer(numUnistrokes)



#Initializing and creating the canvas
root = tk.Tk()
root.title("Group 21")

canvas = Canvas(root, width=700, height=700)
canvas.pack()

global points,f
points = []
num_points =64
# flag variable to reset the canvas when drawing a new gesture again
f=0



def redraw(line_array):
   
    canvas.create_line(line_array)
    # x = event.x
    # y = event.y
    # points.append((x, y))

def mouseclickevent(event):
    global x, y,points,f
    if f>1:
        canvas.delete("all")
    f=1
    
    x, y = event.x, event.y
    points.append((x, y))
    
def draw(event):
    global x, y,points,f
    canvas.create_line((x, y, event.x, event.y),fill='red',width=4)
    x = event.x
    y = event.y
    points.append((x, y))

def on_release(event):
    global f,points
    f=f+1
    x, y = event.x, event.y
    points.append((x, y))
    print(len(points))
    if len(points)>1:
        k=object1.Recognize(points,False)
        print("Answer: ",k.Name,k.Score)
   
    # print(cntrl.centroid(points))
    points=[] 

# button to start the drawing of a gesture and to add the starting point of a gesture to the points array
canvas.bind("<ButtonPress>", mouseclickevent)
# button to draw the gesture in a series of continuous points
canvas.bind("<B1-Motion>", draw)
# button release to capture/store/process the python main.py points on the canvas on release of the button
canvas.bind("<ButtonRelease>", on_release)



root.mainloop()