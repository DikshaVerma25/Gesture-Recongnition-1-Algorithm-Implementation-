#Importing the libraries
from tkinter import *
import tkinter as tk
import math
from typing import List
# importing the controller class which has function to process the candidates and the templates
# import controller as cntrl
# numUnistrokes = 16


# object1=cntrl.Recognizer(numUnistrokes)

import backend as bend
# for resampling into same number of points
N=64
Unistrokes=[("circle",[(127,141),(124,140),(120,139),(118,139),(116,139),(111,140),(109,141),(104,144),(100,147),(96,152),(93,157),(90,163),(87,169),(85,175),(83,181),(82,190),(82,195),(83,200),(84,205),(88,213),(91,216),(96,219),(103,222),(108,224),(111,224),(120,224),(133,223),(142,222),(152,218),(160,214),(167,210),(173,204),(178,198),(179,196),(182,188),(182,177),(178,167),(170,150),(163,138),(152,130),(143,129),(140,131),(129,136),(126,139)])]


#Initializing and creating the canvas
root = tk.Tk()
root.title("Group 21")

canvas = Canvas(root, width=700, height=700)
canvas.pack()

global points,f
points = []

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
    print(len(points),len(Unistrokes[0][1]))
    newpoints=bend.resample(points,N)
    tnewpoints=bend.resample(Unistrokes[0][1],N)
    print("template new points",len(tnewpoints))
    print("candidate new points",len(newpoints))
    redraw(tnewpoints)
    points=[] 

# button to start the drawing of a gesture and to add the starting point of a gesture to the points array
canvas.bind("<ButtonPress>", mouseclickevent)
# button to draw the gesture in a series of continuous points
canvas.bind("<B1-Motion>", draw)
# button release to capture/store/process the python main.py points on the canvas on release of the button
canvas.bind("<ButtonRelease>", on_release)



root.mainloop()