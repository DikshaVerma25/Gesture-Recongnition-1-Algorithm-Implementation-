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

# points1=[]
# seasons = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]

# gestures = ["arrow", "caret" , "check" , "circle" , "delete" , "left-curly_brace" , "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" , "star", "triangle" , "v" , "x"]
# m={}
# # filestructure=[]
# for sname in seasons:
#     directory = text + '/xml_logs/'+sname+'/medium'

#     for filename in os.listdir(directory):
#         # directory.join('/s01/medium/')cd  
#         if filename.endswith('.xml'):
#             # build the full path to the XML file
#             filepath = os.path.join(directory, filename)
            
#             # parse the XML file
#             tree = ET.parse(filepath)
            
#             # get the root element
#             root = tree.getroot()
            
#             # print('XML file:', filepath)
#             gesname=filepath.replace(directory+"\\","")
#             ges=gesname[:-6]
#             # print("&&&&&&&   "+ges)
#             # do something with the data from the XML file
#             # for example, print the tag and text of each element
            
#             # if ges not in m:
#             #     m[ges]=
#             # for child in root:
#             #     item = {}
#             #     for key, value in child.attrib.items():
#             #         item[key] = value
#             #     data.append(item)
            
#         if hj<2:
#             for point in root.findall(".//Point"):
#                 x = int(point.attrib["X"])
#                 y = int(point.attrib["Y"])
#                 points1.append([x, y])
#             # print("^^^",points1)
            
            

#             if ges not in m:
#                 m[ges]=[points1]
#             else:
#                 arr=m[ges]
#                 arr.append(points1)
#             hj=hj+1
#             points1=[]

    
#     # append the dictionary to the list
# p=m["arrow"]
# print("file: ",p, len(p))   
# import json

# with open('output.txt', 'w') as filehandle:
#     json.dump(p, filehandle)

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


class Gesture:
    
    def __init__(self, points, flag=True):
        self.points = points
        if flag:
            # preprocessing the candidate points or the template points based on the initialized call
            print("Gesture here check",len(self.resample()))
            
            self.rotateTo(-self.indicative_angle())
            self.scale_to(square_size)
            self.translate_to(origin)

#This is done by calculating the desired distance between the points and resampling it in such a way that there are total 64 points.
# the resampling function will calculatethe distance between two adjacent points and if the distance is greater than the set interval I,
# at each interval I ,it will add a new point.
# the candidate and templategestures will have same number of points
    def resample(self):
        points = self.points
        I = self.path_length() / (num - 1)
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
        self.points = new_points
        return self.points


#The length of the path of gesture is calculated using this method
# the distance between two adajcent points is calculated and added to the total distance d to get the path length
    def path_length(self):
        d = 0
        for i in range(1, len(self.points)):
            d += distance(self.points[i - 1], self.points[i])
        return d
# this will calculate the centroid and compute the angle with respect to the X axis and the centroid line between c(x,y)and points(x,y)
    def indicative_angle(self):
        # angle formed by (points[0], centroid) and the horizon
        c = self.centroid()
        return atan2(c[1] - self.points[0][1], c[0] - self.points[0][0])


    def centroid(self):
        n = len(self.points)
        return (
            sum([p[0] / n for p in self.points]),
            sum([p[1] / n for p in self.points])
        )


#This function is rotating the gesture to its centroid whose points are provided by a different function
# Here it uses the cosine and sine values of radian angle for rotating which are then stored in a new_points array 
# It will rotate te x axis point counter clockwise and rotate the Y coordinate clockwise to get a best fit using the indicative angle returned
# vetween the centroid line and the x axis
    def rotateTo(self, angle):
        c = self.centroid()
        new_points = []
        for p in self.points:
            dx, dy = p[0] - c[0], p[1] - c[1]
            new_points.append((
                dx * cos(angle) - dy * sin(angle) + c[0],
                dx * sin(angle) + dy * cos(angle) + c[1]
            ))
        self.points = new_points



#This function helps to scale the gesture to a bounding box.
#It takes one inputs and then calls the BoundingBox function which returns points of new rectangle
#After creating new array it  creates new coordinates by multiplying original to scaling factor
#Scaling factor is desire size (in this case is square size by width and height of bounding box)
    def scale_to(self, size):
        B = self.bounding_box()
        new_points = []
        for p in self.points:
            new_points.append((
                p[0] * size / B[0],
                p[1] * size / B[1]
            ))
        self.points = new_points

    
 #Bounding Box is smallest rectangle that will enclose the gesture where array points is passed as parameter
 # after initializing all the required variables it loopsthrough all the points resulting in the dimensions os the
 # smallest rectangle by substracting the min values to max     
    def bounding_box(self):
        minX, maxX = inf, -inf
        minY, maxY = inf, -inf
        for point in self.points:
            minX, maxX = min(minX, point[0]), max(maxX, point[0])
            minY, maxY = min(minY, point[1]), max(maxY, point[1])
        return (maxX - minX, maxY - minY)

