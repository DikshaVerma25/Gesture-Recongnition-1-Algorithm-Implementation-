import os
from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET
import glob
import xml.etree.ElementTree as ET
StoredTemplates=[]
OriginalNumbers=["1","2","3","4","5","6","7","8","9","10"]

class XMLfolder:
    def __init__(self):
        # self.xmlfiles=
        self.data=self.parse_folder()
       
        # print(self.xmlfiles[0][0][0][0])

    def addGesture(self,template):
        StoredTemplates.append(template)
   
# function to parse the xml logs folder and return the data from the xmlogs
    def parse_folder(self):
        # get the current directory
        text = os.getcwd()
        folder_path = text + '/xml_newUser'
        # data=[]

        # Get a list of folders inside the parent folder
        folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        # print(folders)
        # Loop through the folders and print their names
        xmlFolder_array=[]
        # loop through the users
        for folder in folders:
            filepath=folder_path+'/'+folder
            # print("filepath****",filepath)
            # subfolders = [f for f in os.listdir(folder_pathi) if os.path.isdir(os.path.join(folder_pathi, f))]
            pacfolders=[]
            # subfolder_array=[]
     # iterate through the subfolders which will contain  the pace of the gesture(fast,medium,slow)

            # filepath = os.path.join(folder_pathi, subfolder)
            # print(filepath)
            xmlfiles=glob.glob(filepath+'/*.xml')
            gestureNamesList=[]
            pointsarray=[]
            OriginalGesturesList=set()
            # OriginalNumbers=set()
            # from the xml files,get the set of gestures array and set of numbers 
            for xml_file in xmlfiles:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                # get the gesture Name from the file
                gesture_Name=root.get('Name')
                # OriginalNumbers.add(gesture_Name[-2]+gesture_Name[-1])
                OriginalGesturesList.add(gesture_Name)
            # print(OriginalGesturesList)
            Gesture_Array=[]
            OriginalGesturesArray=list(OriginalGesturesList)
            OriginalNumbersArray=OriginalNumbers
            # loop through each of the 16  gestures stored in the Original Getsures Array
            for g in range(len(OriginalGesturesArray)):
                pointsarray=[]
                # loop through each of the numbers in the Numbersarray(1,10)
                for t in range(len(OriginalNumbersArray)):
                    str=OriginalGesturesArray[g]+"_"+OriginalNumbersArray[t]+'.xml'
                    # get the xml file using the above string eg,(Arrow02,Caret03)
                    xmlpath = os.path.join(filepath, str)
                    tree = ET.parse(xmlpath)
                    root = tree.getroot()
                    points=[]
                    # get the points from the xml file
                    for point in root.findall(".//Point"):
                        x = int(point.attrib["X"])
                        y = int(point.attrib["Y"])
                        points.append([x, y])
                    # Add the points to points array for each number in original numbers array
                    pointsarray.append(points)
                # Add the points array to each of the 16 gestures
                Gesture_Array.append((OriginalGesturesArray[g],pointsarray))
            # Add the gestures array which consists of 16 getsures and all the points for eachof those 16 gesstures to th esubfolder array
            xmlFolder_array.append((folder,Gesture_Array))
        print(len(xmlFolder_array)  )  
        # (user1/user2/user3)/array/ gesture1 or gestur e2
        # print("***",xmlFolder_array[0][1][1])
        # print("***",xmlFolder_array[2][1][2])
        # arrow
        # print("***",xmlFolder_array[3][1][2][0])
        # print("***",xmlFolder_array[3][1][2][1])
        # 5th bracket for choose 1 of the 16 gestures[points array]
        # print("***",len(xmlFolder_array[3][1][2][1][0]))
        

        # 10
        # print("***",len(xmlFolder_array[1][1][1][1]))

        # 16
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",len(xmlFolder_array[1][1]))
        # print("################################",xmlFolder_array[1][1][1][0],xmlFolder_array[1][0])
        # print(xmlFolder_array[1][1][1][1][1])


        return xmlFolder_array




        # print("***",len(xmlFolder_array[1][1][5]))
        # # will give so2/medium/gestures/a particular gesture/ [points array]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][4][0])
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][3][0])
        # # will give s02/medium's/[all gestures and data]=>output [medium[]]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1])

        # # will give [folders array(so1s,so2,so3...)]/so2/[Pace array]/medium/[diff gestures]/ 4th gesture / [pointsarray]/pointarray[0]
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",xmlFolder_array[1][1][1][1][4][1][0])
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",len(xmlFolder_array[0][0]),xmlFolder_array[1][1][1][0],len(xmlFolder_array[1][0]),len(xmlFolder_array[1][1][1][1]),len(xmlFolder_array[1][1][1][1][1][1]))
        import json

        with open('output.txt', 'w') as filehandle:
            json.dump(xmlFolder_array, filehandle)
        # return xmlFolder_array



        # import json

        # with open('output.txt', 'w') as filehandle:
        #     json.dump(xmlFolder_array, filehandle)

                    



                

                
               


                    




                    

                





            
                                
XMLfolder()








    


