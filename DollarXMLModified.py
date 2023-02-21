from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET
import os
import filestruct1 as filest
import random
import copy
text = os.getcwd()
# hj=0
data = []

# Template points will be stored in UNISTROKE variable
# List of List is being used to store the template points
data=filest.XMLfolder().data
OriginalData = copy.deepcopy(data)

# print("&&&&&& ",len(xmlfiles),len(xmlfiles[0]),len(xmlfiles[0][0]),len(xmlfiles[0][0][0][0]),xmlfiles[0][0][0][0])

# num variable stores the N value- that divides the total path length into N point path
num = 64
origin = (0, 0)
# bounding box square size
square_size = 350
range_of_angle = (2 / 180) * pi
angle_p = (2 / 180) * pi
phi = 0.5 * (-1.0 + (5.0)**0.5)
Diagonal = math.sqrt(square_size * square_size + square_size * square_size)
HalfDiagonal = 0.5 * Diagonal

class Recognize:
    def preprocess(pointse):
        g=Gesture()
        p=g.resample(pointse)
        p1=g.rotateTo(-g.indicative_angle(p),p)
        p2=g.scale_to(square_size,p1)
        p3=g.translate_to(origin,p2)
        return p3
        

class Gesture:

#This is done by calculating the desired distance between the points and resampling it in such a way that there are total 64 points.
# the resampling function will calculatethe distance between two adjacent points and if the distance is greater than the set interval I,
# at each interval I ,it will add a new point.
# the candidate and templategestures will have same number of points
    def resample(self,pointse):
        points = pointse
        I = self.path_length(pointse) / (num - 1)
        D = 0
        new_points = [points[0]]
        i = 1
        while i < len(points):
            pt1, pt2 = points[i - 1:i + 1]
            d = distance(pt1, pt2)
            if ((D + d) >= I):
                q = (pt1[0] + ((I - D) / d) * (pt2[0] - pt1[0]),
                    pt1[1] + ((I - D) / d) * (pt2[1] - pt1[1]))
                # append new point 'q'
                new_points.append(q)
                # insert 'q' at position i in points s.t. 'q' will be the next i
                points.insert(i, q)
                D = 0
            else:
                D += d
            i += 1
        # somtimes we fall a rounding-error short of adding the last point, so
        # add it if so
        if len(new_points) == num - 1:
            new_points.append(new_points[-1])
        pointse = new_points
        return pointse


#The length of the path of gesture is calculated using this method
# the distance between two adajcent points is calculated and added to the total distance d to get the path length
    def path_length(self,pointse):
        d = 0
        for i in range(1, len(pointse)):
            d += distance(pointse[i - 1], pointse[i])
        return d
# this will calculate the centroid and compute the angle with respect to the X axis and the centroid line between c(x,y)and points(x,y)
    def indicative_angle(self,pointse):
        # angle formed by (points[0], centroid) and the horizon
        c = self.centroid(pointse)
        return atan2(c[1] - pointse[0][1], c[0] - pointse[0][0])


    def centroid(self,pointse):
        n = len(pointse)
        return (
            sum([p[0] / n for p in pointse]),
            sum([p[1] / n for p in pointse])
        )


#This function is rotating the gesture to its centroid whose points are provided by a different function
# Here it uses the cosine and sine values of radian angle for rotating which are then stored in a new_points array 
# It will rotate te x axis point counter clockwise and rotate the Y coordinate clockwise to get a best fit using the indicative angle returned
# vetween the centroid line and the x axis
    def rotateTo(self, angle,pointse):
        c = self.centroid(pointse)
        new_points = []
        for p in pointse:
            dx, dy = p[0] - c[0], p[1] - c[1]
            new_points.append((
                dx * cos(angle) - dy * sin(angle) + c[0],
                dx * sin(angle) + dy * cos(angle) + c[1]
            ))
        pointse = new_points
        return pointse



#This function helps to scale the gesture to a bounding box.
#It takes one inputs and then calls the BoundingBox function which returns points of new rectangle
#After creating new array it  creates new coordinates by multiplying original to scaling factor
#Scaling factor is desire size (in this case is square size by width and height of bounding box)
    def scale_to(self, size,pointse):
        B = self.bounding_box(pointse)
        new_points = []
        for p in pointse:
            new_points.append((
                p[0] * size / B[0],
                p[1] * size / B[1]
            ))
        pointse = new_points
        return pointse

    
#Bounding Box is smallest rectangle that will enclose the gesture where array points is passed as parameter
# after initializing all the required variables it loopsthrough all the points resulting in the dimensions os the
# smallest rectangle by substracting the min values to max     
    def bounding_box(self,pointse):
        minX, maxX = inf, -inf
        minY, maxY = inf, -inf
        for point in pointse:
            minX, maxX = min(minX, point[0]), max(maxX, point[0])
            minY, maxY = min(minY, point[1]), max(maxY, point[1])
        return (maxX - minX, maxY - minY)

#recentering the gesture by aligning its centroid to  the origin
    def translate_to(self, target,pointse):
        c = self.centroid(pointse)
        new_points = []
        for p in pointse:
            new_points.append((
                p[0] + target[0] - c[0],
                p[1] + target[1] - c[1]
            ))
        pointse = new_points
        return pointse