#recentering the gesture by aligning its centroid to  the origin
    def translate_to(self, target):
        c = self.centroid()
        new_points = []
        for p in self.points:
            new_points.append((
                p[0] + target[0] - c[0],
                p[1] + target[1] - c[1]
            ))
        self.points = new_points

# distance at best angle will rotate a normalized gesture at various angles and calculatte the distance between the rotated gesture and a set of 
# reference templates. The angle that produces the smallest distance is considered the "best angle" for recognizing the symbol. 
    def distance_at_best_angle(self, T):
        a = -range_of_angle
        b = range_of_angle
        x1 = phi * a + (1 - phi) * b
        x2 = phi * b + (1 - phi) * a
        f1 = self.distace_at_angle(T, x1)
        f2 = self.distace_at_angle(T, x2)
        while abs(b - a) > angle_p:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = phi * a + (1 * phi) * b
                f1 = self.distace_at_angle(T, x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = phi * b + (1 - phi) * a
                f2 = self.distace_at_angle(T, x2)
        return min(f1, f2)

    def distace_at_angle(self, T, angle):
        r_angle = Gesture(self.points, False)
        r_angle.rotateTo(angle)
        return r_angle.path_distance(T)

    def path_distance(self, points):
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(self.points))
        if len(points)>64:
            print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",points)
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(points))

        n = len(points)
        #print("###########################################################################",n)
        return sum([distance(self.points[i], points[i]) / n for i in range(n)])


def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5




