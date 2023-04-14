from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math
import xml.etree.ElementTree as ET
import os
import filestructUser as filest
import random
import copy
import csv
text = os.getcwd()
# hj=0
data = []
obj=filest.XMLfolder()
# Template points will be stored in UNISTROKE variable
# List of List is being used to store the template points
data=filest.XMLfolder().data
OriginalData = copy.deepcopy(data)

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'output.csv')
    

# #def write_data_to_csv(csv_file_path, data):
# with open(csv_path, mode='a', newline='') as csv_file:
#     global writer 
#     writer = csv.writer(csv_file)
#     #csv_file.truncate(0) 
#     writer.writerow(["Recognition Log: Jotsna Gowda & Diksha Verma", "$1 Algorithm"])
#     writer.writerow(["User[all-users]", "GestureType[all-gestures-types]", "RandomIteration[1to100]", "#ofTrainingExamples[E]", "TrainingSetSize[count]", "TrainingSetContents[specific-gesture-instances]",
#                     "Candidate[specific-instance]", "RecoResultGestureType[what-was-recognized]", "Correct/Incorrect[1or0]", "RecoResultScore", "RecoResultBestMatch[specific-instance]",
#                     "RecoResultNBestSorted"])
    #writer.writerow(data)
 
       
# print("&&&&&& ",len(xmlfiles),len(xmlfiles[0]),len(xmlfiles[0][0]),len(xmlfiles[0][0][0][0]),xmlfiles[0][0][0][0])

# current_dir = os.path.dirname(__file__)

# # Construct the path to the CSV file using the current directory
# csv_path = os.path.join(current_dir, 'output.csv')


# data_2 = [ 'Recognition Log: Jotsna Gowda, Diksha Verma // $1 Algorithm //  // USER-DEPENDENT RANDOM-1']
# data_3 = ['User[all-users],GestureType[all-gestures-types],RandomIteration[1to100],#ofTrainingExamples[E],TotalSizeOfTrainingSet[count],TrainingSetContents[specific-gesture-instances],Candidate[specific-instance],RecoResultGestureType[what-was-recognized],CorrectIncorrect[1or0],RecoResultScore,RecoResultBestMatch[specific-instance],RecoResultNBestSorted[instance-and-score]']
# write_data_to_csv(csv_path, data_2)
# write_data_to_csv(csv_path, data_3)


#write_data_to_csv(csv_path, data_3)


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
    
    def __init__(self, pointsd, flag=True):
        self.pointse = pointsd
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
        points = self.pointse
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
        self.pointse = new_points
        return self.pointse


#The length of the path of gesture is calculated using this method
# the distance between two adajcent points is calculated and added to the total distance d to get the path length
    def path_length(self):
        d = 0
        for i in range(1, len(self.pointse)):
            d += distance(self.pointse[i - 1], self.pointse[i])
        return d
# this will calculate the centroid and compute the angle with respect to the X axis and the centroid line between c(x,y)and points(x,y)
    def indicative_angle(self):
        # angle formed by (points[0], centroid) and the horizon
        c = self.centroid()
        return atan2(c[1] - self.pointse[0][1], c[0] - self.pointse[0][0])


    def centroid(self):
        n = len(self.pointse)
        return (
            sum([p[0] / n for p in self.pointse]),
            sum([p[1] / n for p in self.pointse])
        )


#This function is rotating the gesture to its centroid whose points are provided by a different function
# Here it uses the cosine and sine values of radian angle for rotating which are then stored in a new_points array 
# It will rotate te x axis point counter clockwise and rotate the Y coordinate clockwise to get a best fit using the indicative angle returned
# vetween the centroid line and the x axis
    def rotateTo(self, angle):
        c = self.centroid()
        new_points = []
        for p in self.pointse:
            dx, dy = p[0] - c[0], p[1] - c[1]
            new_points.append((
                dx * cos(angle) - dy * sin(angle) + c[0],
                dx * sin(angle) + dy * cos(angle) + c[1]
            ))
        self.pointse = new_points



