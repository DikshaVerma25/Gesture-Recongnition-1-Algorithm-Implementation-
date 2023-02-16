from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf


# Template points will be stored in UNISTROKE variable
# List of List is being used to store the template points
UNISTROKES = [("triangle", [[137, 139],[135, 141],[133, 144],[132, 146],[130, 149],[128, 151],[126, 155],[123, 160],[120, 166],[116, 171],[112, 177],[107, 183],[102, 188],[100, 191],[95, 195],[90, 199],[86, 203],[82, 206],[80, 209],[75, 213],[73, 213],[70, 216],[67, 219],[64, 221],[61, 223],[60, 225],[62, 226],[65, 225],[67, 226],[74, 226],[77, 227],[85, 229],[91, 230],[99, 231],[108, 232],[116, 233],[125, 233],[134, 234],[145, 233],[153, 232],[160, 233],[170, 234],[177, 235],[179, 236],[186, 237],[193, 238],[198, 239],[200, 237],[202, 239],[204, 238],[206, 234],[205, 230],[202, 222],[197, 216],[192, 207],[186, 198],[179, 189],[174, 183],[170, 178],[164, 171],[161, 168],[154, 160],[148, 155],[143, 150],[138, 148],[136, 148]]),("x", [[87, 142],[89, 145],[91, 148],[93, 151],[96, 155],[98, 157],[100, 160],[102, 162],[106, 167],[108, 169],[110, 171],[115, 177],[119, 183],[123, 189],[127, 193],[129, 196],[133, 200],[137, 206],[140, 209],[143, 212],[146, 215],[151, 220],[153, 222],[155, 223],[157, 225],[158, 223],[157, 218],[155, 211],[154, 208],[152, 200],[150, 189],[148, 179],[147, 170],[147, 158],[147, 148],[147, 141],[147, 136],[144, 135],[142, 137],[140, 139],[135, 145],[131, 152],[124, 163],[116, 177],[108, 191],[100, 206],[94, 217],[91, 222],[89, 225],[87, 226],[87, 224]]),
("rectangle", [[78, 149],[78, 153],[78, 157],[78, 160],[79, 162],[79, 164],[79, 167],[79, 169],[79, 173],[79, 178],[79, 183],[80, 189],[80, 193],[80, 198],[80, 202],[81, 208],[81, 210],[81, 216],[82, 222],[82, 224],[82, 227],[83, 229],[83, 231],[85, 230],[88, 232],[90, 233],[92, 232],[94, 233],[99, 232],[102, 233],[106, 233],[109, 234],[117, 235],[123, 236],[126, 236],[135, 237],[142, 238],[145, 238],[152, 238],[154, 239],[165, 238],[174, 237],[179, 236],[186, 235],[191, 235],[195, 233],[197, 233],[200, 233],[201, 235],[201, 233],[199, 231],[198, 226],[198, 220],[196, 207],[195, 195],[195, 181],[195, 173],[195, 163],[194, 155],[192, 145],[192, 143],[192, 138],[191, 135],[191, 133],[191, 130],[190, 128],[188, 129],[186, 129],[181, 132],[173, 131],[162, 131],[151, 132],[149, 132],[138, 132],[136, 132],[122, 131],[120, 131],[109, 130],[107, 130],[90, 132],[81, 133],[76, 133]]),
("circle", [[127, 141],[124, 140],[120, 139],[118, 139],[116, 139],[111, 140],[109, 141],[104, 144],[100, 147],[96, 152],[93, 157],[90, 163],[87, 169],[85, 175],[83, 181],[82, 190],[82, 195],[83, 200],[84, 205],[88, 213],[91, 216],[96, 219],[103, 222],[108, 224],[111, 224],[120, 224],[133, 223],[142, 222],[152, 218],[160, 214],[167, 210],[173, 204],[178, 198],[179, 196],[182, 188],[182, 177],[178, 167],[170, 150],[163, 138],[152, 130],[143, 129],[140, 131],[129, 136],[126, 139]]),
("check", [[91, 185],[93, 185],[95, 185],[97, 185],[100, 188],[102, 189],[104, 190],[106, 193],[108, 195],[110, 198],[112, 201],[114, 204],[115, 207],[117, 210],[118, 212],[120, 214],[121, 217],[122, 219],[123, 222],[124, 224],[126, 226],[127, 229],[129, 231],[130, 233],[129, 231],[129, 228],[129, 226],[129, 224],[129, 221],[129, 218],[129, 212],[129, 208],[130, 198],[132, 189],[134, 182],[137, 173],[143, 164],[147, 157],[151, 151],[155, 144],[161, 137],[165, 131],[171, 122],[174, 118],[176, 114],[177, 112],[177, 114],[175, 116],[173, 118]]),
("caret", [[79, 245],[79, 242],[79, 239],[80, 237],[80, 234],[81, 232],[82, 230],[84, 224],[86, 220],[86, 218],[87, 216],[88, 213],[90, 207],[91, 202],[92, 200],[93, 194],[94, 192],[96, 189],[97, 186],[100, 179],[102, 173],[105, 165],[107, 160],[109, 158],[112, 151],[115, 144],[117, 139],[119, 136],[119, 134],[120, 132],[121, 129],[122, 127],[124, 125],[126, 124],[129, 125],[131, 127],[132, 130],[136, 139],[141, 154],[145, 166],[151, 182],[156, 193],[157, 196],[161, 209],[162, 211],[167, 223],[169, 229],[170, 231],[173, 237],[176, 242],[177, 244],[179, 250],[181, 255],[182, 257]]),
("arrow", [[68, 222],[70, 220],[73, 218],[75, 217],[77, 215],[80, 213],[82, 212],[84, 210],[87, 209],[89, 208],[92, 206],[95, 204],[101, 201],[106, 198],[112, 194],[118, 191],[124, 187],[127, 186],[132, 183],[138, 181],[141, 180],[146, 178],[154, 173],[159, 171],[161, 170],[166, 167],[168, 167],[171, 166],[174, 164],[177, 162],[180, 160],[182, 158],[183, 156],[181, 154],[178, 153],[171, 153],[164, 153],[160, 153],[150, 154],[147, 155],[141, 157],[137, 158],[135, 158],[137, 158],[140, 157],[143, 156],[151, 154],[160, 152],[170, 149],[179, 147],[185, 145],[192, 144],[196, 144],[198, 144],[200, 144],[201, 147],[199, 149],[194, 157],[191, 160],[186, 167],[180, 176],[177, 179],[171, 187],[169, 189],[165, 194],[164, 196]]),
("zig-zag", [[307, 216],[333, 186],[356, 215],[375, 186],[399, 216],[418, 186]]),
("left bracket", [[140, 124],[138, 123],[135, 122],[133, 123],[130, 123],[128, 124],[125, 125],[122, 124],[120, 124],[118, 124],[116, 125],[113, 125],[111, 125],[108, 124],[106, 125],[104, 125],[102, 124],[100, 123],[98, 123],[95, 124],[93, 123],[90, 124],[88, 124],[85, 125],[83, 126],[81, 127],[81, 129],[82, 131],[82, 134],[83, 138],[84, 141],[84, 144],[85, 148],[85, 151],[86, 156],[86, 160],[86, 164],[86, 168],[87, 171],[87, 175],[87, 179],[87, 182],[87, 186],[88, 188],[88, 195],[88, 198],[88, 201],[88, 207],[89, 211],[89, 213],[89, 217],[89, 222],[88, 225],[88, 229],[88, 231],[88, 233],[88, 235],[89, 237],[89, 240],[89, 242],[91, 241],[94, 241],[96, 240],[98, 239],[105, 240],[109, 240],[113, 239],[116, 240],[121, 239],[130, 240],[136, 237],[139, 237],[144, 238],[151, 237],[157, 236],[159, 237]]),
("right bracket", [[112, 138],[112, 136],[115, 136],[118, 137],[120, 136],[123, 136],[125, 136],[128, 136],[131, 136],[134, 135],[137, 135],[140, 134],[143, 133],[145, 132],[147, 132],[149, 132],[152, 132],[153, 134],[154, 137],[155, 141],[156, 144],[157, 152],[158, 161],[160, 170],[162, 182],[164, 192],[166, 200],[167, 209],[168, 214],[168, 216],[169, 221],[169, 223],[169, 228],[169, 231],[166, 233],[164, 234],[161, 235],[155, 236],[147, 235],[140, 233],[131, 233],[124, 233],[117, 235],[114, 238],[112, 238]]),
("v", [[89, 164],[90, 162],[92, 162],[94, 164],[95, 166],[96, 169],[97, 171],[99, 175],[101, 178],[103, 182],[106, 189],[108, 194],[111, 199],[114, 204],[117, 209],[119, 214],[122, 218],[124, 222],[126, 225],[128, 228],[130, 229],[133, 233],[134, 236],[136, 239],[138, 240],[139, 242],[140, 244],[142, 242],[142, 240],[142, 237],[143, 235],[143, 233],[145, 229],[146, 226],[148, 217],[149, 208],[149, 205],[151, 196],[151, 193],[153, 182],[155, 172],[157, 165],[159, 160],[162, 155],[164, 150],[165, 148],[166, 146]]),
("delete", [[123, 129],[123, 131],[124, 133],[125, 136],[127, 140],[129, 142],[133, 148],[137, 154],[143, 158],[145, 161],[148, 164],[153, 170],[158, 176],[160, 178],[164, 183],[168, 188],[171, 191],[175, 196],[178, 200],[180, 202],[181, 205],[184, 208],[186, 210],[187, 213],[188, 215],[186, 212],[183, 211],[177, 208],[169, 206],[162, 205],[154, 207],[145, 209],[137, 210],[129, 214],[122, 217],[118, 218],[111, 221],[109, 222],[110, 219],[112, 217],[118, 209],[120, 207],[128, 196],[135, 187],[138, 183],[148, 167],[157, 153],[163, 145],[165, 142],[172, 133],[177, 127],[179, 127],[180, 125]]),
("left curly", [[150, 116],[147, 117],[145, 116],[142, 116],[139, 117],[136, 117],[133, 118],[129, 121],[126, 122],[123, 123],[120, 125],[118, 127],[115, 128],[113, 129],[112, 131],[113, 134],[115, 134],[117, 135],[120, 135],[123, 137],[126, 138],[129, 140],[135, 143],[137, 144],[139, 147],[141, 149],[140, 152],[139, 155],[134, 159],[131, 161],[124, 166],[121, 166],[117, 166],[114, 167],[112, 166],[114, 164],[116, 163],[118, 163],[120, 162],[122, 163],[125, 164],[127, 165],[129, 166],[130, 168],[129, 171],[127, 175],[125, 179],[123, 184],[121, 190],[120, 194],[119, 199],[120, 202],[123, 207],[127, 211],[133, 215],[142, 219],[148, 220],[151, 221]]),
("right curly brace",[(117,132),(115,132),(115,129),(117,129),(119,128),(122,127),(125,127),(127,127),(130,127),(133,129),(136,129),(138,130),(140,131),(143,134),(144,136),(145,139),(145,142),(145,145),(145,147),(145,149),(144,152),(142,157),(141,160),(139,163),(137,166),(135,167),(133,169),(131,172),(128,173),(126,176),(125,178),(125,180),(125,182),(126,184),(128,187),(130,187),(132,188),(135,189),(140,189),(145,189),(150,187),(155,186),(157,185),(159,184),(156,185),(154,185),(149,185),(145,187),(141,188),(136,191),(134,191),(131,192),(129,193),(129,195),(129,197),(131,200),(133,202),(136,206),(139,211),(142,215),(145,220),(147,225),(148,231),(147,239),(144,244),(139,248),(134,250),(126,253),(119,253),(115,253)]),
("star", [[75, 250],[75, 247],[77, 244],[78, 242],[79, 239],[80, 237],[82, 234],[82, 232],[84, 229],[85, 225],[87, 222],[88, 219],[89, 216],[91, 212],[92, 208],[94, 204],[95, 201],[96, 196],[97, 194],[98, 191],[100, 185],[102, 178],[104, 173],[104, 171],[105, 164],[106, 158],[107, 156],[107, 152],[108, 145],[109, 141],[110, 139],[112, 133],[113, 131],[116, 127],[117, 125],[119, 122],[121, 121],[123, 120],[125, 122],[125, 125],[127, 130],[128, 133],[131, 143],[136, 153],[140, 163],[144, 172],[145, 175],[151, 189],[156, 201],[161, 213],[166, 225],[169, 233],[171, 236],[174, 243],[177, 247],[178, 249],[179, 251],[180, 253],[180, 255],[179, 257],[177, 257],[174, 255],[169, 250],[164, 247],[160, 245],[149, 238],[138, 230],[127, 221],[124, 220],[112, 212],[110, 210],[96, 201],[84, 195],[74, 190],[64, 182],[55, 175],[51, 172],[49, 170],[51, 169],[56, 169],[66, 169],[78, 168],[92, 166],[107, 164],[123, 161],[140, 162],[156, 162],[171, 160],[173, 160],[186, 160],[195, 160],[198, 161],[203, 163],[208, 163],[206, 164],[200, 167],[187, 172],[174, 179],[172, 181],[153, 192],[137, 201],[123, 211],[112, 220],[99, 229],[90, 237],[80, 244],[73, 250],[69, 254],[69, 252]]),
("pigtail",[(88, 118), (90, 118), (92, 117), (95, 116), (97, 115), (99, 114), (102, 114), (103, 113), (104, 113), (106, 113), (107, 113), (109, 113), (111, 113), (114, 113), (117, 113), (119, 113), (120, 113), (121, 113), (123, 113), (125, 113), (126, 113), (127, 113), (130, 114), (131, 115), (132, 116), (134, 117), (135, 117), (137, 117), (139, 118), (140, 119), (141, 120), (144, 121), (147, 121), (148, 123), (150, 124), (151, 125), (153, 125), (155, 126), (156, 128), (158, 129), (159, 129), (160, 131), (161, 133), (162, 134), (163, 134), (165, 137), (166, 137), (167, 138), (167, 139), (168, 140), (169, 141), (169, 142), (170, 144), (171, 145), (172, 147), (173, 148), (174, 151), (175, 153), (175, 156), (175, 158), (175, 160), (176, 162), (176, 165), (176, 167), (176, 169), (176, 173), (176, 176), (176, 177), (176, 180), (176, 182), (176, 184), (176, 186), (176, 188), (176, 189), (176, 190), (176, 192), (176, 193), (176, 195), (175, 197), (175, 198), (174, 201), (173, 202), (172, 204), (171, 205), (171, 206), (171, 208), (171, 209), (171, 210), (171, 211), (170, 212), (169, 212), (167, 212), (166, 213), (164, 213), (163, 213), (162, 213), (161, 213), (159, 213), (155, 213), (154, 213), (151, 213), (149, 213), (148, 213), (147, 213), (146, 213), (143, 213), (142, 212), (141, 212), (141, 211), (139, 209), (137, 208), (136, 205), (135, 204), (135, 202), (134, 200), (133, 198), (132, 197), (131, 194), (131, 193), (130, 191), (129, 189), (128, 188), (127, 187), (127, 185), (127, 183), (127, 182), (127, 180), (127, 177), (127, 174), (127, 171), (127, 168), (128, 165), (129, 163), (130, 161), (131, 159), (132, 157), (132, 154), (133, 153), (134, 152), (135, 150), (135, 149), (136, 147), (137, 146), (139, 145), (141, 144), (143, 142), (147, 140), (152, 137), (159, 133), (162, 131), (167, 129), (170, 128), (173, 126), (175, 125), (177, 125), (179, 124), (183, 123), (185, 122), (187, 121), (191, 121), (195, 120), (197, 120), (200, 120), (203, 120), (206, 120), (208, 120), (211, 120), (214, 120), (215, 120), (217, 120), (219, 120), (220, 120), (222, 121), (223, 121), (224, 121), (227, 121), (230, 122), (231, 122), (235, 123), (237, 124), (239, 125), (241, 125), (243, 126), (244, 127), (246, 128), (247, 129), (248, 130), (248, 131), (249, 131), (250, 131), (251, 131), (251, 132), (252, 132), (252, 133), (253, 133), (254, 133), (255, 133), (256, 133), (256, 134), (256, 135), (257, 136), (258, 137), (259, 137), (260, 137), (261, 137), (261, 138), (262, 139), (263, 140), (263, 141), (264, 142), (266, 142), (266, 143), (266, 144), (266, 145), (267, 145), (268, 146), (268, 148), (268, 149), (268, 149)])
]

