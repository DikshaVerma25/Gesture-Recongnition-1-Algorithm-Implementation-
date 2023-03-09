#Group 21
#Jostna Gowda and Diksha Verma
#Part 4 





#Importing all the necessary libraries 
from tkinter import *
import tkinter as tk
import xml.etree.ElementTree as ET
import os
import datetime
import time
import shutil

# Initializing and creating the canvas
root = tk.Tk()
root.title("Group 21")


#These lines of code define the dimensions of a Tkinter Canvas widget and create an instance of it within a Tkinter root window.
canvas_width = 700
canvas_height = 700
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

#These two lines of code create a folder path for storing user-defined gestures.
#this returns the current directory which is stored in current_dir
current_dir=os.getcwd()
#sub-directory is made concatenating the current directory which is stored in folder path
folder_path = current_dir+"/user_gestures"

#code checks if the directory specified by folder_path exists in the current directory.
# If the directory does not exist, os.makedirs() is called to create it.    
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
#If it exists, shutil.rmtree() is called to delete it and all its contents   
else:
    shutil.rmtree(folder_path)

    
# Initializing gesture list and variables
gestures = ["triangle", "x","rectangle", "circle", "check", "caret", "zig-zig", "arrow", "left-square-bracket", "right-square-bracket", "v", "delete", "left-curly-brace", "right-curly-brace", "star", "pigtail"]
current_gesture = gestures[0]
gesture_count = [0] * len(gestures)


#points is an empty list, which will be used to store the (x, y) coordinates of the user's gesture as they draw on the canvas.
points = []
#date is set to today's date, which will be used later in the xml 
date = datetime.date.today()


# Initializing count chart parameters
# count_chart_width = 500
# count_chart_height = 500
# count_chart_margin = 20
# count_chart_bar_width = (count_chart_width - 2 * count_chart_margin) / len(gestures)
# count_chart_x0 = canvas_width - count_chart_width - count_chart_margin
# count_chart_y0 = count_chart_margin

