import os
from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET


class Folder:

    def __init__(self):
        self.x=XMLfolder()



class XMLfolder:
    # def __init__(self):
    #     # self.mainfolder=[]
    #     # self.subfolders=[]
    #     # self.xmlfiles=[]
    #     # self.gestNames=[]
    #     # self.points=[]

    def parse_folder(self):
        text = os.getcwd()
        
        
        Users = ["s02","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
        SpeedArray=["fast","medium","slow"]
        gestures = ["arrow", "caret" , "check" , "circle" , "delete_mark" , "left_curly_brace" , "pigtail" , "question_mark" , "rectangle" , "right_curly_brace" , "star", "triangle" , "v" , "x"]
        gesturetypenumber=["01","02","03","04","05","06","07","08","09","10"]
        a=[]
        mainfolder=[]
        for i in range(len(Users)):
            # directory = text + '/xml_logs/'+uname+'/medium'
            f=Folder()
            mainfolder.append([Users[i]])
            subfolders=[]
            # speeds=[]

            for j in range(len(SpeedArray)): 
                directory = text + '/xml_logs/'+Users[i]+'/'+SpeedArray[j]

                subfolders.append([SpeedArray[j]])
                gests=[]
                
                for g in range(len(gestures)):
                    gests.append(gestures[g])
                    points=[]

                    hj=0
                    for gnumber in range(len(gesturetypenumber)):
                        str=gestures[g]+gesturetypenumber[gnumber]+'.xml'
                        filepath = os.path.join(directory, str)
                        # print("filepath",filepath)
                        tree = ET.parse(filepath)
                        root = tree.getroot()
                        points1=[]
                        
                        if hj<2:
                            for point in root.findall(".//Point"):
                                x = int(point.attrib["X"])
                                y = int(point.attrib["Y"])
                                points1.append([x, y])
                                hj=hj+1
                            points.append(points1)
                            points1=[]

                    #     # for filename in os.listdir(directory):
                    #     #     # directory.join('/s01/medium/')cd  
                    #     #     if filename.endswith('.xml'):
                    #     #         filepath = os.path.join(directory, filename)
                    #     #         tree = ET.parse(filepath)
                    #     #         root = tree.getroot()
                    #     #         gesname=filepath.replace(directory+"\\","")
                    #     #         ges=gesname[:-6]
                    
                    gests[g].append(points)
                    break
                subfolders[j].append(gests)
                break
            mainfolder[i].append(subfolders)
            
        print(mainfolder[0])

        

                
                
            
            


s=XMLfolder()
s.parse_folder()








    