# num variable stores the N value- that divides the total path length into N point path
num = 64
origin = (0, 0)
# bounding box square size
square_size = 350
range_of_angle = (2 / 180) * pi
angle_p = (2 / 180) * pi
phi = 0.5 * (-1.0 + (5.0)**0.5)


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
        n = len(points)
        return sum([distance(self.points[i], points[i]) / n for i in range(n)])


def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5




class Input:
    # Preprocess the template points e.g resample,rotate, scale to and translate
    def __init__(self):
        # format the example gestures
        self.unistrokes = []
        for template in UNISTROKES:
            self.unistrokes.append(Gesture(template[1]))
            self.unistrokes[-1].name = template[0]
        print("check for the input",self.unistrokes[3])
        print(len(UNISTROKES[3][1]))
        Gesture(UNISTROKES[3][1])

    # recognition gesture function will perform golden search using the golden ratio which calls the method distance at best angle
    def rec_ges(self, points):

        # here the call to gesture class will preprocess the candidate points
        ges = Gesture(points)
        b = inf
        result = ''
        for template_stroke in self.unistrokes:
            # returns the distance between candidate points and the template points after preprocessing
            d = ges.distance_at_best_angle(template_stroke.points)

            # calculates the minimum distance and store the template name with the minimum distance to recognize the gesture
            if d < b:
                # update the pt2 best gesture
                b = d
                result = template_stroke.name
        return result