#This function helps to scale the gesture to a bounding box.
#It takes one inputs and then calls the BoundingBox function which returns points of new rectangle
#After creating new array it  creates new coordinates by multiplying original to scaling factor
#Scaling factor is desire size (in this case is square size by width and height of bounding box)
    def scale_to(self, size):
        B = self.bounding_box()
        new_points = []
        for p in self.pointse:
            new_points.append((
                p[0] * size / B[0],
                p[1] * size / B[1]
            ))
        self.pointse = new_points

    
 #Bounding Box is smallest rectangle that will enclose the gesture where array points is passed as parameter
 # after initializing all the required variables it loopsthrough all the points resulting in the dimensions os the
 # smallest rectangle by substracting the min values to max     
    def bounding_box(self):
        minX, maxX = inf, -inf
        minY, maxY = inf, -inf
        for point in self.pointse:
            minX, maxX = min(minX, point[0]), max(maxX, point[0])
            minY, maxY = min(minY, point[1]), max(maxY, point[1])
        return (maxX - minX, maxY - minY)

#recentering the gesture by aligning its centroid to  the origin
    def translate_to(self, target):
        c = self.centroid()
        new_points = []
        for p in self.pointse:
            new_points.append((
                p[0] + target[0] - c[0],
                p[1] + target[1] - c[1]
            ))
        self.pointse = new_points

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
        r_angle = Gesture(self.pointse, False)
        r_angle.rotateTo(angle)
        return r_angle.path_distance(T)

    def path_distance(self,templatepoints):
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(self.points))
        if len(templatepoints)>64:
            print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",templatepoints)
        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",len(points))

        n = len(templatepoints)
        #print("###########################################################################",n)
        return sum([distance(self.pointse[i], templatepoints[i]) / n for i in range(n)])


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
        global writer
        # 6
        numUsers=len(data)
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",numUsers)
        # 10
        numForEachGesture=len(data[1][1][1][1])
        # 16
        numGestures=len(data[1][1])
        # print("******************",numGestures)

        # print("&&&&&&&&&&&&&&&&&&&",numForEachGesture)
        c=0
        cn=0
        Speed=1
        # looping through each user
        for user in range(numUsers):
            # for speed in range(numSpeed):
            # looping through eachof th e16 differentgestrues
            for gesture in range(numGestures):
                # looping to 10 different gestures for each gesture type
                for t in range(numForEachGesture):
                    # Preprocessing the gesture points and storing all the preprocessed points in the data
                    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",data[user][1][Speed][1][gesture][1][t])
                    d=data[user][1][gesture][1][t]
                    arr=Gesture(d)
                    data[user][1][gesture][1][t]=arr.pointse
                    if len(arr.pointse)==64:
                        c=c+1
                    else:
                        cn=cn+1
        #def write_data_to_csv(csv_file_path, data):
        with open(csv_path, mode='a', newline='') as csv_file:
            global writer 
            writer = csv.writer(csv_file)
            csv_file.truncate(0) 
            writer.writerow(["Recognition Log: Jotsna Gowda & Diksha Verma", "$1 Algorithm"])
            writer.writerow(["User[all-users]", "GestureType[all-gestures-types]", "RandomIteration[1to100]", "#ofTrainingExamples[E]", "TrainingSetSize[count]", "TrainingSetContents[specific-gesture-instances]",
                            "Candidate[specific-instance]", "RecoResultGestureType[what-was-recognized]", "Correct/Incorrect[1or0]", "RecoResultScore", "RecoResultBestMatch[specific-instance]",
                            "RecoResultNBestSorted"])
            per_user_accuracy =[]
            
            
            total_count = 0
            rec_count = 0
            uc=0
            ut=0 
            in_count =0
            Array_er=[]
        # random 100 loop can be used here
            for user in range(numUsers):
                error = []
                Ep = [ ]
                
                
               
               
                
            # for speed in range(numSpeed):
                #for gesture in range(numGestures):
                    #candidateList.append((data[user][1][Speed][1][gesture][0],data[user][1][Speed][1][gesture][1][r]))
                    #cdname.append(data[user][1][Speed][1][gesture][0])
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@@",cdname)

                for E in range(1,10):
                    tt=0
                    inc_c =0
                    
                    recoscore=0
                    for i in range(10):
                        TemplatesList=[]
                        candidateList=[]
                        templatename=[]
                        CandidateNames=[]
                        cdname=[]
                        trainingsetcontents=""
                        candidate_num_list = {}
                        for gesture in range(numGestures):
                            # storing an array of random numbers from the list betweeen 1,11
                            templatenumbers=random.sample(range(0,10),E)
                            # print("templatenumbers******",templatenumbers)
                            # storing the random number except for the numbers selected in templagtenumbers array
                            candidatenumbers=random.sample(list(set([i for i in range(0,10)]) - set(templatenumbers)), 1)[0]
                            # print("&&&&&&&&",candidatenumbers)
                            # creating a random list of templates for each type
                            for num in templatenumbers:
                                # gesture name,user name,templatetype number,data points
                                TemplatesList.append((data[user][1][gesture][0],data[user][0],num,data[user][1][gesture][1][num]))
                                templatename.append(data[user][1][gesture][0]+'0'+str(num))
                                #trainingsetcontents = trainingsetcontents+"{}-{}-{}:::".format(user, data[user][1][Speed][1][gesture][0], num)
                                trainingsetcontents += "{}-{}-{}".format( data[user][0],data[user][1][gesture][0],num)
                            
                            candidatel=(data[user][1][gesture][0],data[user][0],candidatenumbers,data[user][1][gesture][1][candidatenumbers])
                            #candidate_num_list[candidatel]=candidatenumbers
                            # creating a list of candidates
                            candidateList.append(candidatel)
                            CandidateNames.append(data[user][1][gesture][0]+'0'+str(candidatenumbers))
                            # print("TemplatesList@@@@@@@@@@@@@@@@@",len(templatename) )
                            # print("CandidateList^^^^^^^^^^^^^^^^^",len(CandidateNames))
                        # adding each template tostore it in the global variable
                        for template in TemplatesList:
                            obj.addGesture(template) 
                        # looping through each candidate and calling the recognition function
                        for candidate in candidateList:
                            #candidate_num = candidate_num_list[candidate]
                            log =[]
                            total_count += 1
                            tt += 1 
                            # result will be a tuple of gest type,score,user,num
                            result=self.rec_ges(candidate[3],TemplatesList)
                            #print("result####################################################################### ",result,candidate[0])
                            user_s = data[user][0]
                            ges_name = candidate[0]
                            i_no = i
                            train_exp = E
                            total_size = E * 16
                            candidate_log = "{}-{}-{}::::".format( candidate[1],ges_name ,candidate[2])
                            rec_ges_name = result[0]
                            rec_check = 0
                            rec_score = result[1]
                            rec_best_match = "{}-{}-{}::::".format( result[2],result[0], result[3])
                            # print("**************************", ges_name)
                            n_best_list = ""
                            for nb in result[4]:
                                #print("nb !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",nb)
                                n_best_list += "{}-{}-{}-{}::::".format(nb[2], nb[0], nb[3], nb[1])
                            
                            if  rec_ges_name ==   ges_name:
                                ut+=1
                                uc+=1
                                rec_check = 1
                                rec_count += 1
                                inc_c += 1
                                
                            else:
                                ut+=1
                                
                                
                            log.append(user_s)
                            log.append(ges_name)
                            log.append(i_no)
                            log.append(train_exp)
                            log.append(total_size)
                            log.append(trainingsetcontents)
                            log.append(candidate_log)
                            log.append(rec_best_match)
                            log.append(rec_check)
                            log.append(rec_score)  
                            log.append(rec_best_match)
                            log.append(n_best_list)  
                            writer.writerow(log)
                    err = inc_c / tt
                    error.append(err) 
                    Ep.append(E)
                Array_er.append(error)         
                            
            #     average_acc= uc/ut *100
            #     per_user_accuracy.append((average_acc, data[user][0]))
            #     #print("zzzzzzzzzzzzzzzzzz", average_acc, user)
            #     print(per_user_accuracy)
            avg_accuracy = rec_count /total_count
            print("pppppppppppppppppppppppppppppppppppppp", avg_accuracy,user)
            test =[]
            
            print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", total_count)
            test.append("Total avg. accuracy:")
            test.append(avg_accuracy)
            writer.writerow(test)
            print(Array_er)                    

            #     for gesture in range(numGestures):
            #         TemplatesList.append((data[user][1][Speed][1][gesture][0],data[user][1][Speed][1][gesture][1][r]))
            #         templatename.append(data[user][1][Speed][1][gesture][0])
                
            #     for candidate in candidateList:
            #         result=self.rec_ges(candidate[1],TemplatesList)
            #         print("result####################################################################### ",result,candidate[0])
            #         cg=cg+1
            #         if result[0]==candidate[0]:
            #             recoscore=recoscore+1

            # avg_rec_user=recoscore/10
            # print("avg_rec_score&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ",avg_rec_user,cg,recoscore)
        
            # data_1 = [user, ges_name, i, E, len(Templates3), "{}" ]
            # write_data_to_csv(csv_path, data_1)
    
                    





                
            
                    
                
            

                




                
             

            # for t in range(numForEachGesture):
            #     for f in range(2):
            #         Templates1=[]
            #         Templatesiszearr=[]
            #         for gesture in range(numGestures):

            #             # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",data[user][1][Speed][1][gesture][1][t])
            #             # arr=Gesture(data[user][1][Speed][1][gesture][1][t])
            #             # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",len(arr.points))
            #             # data[user][1][1][1][gesture][1][t]=arr.points
            #             # na= candidate gesture name, cd=candidate points
            #             # cd,na=data[user][1][Speed][1][gesture][1][r],data[user][1][Speed][1][gesture][0]
            #             candidatename=data[user][1][Speed][1][gesture][0]
            #             ct=data[user][1][Speed][1][gesture][1][r]
            #             cd.append((candidatename,ct))
            #             # print("*******************************",data[user][1][Speed][1][gesture][0])
            #             if r!=t:
            #                 dt=data[user][1][Speed][1][gesture][1][t]
            #                 templateName=data[user][1][Speed][1][gesture][0]
            #                 Templatesiszearr.append(len(dt))
            #                 Templates1.append((templateName,dt))
            #         print("cadidtae array length ############## ",len(cd))  
            #         h=0
            #         for candidate in cd:
            #             [print("inside candidate loop******=====",len(temp[1])) for temp in Templates1]
            #             if h>3:
            #                 break
            #             result=self.rec_ges(candidate[1],Templates1)

            #             print("result####################################################################### ",result)
            #             h=h+1
                        

            #         # [print("Raja=====",len(temp[1])) for temp in Templates1]
            #         # for g in range(numGestures):
            #         #     cd,na=data[user][1][Speed][1][g][1][r],data[user][1][Speed][1][g][0]
            #         #     result=self.rec_ges(cd,Templates1) 
            #         #     print("result####################################################################### ",result,na)
            #     Templates1=  []
            #     cd=[]
            # Templates1=  []
            # cd=[]




                
                

                    
                        
                   
               
        

 
                
    
                            





       
    


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
        #print("CopyTmplay Before==", len(copyTemplate))
        #print("Josh LEMN===",len(Templates2))
        #[print("JOSH=====",len(temp[1])) for temp in Templates2]
        ges = Gesture(points,False)
        #[print("JOSH22=====",len(temp[1])) for temp in copyTemplate]
        print("CopyTmplay==", len(copyTemplate))
        b = inf
        result = ''
        resultuser = ''
        resultnum =-1
        k=[]
        for template_stroke in copyTemplate:
            # returns the distance between candidate points and the template points after preprocessing
            # if len(template_stroke[1])>64:
            #     print("****************************************************************",template_stroke[0])
            # else:
            #print("JOSH1===",len(template_stroke[1]))
            #[print("JOSH222222=====",len(temp[1]),end='') for temp in Templates2]
            #print()
            d = ges.distance_at_best_angle(template_stroke[3])

            # calculates the minimum distance and store the template name with the minimum distance to recognize the gesture
            result1 = template_stroke[0]
            # k array will store the n best list
            k.append((result1,1.0 - d / HalfDiagonal,template_stroke[1],template_stroke[2]))

            if d < b:
                # update the pt2 best gesture
                b = d
                result = template_stroke[0]
                resultuser=template_stroke[1]
                resultnum=template_stroke[2]


        #k.append((result,1.0 - b / HalfDiagonal,resultuser,resultnum))
      
        v=sorted(k, key = lambda x: x[1], reverse= True)
        if len(v) >50:
            v = v[:50]
        print("v @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",v[0][1]) 

        return (result,1.0 - b / HalfDiagonal,resultuser,resultnum ,v)


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
    