class Input:
    # Preprocess the template points e.g resample,rotate, scale to and translate
    
    # processed_xml_files=[]
    def __init__(self):
        # format the example gestures
        t0 = time.time()
        # self.processed_xml_files=[]
        self.preprocessALLGestures1(data)
        # a = [len(self.processed_xml_files[i1][i2][i3][i4]) for i1 in range(len(self.processed_xml_files)) for i2 in range(len(self.processed_xml_files[0])) for i3 in range(len(self.processed_xml_files[0][0])) for i4 in range(len(self.processed_xml_files[0][0][0]))]
        # print(a)
        # self.unistrokes = []
        # for template in Templates:
        #     self.unistrokes.append(Gesture(template[1]))
        #     self.unistrokes[-1].name = template[0]
        # if f:
        # self.random_100(self.processed_xml_files)
        # print("777777",self.processed_xml_files[0][0][0][0])
        
   
    # def preprocessALLGestures1(self,xmlfiles):
    #     processed_xml_files=[]

    #     for user in range(len(xmlfiles)):
    #         p=[]
    #         for speed in range(len(xmlfiles[user])):
    #             q=[]
    #             for g in range(len(xmlfiles[user][speed])):
    #                 r=[]
    #                 for t in range(len(xmlfiles[user][speed][g])):
    #                     arr=Gesture(xmlfiles[user][speed][g][t])
    #                     print("---------",len(arr.points))
    #                     r.append(arr.points)
    #                 q.append(r)
    #             p.append(q)
    #         processed_xml_files.append(p)
    #     return processed_xml_files

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
                    arr=Gesture(data[user][1][Speed][1][gesture][1][t])
                    data[user][1][Speed][1][gesture][1][t]=arr.points
                    if len(arr.points)==64:
                        c=c+1
                    else:
                        cn=cn+1

        # random 100 loop can be used here
        for user in range(numUsers):
        # for speed in range(numSpeed):
            for t in range(numForEachGesture):
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
                    cd,na=data[user][1][Speed][1][gesture][1][0],data[user][1][Speed][1][gesture][0]
                    # print("*******************************",data[user][1][Speed][1][gesture][0])
                    if r!=t:
                        dt=data[user][1][Speed][1][gesture][1][t]
                        templateName=data[user][1][Speed][1][gesture][0]
                        Templatesiszearr.append(len(dt))
                        Templates1.append((templateName,dt))
                
                
                # [print("Raja=====",len(temp[1])) for temp in Templates1]
                result=self.rec_ges(cd,Templates1) 
                print("result####################################################################### ",result,na)

                

                    
                        
                   
               
        
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",c,cn)



            
                
    # def random_100(self):
    #     pace=1
    #     Users = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
    #     SpeedArray=["fast","medium","slow"]
    #     gestures = ["arrow", "caret" , "check" , "circle" , "delete_mark" , "left_curly_brace" , "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" , "star", "triangle" , "v" , "x"]
    #     gesturetypenumber=["01","02","03","04","05","06","07","08","09","10"]
    #     for user in range(len(self.processed_xml_files)):
           

    #             for g in range(len(self.processed_xml_files[user][pace])):
    #                 # for i in range(100):
    #                 # Candidate=self.processed_xml_files[user][pace][g][r]
    #                 Templates=[]
    #                 r=random.randint(0,9)
    #                 for t in range(9):
                        

    #                     if r!=t:
    #                         str=gestures[g]+gesturetypenumber[t]
    #                         Templates.append((str,self.processed_xml_files[user][pace][g][t]))
    #                         # print("Templates^^^ ",Templates)
    #                 for k in range(1,g):
    #                     Candidate=self.processed_xml_files[user][pace][k][r]
    #                     print("template size******",len(Templates))
    #                     result=self.rec_ges(Candidate,Templates) 
    #                     print("$$$$$$$$$$ ",result) 
                    
                
    # def random_100(self):
    #     pace=1
    #     Users = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
    #     SpeedArray=["fast","medium","slow"]
    #     gestures = ["arrow", "caret" , "check" , "circle" , "delete_mark" , "left_curly_brace" , "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" , "star", "triangle" , "v" , "x"]
    #     gesturetypenumber=["01","02","03","04","05","06","07","08","09","10"]
    #     a = [len(self.processed_xml_files[i1][i2][i3][i4])for i1 in range(len(self.processed_xml_files)) for i2 in range(len(self.processed_xml_files[0])) for i3 in range(len(self.processed_xml_files[0][0])) for i4 in range(len(self.processed_xml_files[0][0][0]))]
        
    #     print(a)
        
    #     for user in range(len(self.processed_xml_files)):

    #         for t in range(9):      
    #             Templates=[]
    #             r=random.randint(0,9)  
    #             if r!=t:

    #                 for g in range(len(self.processed_xml_files[user][pace])):
    #                         str=gestures[g]+gesturetypenumber[t]
    #                         print("here", len(self.processed_xml_files[user][pace][g][t]), user,g,t)
    #                         Templates.append((str,self.processed_xml_files[user][pace][g][t]))
    #                 for k in range(len(self.processed_xml_files[user][pace])):
    #                     Candidate=self.processed_xml_files[user][pace][k][r]
    #                     print(user,pace,k,r)
    #                     a = [len(Templates[temp][1]) for temp in range(len(Templates))]
    #                     print("Candidate size******",len(Candidate))
    #                     print("template size******",a)
    #                     # s=self.Input(Templates,False)
    #                     self.unistrokes = []
    #                     for template in Templates:
    #                         self.unistrokes.append(Gesture(template[1]))
    #                         self.unistrokes[-1].name = template[0]
    #                     result=self.rec_ges(Candidate, self.unistrokes) 
    #                     print("$$$$$$$$$$ ",result) 
                
    def random_100(self,processed_xml_files):
        pace=1
        Users = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
        SpeedArray=["fast","medium","slow"]
        gestures = ["arrow", "caret" , "check" , "circle" , "delete_mark" , "left_curly_brace" ,"left_sq_bracket", "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" ,"right_sq_bracket", "star", "triangle" , "v" , "x"]
        gesturetypenumber=["01","02","03","04","05","06","07","08","09","10"]
        # a = [len(processed_xml_files[i1][i2][i3][i4])for i1 in range(len(self.processed_xml_files)) for i2 in range(len(self.processed_xml_files[0])) for i3 in range(len(self.processed_xml_files[0][0])) for i4 in range(len(self.processed_xml_files[0][0][0]))]
        
        # print(a)
        
        for user in range(len(processed_xml_files)):

            for t in range(0,9):      
                Templates=[]
                r=random.randint(0,9)  
                if r!=t:

                    for g in range(len(processed_xml_files[user][pace])):
                            str=gestures[g]+gesturetypenumber[t]
                            print("here", len(processed_xml_files[user][pace][g][t]), user,g,t)
                            Templates.append((str,processed_xml_files[user][pace][g][t]))
                    for k in range(len(processed_xml_files[user][pace])):
                        str1=gestures[k]+gesturetypenumber[r]

                        Candidate=processed_xml_files[user][pace][k][r]
                        print("Candidate name ",str1)
                        print(user,pace,k,r)
                        a = [len(Templates[temp][1]) for temp in range(len(Templates))]
                        print("Candidate size******",len(Candidate))
                        print("template size******",a)
                        if len(Templates[0][1])>64:
                            self.unistrokes = []
                            ti=[]
                            for template in Templates:
                                l=Gesture(template[1])
                                ti.append((template[0],l.points))
                            Templates=ti
                        result=self.rec_ges(Candidate, Templates) 
                        print("$$$$$$$$$$ ",result) 
                

                    
                
            
                            





       
    


    # # recognition gesture function will perform golden search using the golden ratio which calls the method distance at best angle
    # def rec_ges(self, points,Templates):

    #     # here the call to gesture class will preprocess the candidate points
    #     t0 = time.time()

    #     ges = Gesture(points)
    #     b = inf
    #     result = ''
    #     for template_stroke in Templates:
    #         # returns the distance between candidate points and the template points after preprocessing
    #         d = ges.distance_at_best_angle(template_stroke.points)

    #         # calculates the minimum distance and store the template name with the minimum distance to recognize the gesture
    #         if d < b:
    #             # update the pt2 best gesture
    #             b = d
    #             result = template_stroke.name
            
    #     return (result,1.0 - b / HalfDiagonal)
  # recognition gesture function will perform golden search using the golden ratio which calls the method distance at best angle
    def rec_ges(self, points,Templates2):

        # here the call to gesture class will preprocess the candidate points
        t0 = time.time()
        copyTemplate = copy.deepcopy(Templates2)
        print("CopyTmplay Before==", len(copyTemplate))
        print("Josh LEMN===",len(Templates2))
        [print("JOSH=====",len(temp[1])) for temp in Templates2]
        ges = Gesture(points)
        [print("JOSH22=====",len(temp[1])) for temp in Templates2]
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
            d = ges.distance_at_best_angle(template_stroke[1])

            # calculates the minimum distance and store the template name with the minimum distance to recognize the gesture
            result1 = template_stroke[0]
            if d < b:
                # update the pt2 best gesture
                b = d
                result = template_stroke[0]
                k.append((result,1.0 - b / HalfDiagonal))

                
        print("k @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",k) 
        return (result,1.0 - b / HalfDiagonal)