class Can:
            
    
    global points,f
    points = []
    num_points =64
    # flag variable to reset the canvas when drawing a new gesture again
    f=0        
    numUnistrokes = 16


    # object1=cntrl.Recognizer(numUnistrokes)


    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Group 21")
        self.canvas = Canvas(self.root, width=350, height=350)
        self.canvas.pack()
        self.text_widget = tk.Text(self.root, height=5, width=50)
        self.text_widget.pack(side="bottom", fill="x") 
        # button to start the drawing of a gesture and to add the starting point of a gesture to the points array
        self.canvas.bind("<ButtonPress>", self.mouseclickevent)
        # button to draw the gesture in a series of continuous points
        self.canvas.bind("<B1-Motion>", self.draw)
        # button release to capture/store/process the python main.py points on the canvas on release of the button
        self.canvas.bind("<ButtonRelease>", self.on_release)
        self.root.mainloop()


    

    


    def redraw(self,line_array):
    
        self.canvas.create_line(self.line_array)
        # x = event.x
        # y = event.y
        # points.append((x, y))

    def mouseclickevent(self , event):
        global x, y,points,f
        if f>1:
            self.canvas.delete("all")
            self.text_widget.delete("1.0", END)
            #canvas.delete(text_widget)
        f=1 
        x, y = event.x, event.y
        points.append((x, y))
        
    def draw(self,event):
        global x, y,points,f
        if f==1:
            self.canvas.create_line((x, y, event.x, event.y),fill='red',width=4)
            x = event.x
            y = event.y
            points.append((x, y))
        else:
            self.canvas.delete("all")
            
        

    def on_release(self, event):
        global f,points
        f=f+1
        x, y = event.x, event.y
        points.append((x, y))
        print(points)
        if(len(points) >=10):
            
            obj=Input()
            print(obj.rec_ges(points))
            rest= obj.rec_ges(points)
            print(rest)
            #canvas.create_text(100, 100, text= obj.rec_ges(points))
            
            self.text_widget.insert("1.0", rest)
        else:
            self.text_widget.insert("1.0", "Very Few points")
        
        # print(cntrl.centroid(points))
        
        points=[] 
        


Can()
    



