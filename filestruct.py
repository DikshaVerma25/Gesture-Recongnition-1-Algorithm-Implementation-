import os
from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET






class XMLfolder:
    xmlfiles=[]
    def __init__(self):
        self.xmlfiles=self.parse_folder()
        print(self.xmlfiles[0][0][0][0])

   
    def parse_folder(self):
        text = os.getcwd()
        
        
        Users = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
        SpeedArray=["fast","medium","slow"]
        gestures = ["arrow", "caret" , "check" , "circle" , "delete_mark" , "left_curly_brace" ,"left_sq_bracket", "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" ,"right_sq_bracket", "star", "triangle" , "v" , "x"]
        gesturetypenumber=["01","02","03","04","05","06","07","08","09","10"]
        
        xmlfiles=[]
        
        for i in range(len(Users)):
            q=[]
            for j in range(len(SpeedArray)): 
                directory = text + '/xml_logs/'+Users[i]+'/'+SpeedArray[j]

                p=[]
                for g in range(len(gestures)):
                    # Gestures.append(gestures[g])
                    # Seasons[i][j].append(gestures[g])
                    pointsarray=[]
                    for gnumber in range(len(gesturetypenumber)):
                        str=gestures[g]+gesturetypenumber[gnumber]+'.xml'
                        filepath = os.path.join(directory, str)
                        # print("filepath",filepath)
                        tree = ET.parse(filepath)
                        root = tree.getroot()
                        points1=[]
                    
                    
                        for point in root.findall(".//Point"):
                            x = int(point.attrib["X"])
                            y = int(point.attrib["Y"])
                            points1.append([x, y])
                        
                        pointsarray.append(points1) 
                           
                    p.append(pointsarray)
                    
                q.append(p)
                
            
            xmlfiles.append(q)
        return xmlfiles
                        
XMLfolder()








    


