import os
from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET
import glob
import xml.etree.ElementTree as ET







class XMLfolder:
   
    def __init__(self):
        # self.xmlfiles=
        self.data=self.parse_folder()
        # print(self.xmlfiles[0][0][0][0])

   

    def parse_folder(self):
        text = os.getcwd()
        folder_path = text + '/xml_logs'
        # data=[]

        # Get a list of folders inside the parent folder
        folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

        # Loop through the folders and print their names
        xmlFolder_array=[]
        for folder in folders:
            folder_pathi=folder_path+'/'+folder
            subfolders = [f for f in os.listdir(folder_pathi) if os.path.isdir(os.path.join(folder_pathi, f))]
            pacfolders=[]
            subfolder_array=[]
            for subfolder in subfolders:
                filepath = os.path.join(folder_pathi, subfolder)
                # print(filepath)
                xmlfiles=glob.glob(filepath+'/*.xml')
                gestureNamesList=[]
                pointsarray=[]
                OriginalGesturesList=set()
                OriginalNumbers=set()
                for xml_file in xmlfiles:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    # get the gesture Name from the file
                    gesture_Name=root.get('Name')
                    OriginalNumbers.add(gesture_Name[-2]+gesture_Name[-1])
                    OriginalGesturesList.add(gesture_Name[:-2])
                # print(OriginalGesturesList)
                Gesture_Array=[]
                OriginalGesturesArray=list(OriginalGesturesList)
                OriginalNumbersArray=list(OriginalNumbers)
                for g in range(len(OriginalGesturesArray)):
                    pointsarray=[]
                    for t in range(len(OriginalNumbersArray)):
                        str=OriginalGesturesArray[g]+OriginalNumbersArray[t]+'.xml'
                        xmlpath = os.path.join(filepath, str)
                        tree = ET.parse(xmlpath)
                        root = tree.getroot()
                        points=[]
                        for point in root.findall(".//Point"):
                            x = int(point.attrib["X"])
                            y = int(point.attrib["Y"])
                            points.append([x, y])
                        pointsarray.append(points)
                    Gesture_Array.append((OriginalGesturesArray[g],pointsarray))
                subfolder_array.append((subfolder,Gesture_Array))
            xmlFolder_array.append((folder,subfolder_array))
        
        # # will give so2/medium/gestures/a particular gesture/ [points array]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][4][0])
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][3][0])
        # # will give s02/medium's/[all gestures and data]=>output [medium[]]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1])

        # # will give [folders array(so1,so2,so3...)]/so2/[Pace array]/medium/[diff gestures]/ 4th gesture / [pointsarray]/pointarray[0]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][4][1][0])
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",len(xmlFolder_array[0][0]),xmlFolder_array[1][1][1][0],len(xmlFolder_array[1][0]),len(xmlFolder_array[1][1][1][1]),len(xmlFolder_array[1][1][1][1][1][1]))

        return xmlFolder_array



        import json

        with open('output.txt', 'w') as filehandle:
            json.dump(xmlFolder_array, filehandle)

                    



                

                
               


                    




                    

                





            
                                
XMLfolder()








    


