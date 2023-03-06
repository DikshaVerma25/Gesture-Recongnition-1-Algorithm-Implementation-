#Importing the libraries
from tkinter import *
import tkinter as tk
import math
from typing import List
import time

N=64

Unistrokes=[("circle",[(127,141),(124,140),(120,139),(118,139),(116,139),(111,140),(109,141),(104,144),(100,147),(96,152),(93,157),(90,163),(87,169),(85,175),(83,181),(82,190),(82,195),(83,200),(84,205),(88,213),(91,216),(96,219),(103,222),(108,224),(111,224),(120,224),(133,223),(142,222),(152,218),(160,214),(167,210),(173,204),(178,198),(179,196),(182,188),(182,177),(178,167),(170,150),(163,138),(152,130),(143,129),(140,131),(129,136),(126,139)])]

def resample(points,N):
    M=totalpathlength(points)
    # I is the interval length
    I=0.0
    I=M/63
    D=0.0
    newpoints=[points[0]]
    
    i = 1
    while i < len(points):
        previous, current = points[i - 1:i + 1]
        d = distance(previous, current)
        if ((D + d) >= I):
            q = (previous[0] + ((I - D) / d) * (current[0] - previous[0]),
                    previous[1] + ((I - D) / d) * (current[1] - previous[1]))
            # append new point 'q'
            newpoints.append(q)
            # insert 'q' at position i in points s.t. 'q' will be the next i
            points.insert(i, q)
            D = 0
        else:
            D += d
        i += 1
    # somtimes we fall a rounding-error short of adding the last point, so
    # add it if so
    if len(newpoints) == 63:
        newpoints.append(newpoints[-1])
    points = newpoints
    return points



def totalpathlength(points):
    d=0.0
    for i in range(1,len(points)):
        print("tpl ",i,d)
        d=float(d+distance(points[i-1],points[i]))
    return d

def distance(pt1,pt2):
    d=0.0
    dx=float(pt2[0]-pt1[0])
    dy=float(pt2[1]-pt2[1])
    d=float(math.sqrt((dx*dx)+(dy*dy)))
    return d