# class Can:
            
    
#     global points,f
#     points = []
#     num_points =64
#     # flag variable to reset the canvas when drawing a new gesture again
#     f=0        
#     numUnistrokes = 16


#     # object1=cntrl.Recognizer(numUnistrokes)


#     def __init__(self):
        
#         self.root = tk.Tk()
#         self.root.title("Group 21")
#         self.canvas = Canvas(self.root, width=350, height=350)
#         self.canvas.pack()
#         self.text_widget = tk.Text(self.root, height=5, width=50)
#         self.text_widget.pack(side="bottom", fill="x") 
#         # button to start the drawing of a gesture and to add the starting point of a gesture to the points array
#         self.canvas.bind("<ButtonPress>", self.mouseclickevent)
#         # button to draw the gesture in a series of continuous points
#         self.canvas.bind("<B1-Motion>", self.draw)
#         # button release to capture/store/process the python main.py points on the canvas on release of the button
#         self.canvas.bind("<ButtonRelease>", self.on_release)
#         self.root.mainloop()


    

    


#     def redraw(self,line_array):
    
#         self.canvas.create_line(self.line_array)
#         # x = event.x
#         # y = event.y
#         # points.append((x, y))

#     def mouseclickevent(self , event):
#         global x, y,points,f
#         if f>1:
#             self.canvas.delete("all")
#             self.text_widget.delete("1.0", END)
#             #canvas.delete(text_widget)
#         f=1 
#         x, y = event.x, event.y
#         points.append((x, y))
        
#     def draw(self,event):
#         global x, y,points,f
#         if f==1:
#             self.canvas.create_line((x, y, event.x, event.y),fill='red',width=4)
#             x = event.x
#             y = event.y
#             points.append((x, y))
#         else:
#             self.canvas.delete("all")
            
        

#     def on_release(self, event):
#         global f,points
#         f=f+1
#         x, y = event.x, event.y
#         points.append((x, y))
#         # print(points)
#         if(len(points) >=10):
            
#             obj=Input()

#         #     rest= obj.rec_ges(points)
#         #     print("***",rest)
#         #     #canvas.create_text(100, 100, text= obj.rec_ges(points))
#         #     result=rest[0]+"("+str(rest[1])+")"
#         #     self.text_widget.insert("1.0", result)
#         # else:
#         #     self.text_widget.insert("1.0", "Very Few points")
        
        
#         points=[] 
        


Input()
    