# distance at best angle will rotate a normalized gesture at various angles and calculatte the distance between the rotated gesture and a set of 
# reference templates. The angle that produces the smallest distance is considered the "best angle" for recognizing the symbol. 
    def distance_at_best_angle(self, T,pointse):
        a = -range_of_angle
        b = range_of_angle
        x1 = phi * a + (1 - phi) * b
        x2 = phi * b + (1 - phi) * a
        f1 = self.distace_at_angle(T, x1,pointse)
        f2 = self.distace_at_angle(T, x2,pointse)
        while abs(b - a) > angle_p:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = phi * a + (1 * phi) * b
                f1 = self.distace_at_angle(T, x1,pointse)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = phi * b + (1 - phi) * a
                f2 = self.distace_at_angle(T, x2,pointse)
        return min(f1, f2)

    def distace_at_angle(self, T, angle,pointse):
        r_angle = Gesture()
        r_angle.rotateTo(angle,pointse)
        return r_angle.path_distance(T,pointse)

    def path_distance(self,templatepoints,pointse):
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(self.points))
        if len(templatepoints)>64:
            print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",templatepoints)
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(points))

        n = len(templatepoints)
        #print("###########################################################################",n)
        return sum([distance(pointse[i], templatepoints[i]) / n for i in range(n)])


def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5




class Input:
    # Preprocess the template points e.g resample,rotate, scale to and translate
    
    # processed_xml_files=[]
    def __init__(self):
        # format the example gestures
        t0 = time.time()
        self.preprocessALLGestures1(data)
    

    def preprocessALLGestures1(self,data):
        numUsers=len(data[0][0])
        numSpeed=len(data[1][0])
        numGestures=len(data[1][1][1][1])
        numForEachGesture=len(data[1][1][1][1][1][1])
        c=0
        cn=0
        Speed=1
        for user in range(numUsers):
            # for speed in range(numSpeed):
            for gesture in range(numGestures):
                for t in range(numForEachGesture):
                    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",data[user][1][Speed][1][gesture][1][t])
                    arr=Recognize.preprocess(data[user][1][Speed][1][gesture][1][t])
                    data[user][1][Speed][1][gesture][1][t]=arr
                    if len(arr)==64:
                        c=c+1
                    else:
                        cn=cn+1

        # random 100 loop can be used here
        for user in range(numUsers):
        # for speed in range(numSpeed):
            for t in range(numForEachGesture):
                
                for f in range(2):
                    Templates1=  []
                    cd=[]
                    Templatesiszearr=[]
                    r=random.randint(0,9)
                    for gesture in range(numGestures):

                        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",data[user][1][Speed][1][gesture][1][t])
                        # arr=Gesture(data[user][1][Speed][1][gesture][1][t])
                        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",len(arr.points))
                        # data[user][1][1][1][gesture][1][t]=arr.points
                        # na= candidate gesture name, cd=candidate points
                        # cd,na=data[user][1][Speed][1][gesture][1][r],data[user][1][Speed][1][gesture][0]
                        candidatename=data[user][1][Speed][1][gesture][0]
                        ct=data[user][1][Speed][1][gesture][1][r]
                        cd.append((candidatename,ct))
                        # print("*******************************",data[user][1][Speed][1][gesture][0])
                        if r!=t:
                            dt=data[user][1][Speed][1][gesture][1][t]
                            templateName=data[user][1][Speed][1][gesture][0]
                            Templatesiszearr.append(len(dt))
                            Templates1.append((templateName,dt))
                    print("cadidtae array length ############## ",len(cd))  
                    h=0
                    for candidate in cd:
                        [print("inside candidate loop******=====",len(temp[1])) for temp in Templates1]
                        if h>3:
                            break
                        result=self.rec_ges(candidate[1],Templates1)

                        print("result####################################################################### ",result)
                        h=h+1
                        

                    # [print("Raja=====",len(temp[1])) for temp in Templates1]
                    # for g in range(numGestures):
                    #     cd,na=data[user][1][Speed][1][g][1][r],data[user][1][Speed][1][g][0]
                    #     result=self.rec_ges(cd,Templates1) 
                    #     print("result####################################################################### ",result,na)
                Templates1=  []
                cd=[]
            Templates1=  []
            cd=[]
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",c,cn)
        
# recognition gesture function will perform golden search using the golden ratio which calls the method distance at best angle
    def rec_ges(self, pointse,Templates2):

        # here the call to gesture class will preprocess the candidate points
        t0 = time.time()
        copyTemplate = copy.deepcopy(Templates2)
        print("CopyTmplay Before==", len(copyTemplate))
        print("Josh LEMN===",len(Templates2))
        [print("JOSH=====",len(temp[1])) for temp in Templates2]
        ges = Gesture()
        resamplespoints=Recognize.preprocess(pointse)
        [print("JOSH22=====",len(temp[1])) for temp in copyTemplate]
        print("CopyTmplay==", len(copyTemplate))
        b = inf
        result = ''
        k=[]
        for template_stroke in copyTemplate:
            # returns the distance between candidate points and the template points after preprocessing
            # if len(template_stroke[1])>64:
            #     print("****************************************************************",template_stroke[0])
            # else:
            #print("JOSH1===",len(template_stroke[1]))
            #[print("JOSH222222=====",len(temp[1]),end='') for temp in Templates2]
            #print()
            d = ges.distance_at_best_angle(template_stroke[1],resamplespoints)

            # calculates the minimum distance and store the template name with the minimum distance to recognize the gesture
            result1 = template_stroke[0]
            if d < b:
                # update the pt2 best gesture
                b = d
                result = template_stroke[0]
                k.append((result,1.0 - b / HalfDiagonal))

                
        print("k @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",k) 
        return (result,1.0 - b / HalfDiagonal)


Input()
    