# Function to display the name of the current gesture to be drawn
#The draw_gesture() function deletes any existing "gesture_text" on the canvas and creates a new text in the center of the canvas 
def draw_gesture():
    canvas.delete("gesture_text")
    canvas.create_text(canvas_width // 2, 50, text="Draw a " + current_gesture, font=("Arial", 16), tags="gesture_text")


# Function to handle mouse click events taking event as parameter
def mouseclickevent(event):
    # print("points**********",len(points))

#The x and y variables are assigned the x and y coordinates of the mouse click event.
    global x, y
    x, y = event.x, event.y
    # canvas.create_oval(x, y, event.x,event.y, fill='red', width=4)


# Function to draw lines on the canvas
#draws a line on the canvas between the previous position of the mouse and the current position of the mouse. 
# The x and y global variables are updated to the current position of the mouse
#The gesture_line variable is set to the ID of the line that was just drawn, so that it can be deleted later if necessary.
def draw(event):

    global x, y,points,gesture_line

    gesture_line=canvas.create_line((x, y, event.x, event.y), fill='red', width=4,tag="gesture_line")
    points.append((event.x, event.y))
    x = event.x
    y = event.y

#clears the canvas by deleting the gesture_line tag and resetting the global variable points to an empty list.
def clearPicture():
    global points
    points=[]
    canvas.delete("gesture_line")

# def draw_count_table():
#     global gesture_count
#     table_width = 500
#     table_height = 500
#     table_x0 = canvas_width - table_width - count_chart_margin
#     table_y0 = canvas_height - table_height - count_chart_margin
#     cell_width = table_width // 3
#     cell_height = table_height // (len(gestures) + 1)
#     canvas.create_rectangle(table_x0, table_y0, table_x0 + table_width, table_y0 + table_height, fill="white", tags="count_table")
#     canvas.create_text(table_x0 + cell_width // 2, table_y0 + cell_height // 2, text="Gesture", font=("Arial", 12), tags="count_table")
#     canvas.create_text(table_x0 + cell_width // 2 + cell_width, table_y0 + cell_height // 2, text="Count", font=("Arial", 12), tags="count_table")
#     for i, gesture in enumerate(gestures):
#         canvas.create_text(table_x0 + cell_width // 2, table_y0 + (i + 1) * cell_height + cell_height // 2, text=gesture, font=("Arial", 12), tags="count_table")
#         canvas.create_text(table_x0 + cell_width // 2 + cell_width, table_y0 + (i + 1) * cell_height + cell_height // 2, text=gesture_count[i], font=("Arial", 12), tags="count_table")
#     canvas.create_text(table_x0 + cell_width // 2, table_y0 + (len(gestures) + 1) * cell_height + cell_height // 2, text="Total", font=("Arial", 12), tags="count_table")
#     canvas.create_text(table_x0 + cell_width // 2 + cell_width, table_y0 + (len(gestures) + 1) * cell_height + cell_height // 2, text=sum(gesture_count), font=("Arial", 12), tags="count_table")
    


# Function to draw the count bar chart on the canvas
def draw_count_chart():
    global gesture_count
    canvas.delete("count_chart")
    bar_width = canvas_width // len(gestures)
    bar_height = canvas_height // 15
    # for i, gesture in enumerate(gestures):
    #     count = gesture_count[i]
    #     for j in range(10):
    #         fill_color = "red" if j < count else "white"
        #     canvas.create_rectangle(i * bar_width, canvas_height - (j + 1) * bar_height,
        #                              (i + 1) * bar_width, canvas_height - j * bar_height,
        #                              fill=fill_color, outline="black", tags="count_chart")
        # canvas.create_text((i + 0.5) * bar_width, canvas_height - (10 + 0.5) * bar_height,
        #                     text=gesture + " ({}/{})".format(count, 10), font=("Arial", 12), tags="count_chart")
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");

#If the current gesture being drawn is the first sample for a new gesture, the function calculates the sample number s         
    if (sum(gesture_count)+1)%len(gestures)==1:
        s=gesture_count[0]+1
        canvas.create_text(canvas_width // 2, bar_height // 2, text="Gesture {} / {} {} {}".format(sum(gesture_count)+1, len(gestures) * 10, "Sample No. ", s),
                        font=("Arial", 12), tags="count_chart")

#If the current gesture being drawn is not the first sample for a new gesture, the function creates the same text object as above, but with the sample number being gesture_count[0] instead of s.        
    else:
        canvas.create_text(canvas_width // 2, bar_height // 2, text="Gesture {} / {} {} {}".format(sum(gesture_count)+1, len(gestures) * 10, "Sample No. ", gesture_count[0]),
                        font=("Arial", 12), tags="count_chart")


 
# Function to submit the drawing and update the gesture count and count chart
# Function to submit the drawing and update the gesture count and count chart
        
# def submit():
#     global gesture_count, current_gesture
#     gesture_count[gestures.index(current_gesture)] += 1
#     draw_count_chart()  # Updating the count chart
#     if sum(gesture_count) == len(gestures) * 10:
#         canvas.create_text(canvas_width // 2, canvas_height // 2, text="Thank you for drawing!", font=("Arial", 24))
#     else:
#         # Create new XML file for current gesture
#         gesture_dir = "gesture-" + current_gesture
#         if not os.path.exists(gesture_dir):
#             os.makedirs(gesture_dir)
#         gesture_count_index = gesture_count[gestures.index(current_gesture)]
#         xml_filename = os.path.join(gesture_dir, "{}-{}.xml".format(current_gesture, gesture_count_index))
#         root_element = ET.Element("gesture")
#         # Add points to XML file
#         for point in canvas.find_withtag("line"):
#             x1, y1, x2, y2 = canvas.coords(point)
#             point_element = ET.SubElement(root_element, "point")
#             ET.SubElement(point_element, "x").text = str(x1)
#             ET.SubElement(point_element, "y").text = str(y1)
#         tree = ET.ElementTree(root_element)
#         tree.write(xml_filename)
#         # Update current gesture and display next gesture
#         current_gesture = gestures[(gestures.index(current_gesture) + 1) % len(gestures)]
#         draw_gesture()
#         #gesture.clear()
#         draw_count_chart()
#         #draw_count_table()



def submit():
    # points = []
    global gesture_count, current_gesture
    global points
    #coords = canvas.coords("all")  # get coordinates of all lines drawn
    #gesture_coords = [(x, y) for x, y in coords]
    
#first checks if the number of points in the gesture is greater than 15. 
# If so, it updates the count of the current gesture in the gesture_count list and calls draw_count_chart() function to update the count chart on the canvas. It then deletes all the objects on the canvas 
# and generates a filename for the current gesture and count.    
    if len(points)>15:
        gesture_count[gestures.index(current_gesture)] += 1
        draw_count_chart()  # Updating the count chartf
        canvas.delete("all")
        filename = f"gesture_/{current_gesture}_{gesture_count[gestures.index(current_gesture)]}.xml"
        print("^^^^^^^^^^^^^^^^^^^^^",len(points))
        coords=points
        save_to_xml(coords, filename)
        gesture_coords = []
        points=[]
#the points list is then cleared, and if the sum of all the gesture counts is equal to len(gestures) * 10, a "Thank you for drawing!" message is displayed on the canvas.
#it updates the current gesture to the next one in the list and displays the new gesture name and the updated count chart using the draw_gesture() and draw_count_chart() functions, respectively.        
        if sum(gesture_count) == len(gestures) * 10:
            canvas.create_text(canvas_width // 2, canvas_height // 2, text="Thank you for drawing!", font=("Arial", 12))
        else:
            current_gesture = gestures[(gestures.index(current_gesture) + 1) % len(gestures)]
            draw_gesture()
            draw_count_chart()
            #save_to_xml(points)
            
#This code block is executed if the user draws a gesture with fewer than 16 points. It displays an error message on the canvas for two seconds and then clears the canvas and the points list using the clearPicture() function.            
    else:
        msg= canvas.create_text(canvas_width // 2, canvas_height // 2, text="Oops!! Very Few points .Please redraw the gesture", font=("Arial", 12))
        for i in range(2, 0, -1):
            canvas.itemconfigure(msg, text="Less Points. Please redraw in "+str(i)+" seconds")
            canvas.update()
            time.sleep(1)
        canvas.delete(msg)
        clearPicture()

    gesture_line=None
        

# def clear_text_item(msg):
#     canvas.itemconfig(msg, text="")   
 
#This function is responsible for saving the gesture data to an XML file taking two parameters which are the coordinate and the filename 
def save_to_xml(coords, filename):
    global current_gesture, gesture_count
#checks if a folder named "user_gestures" exists in the current directory. If it doesn't, it creates one    
    current_dir=os.getcwd()
    folder_path = current_dir+"/user_gestures"
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = f"{current_gesture}_{gesture_count[gestures.index(current_gesture)]}.xml"
    file_path = os.path.join(folder_path, file_name)

#creates xml folder named as "Gesture" with different attributes described 
#sets the "Name" attribute again to current_gesture and the "ID" attribute to the count of the current gesture in gesture_count
    root = ET.Element("Gesture", {"Name": file_name, "Subject": "1", "Instance": "1", "NumPts": str(len(coords)), "AppName": "Gestures", "Date": date.today().strftime("%A, %B %d, %Y"), "TimeOfDay": time.strftime("%H:%M:%S")})

    root.set("Name", current_gesture)
    root.set("ID", str(gesture_count[gestures.index(current_gesture)]))
    
#for each x, y coordinate pair in the coords list, an Element object named Point is created with attributes X, Y, and T set to str(x), str(y), and "0", respectively. The Point element is added as a child of the Gesture element.
    for x, y in coords:
        point = ET.SubElement(root, "Point", X=str(x), Y=str(y), T=str(int(time.time()*1000)))
        # point = ET.SubElement(root, "Point")
        # point.set("X", str(x))
        # point.set("Y", str(y))

    xml_file = ET.ElementTree(root)
    xml_file.write(folder_path+"/{}_{}.xml".format(current_gesture, gesture_count[gestures.index(current_gesture)]))
    tree = ET.ElementTree(root)
    tree.write(file_path)

# def save_to_xml(coords, filename):
#     global current_gesture, gesture_count

#     folder_path = "gesture-user"

#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
    
#     file_path = os.path.join(folder_path, filename)

#     # root = ET.Element("Gesture", {"Name": current_gesture, "Subject": "1", "Number": "1", "NumPts": str(len(coords)), "Millseconds": "0", "AppName": "Gestures", "AppVer": "1.0", "Date": date.today().strftime("%A, %B %d, %Y"), "TimeOfDay": time.strftime("%H:%M:%S")})

#     # root.set("ID", str(gesture_count[gestures.index(current_gesture)]))
    
#     root = ET.Element("Gesture", {"Name": filename, "Subject": "1", "Number": "1", "NumPts": str(len(coords)), "Millseconds": "0", "AppName": "Gestures", "AppVer": "1.0", "Date": date.today().strftime("%A, %B %d, %Y"), "TimeOfDay": time.strftime("%H:%M:%S")})

#     root.set("Name", current_gesture)
#     root.set("ID", str(gesture_count[gestures.index(current_gesture)]))

#     for x, y in coords:
#         point = ET.SubElement(root, "Point", X=str(x), Y=str(y), T="0")

#     xml_file = ET.ElementTree(root)
#     xml_file.write(os.path.join(folder_path, filename))



# Adding the Erase button
# lambda: canvas.delete("gesture_line")
erase_button = Button(root, text="Erase", command=clearPicture)
erase_button.pack()
# Adding the Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()


draw_gesture()  # Displaying the name of the first gesture to be drawn

canvas.bind("<Button-1>", mouseclickevent)

canvas.bind("<B1-Motion>", draw)

root.mainloop()
