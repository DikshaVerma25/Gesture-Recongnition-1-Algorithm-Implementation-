from tkinter import *
import tkinter as tk
from math import pi, atan2, cos, sin, inf
import time,math


# Template points will be stored in UNISTROKE variable
# List of List is being used to store the template points
UNISTROKES = [("a", [(100, 168), (101, 167), (103, 163), (105, 159), (107, 153), (108, 148), (110, 144), (112, 139), (114, 135), (117, 132), (120, 129), (123, 125), (126, 122), (129, 118), (131, 116), (133, 114), (134, 113), (135, 113), (136, 113), (137, 113), (138, 113), (140, 113), (141, 113), (143, 113), (144, 113), (144, 114), (142, 114), (140, 114), (138, 114), (135, 115), (131, 116), (129, 117), (126, 118), (124, 118), (122, 119), (121, 120), (120, 121), (119, 121), (118, 122), (117, 123), (116, 124), (115, 125), (114, 126), (113, 127), (112, 129), (111, 131), (110, 133), (110, 135), (109, 137), (109, 139), (109, 140), (109, 142), (109, 143), (109, 145), (109, 146), (110, 147), (110, 148), (111, 149), (112, 150), (114, 151), (115, 152), (117, 153), (119, 154), (120, 154), (122, 154), (123, 154), (124, 154), (125, 154), (126, 154), (127, 154), (128, 154), (129, 153), (130, 153), (130, 152), (131, 152), (131, 151), (131, 150), (131, 149), (132, 148), (132, 147), (132, 146), (133, 145), (133, 143), (134, 142), (134, 141), (134, 139), (134, 138), (135, 137), (135, 135), (135, 134), (135, 133), (136, 133), (136, 132), (136, 130), (137, 129), (137, 128), (137, 127), (137, 126), (137, 125), (138, 125), (138, 124), (138, 123), (138, 122), (138, 121), (138, 120), (139, 120), (139, 119), (139, 118), (139, 117), (139, 116), (139, 115), (140, 115), (140, 116), (139, 117), (139, 119), (137, 122), (137, 126), (136, 129), (134, 132), (134, 135), (133, 137), (133, 138), (133, 139), (132, 140), (132, 141), (132, 143), (132, 144), (132, 145), (132, 146), (132, 147), (132, 148), (132, 149), (132, 150), (135, 151), (138, 152), (141, 153), (144, 153), (147, 154), (150, 154), (152, 154), (153, 154), (155, 154), (156, 154), (156, 154)]),
("b", [(108, 298), (108, 297), (109, 296), (113, 292), (117, 287), (121, 281), (123, 273), (126, 263), (128, 252), (129, 239), (129, 226), (129, 213), (129, 200), (129, 188), (129, 178), (129, 170), (128, 164), (127, 161), (126, 158), (124, 156), (123, 155), (120, 154), (118, 154), (115, 154), (112, 154), (108, 157), (104, 162), (101, 168), (99, 173), (99, 180), (99, 186), (99, 192), (99, 198), (99, 203), (101, 209), (103, 215), (105, 222), (108, 229), (111, 235), (114, 241), (117, 246), (119, 250), (122, 253), (125, 257), (127, 260), (130, 264), (132, 267), (134, 269), (137, 271), (139, 272), (141, 273), (144, 275), (146, 275), (149, 276), (152, 276), (155, 276), (157, 276), (159, 276), (161, 275), (163, 273), (165, 270), (167, 265), (169, 260), (170, 255), (171, 249), (172, 243), (172, 238), (172, 233), (172, 229), (172, 226), (171, 223), (170, 219), (169, 216), (168, 214), (166, 213), (165, 212), (163, 211), (162, 211), (160, 211), (158, 211), (156, 211), (155, 211), (154, 212), (153, 213), (152, 215), (152, 216), (152, 217), (152, 218), (152, 219), (153, 220), (155, 220), (158, 220), (163, 220), (167, 220), (172, 220), (177, 220), (181, 220), (186, 219), (191, 218), (196, 216), (201, 215), (204, 214), (205, 213), (206, 213), (207, 213)]),
("c", [(41, 222), (42, 222), (44, 222), (49, 222), (52, 222), (55, 222), (58, 219), (61, 214), (64, 209), (67, 203), (71, 196), (74, 190), (78, 183), (82, 175), (86, 167), (91, 160), (95, 154), (100, 149), (104, 144), (107, 141), (110, 139), (114, 137), (117, 136), (120, 135), (122, 134), (124, 134), (126, 134), (127, 134), (128, 134), (130, 134), (131, 134), (129, 134), (125, 134), (122, 134), (118, 134), (115, 134), (113, 134), (110, 134), (108, 134), (106, 134), (105, 134), (103, 135), (101, 136), (99, 137), (97, 139), (94, 142), (92, 144), (89, 147), (86, 151), (84, 153), (82, 156), (81, 159), (79, 162), (78, 166), (77, 170), (77, 175), (77, 181), (77, 187), (77, 194), (77, 200), (77, 205), (77, 210), (79, 214), (81, 217), (82, 219), (84, 221), (86, 223), (89, 224), (92, 226), (96, 227), (101, 228), (105, 229), (110, 229), (114, 229), (119, 229), (124, 229), (129, 229), (134, 227), (139, 226), (142, 224), (144, 223), (145, 223), (146, 223), (146, 222), (147, 222), (148, 222), (148, 222)]),
("d", [(73, 301), (74, 301), (76, 301), (77, 301), (79, 301), (80, 301), (81, 301), (82, 301), (83, 299), (85, 296), (88, 291), (92, 285), (95, 279), (97, 273), (99, 269), (102, 265), (104, 262), (106, 259), (109, 256), (112, 253), (116, 249), (121, 246), (126, 242), (132, 238), (138, 234), (142, 233), (145, 232), (147, 231), (150, 231), (151, 231), (153, 231), (154, 232), (155, 233), (156, 233), (154, 233), (150, 233), (147, 233), (145, 233), (143, 233), (141, 233), (139, 233), (138, 233), (136, 233), (134, 233), (132, 233), (130, 234), (129, 234), (128, 234), (127, 235), (126, 236), (125, 236), (123, 237), (122, 238), (120, 239), (119, 240), (119, 241), (118, 242), (117, 243), (116, 244), (116, 245), (115, 245), (115, 246), (115, 248), (114, 249), (113, 251), (113, 253), (112, 256), (111, 259), (110, 262), (110, 265), (109, 268), (109, 270), (109, 272), (109, 274), (109, 275), (109, 277), (109, 278), (109, 279), (110, 281), (110, 282), (111, 284), (112, 284), (113, 285), (114, 286), (115, 287), (117, 288), (118, 288), (120, 289), (122, 290), (124, 290), (126, 290), (129, 290), (131, 290), (133, 290), (135, 290), (138, 290), (140, 290), (141, 289), (143, 288), (144, 287), (145, 286), (147, 284), (148, 283), (150, 281), (151, 280), (152, 278), (153, 276), (154, 274), (156, 272), (157, 269), (158, 266), (159, 263), (161, 259), (162, 254), (163, 250), (164, 246), (166, 241), (167, 235), (169, 228), (171, 220), (173, 213), (174, 207), (175, 201), (175, 196), (175, 192), (176, 187), (176, 184), (176, 182), (176, 181), (176, 179), (176, 178), (176, 176), (176, 175), (175, 174), (175, 173), (174, 173), (173, 172), (172, 172), (171, 172), (170, 172), (170, 173), (169, 173), (168, 175), (167, 176), (167, 178), (167, 180), (166, 182), (166, 184), (166, 187), (166, 189), (166, 192), (165, 195), (165, 198), (165, 200), (165, 203), (165, 206), (164, 210), (164, 213), (163, 217), (163, 220), (162, 222), (162, 225), (162, 228), (162, 230), (162, 233), (162, 237), (162, 240), (162, 243), (162, 246), (162, 249), (163, 253), (163, 256), (164, 258), (165, 261), (166, 262), (166, 264), (167, 265), (167, 266), (168, 266), (168, 267), (169, 269), (170, 270), (172, 272), (173, 274), (174, 276), (176, 277), (176, 279), (177, 280), (178, 281), (179, 282), (180, 282), (180, 283), (181, 283), (182, 283), (183, 284), (184, 284), (185, 284), (185, 284)]),
("f", [(77, 209), (80, 209), (82, 209), (87, 209), (94, 207), (99, 206), (103, 205), (106, 204), (108, 203), (111, 202), (115, 199), (119, 196), (124, 192), (130, 188), (134, 184), (138, 181), (141, 178), (144, 175), (145, 172), (146, 168), (148, 165), (148, 161), (148, 157), (148, 152), (148, 148), (148, 144), (146, 139), (144, 135), (142, 132), (140, 130), (138, 128), (137, 127), (136, 127), (135, 129), (134, 131), (132, 135), (131, 140), (129, 146), (128, 151), (128, 157), (128, 163), (128, 169), (128, 174), (128, 180), (128, 185), (128, 191), (128, 197), (128, 203), (128, 209), (128, 216), (128, 223), (128, 231), (128, 237), (128, 243), (128, 249), (128, 253), (129, 257), (131, 260), (132, 263), (133, 265), (134, 267), (136, 270), (139, 273), (141, 275), (143, 276), (145, 277), (147, 277), (148, 278), (149, 278), (151, 278), (152, 277), (153, 275), (154, 273), (155, 269), (156, 266), (157, 263), (157, 259), (157, 256), (157, 253), (157, 250), (156, 247), (156, 244), (155, 242), (154, 239), (153, 237), (151, 234), (149, 231), (147, 228), (145, 226), (142, 223), (140, 221), (138, 219), (136, 217), (133, 215), (131, 214), (129, 213), (127, 212), (125, 212), (123, 212), (122, 211), (121, 211), (120, 211), (119, 211), (119, 212), (118, 213), (118, 214), (118, 215), (118, 216), (118, 217), (118, 218), (118, 219), (119, 220), (120, 220), (121, 220), (123, 220), (125, 220), (128, 220), (131, 220), (134, 220), (138, 219), (142, 218), (145, 216), (148, 215), (152, 213), (155, 211), (157, 210), (159, 209), (160, 209), (160, 209)]),
# ("arrow", [[68, 222],[70, 220],[73, 218],[75, 217],[77, 215],[80, 213],[82, 212],[84, 210],[87, 209],[89, 208],[92, 206],[95, 204],[101, 201],[106, 198],[112, 194],[118, 191],[124, 187],[127, 186],[132, 183],[138, 181],[141, 180],[146, 178],[154, 173],[159, 171],[161, 170],[166, 167],[168, 167],[171, 166],[174, 164],[177, 162],[180, 160],[182, 158],[183, 156],[181, 154],[178, 153],[171, 153],[164, 153],[160, 153],[150, 154],[147, 155],[141, 157],[137, 158],[135, 158],[137, 158],[140, 157],[143, 156],[151, 154],[160, 152],[170, 149],[179, 147],[185, 145],[192, 144],[196, 144],[198, 144],[200, 144],[201, 147],[199, 149],[194, 157],[191, 160],[186, 167],[180, 176],[177, 179],[171, 187],[169, 189],[165, 194],[164, 196]]),
# ("zig-zag", [[307, 216],[333, 186],[356, 215],[375, 186],[399, 216],[418, 186]]),
# ("left bracket", [[140, 124],[138, 123],[135, 122],[133, 123],[130, 123],[128, 124],[125, 125],[122, 124],[120, 124],[118, 124],[116, 125],[113, 125],[111, 125],[108, 124],[106, 125],[104, 125],[102, 124],[100, 123],[98, 123],[95, 124],[93, 123],[90, 124],[88, 124],[85, 125],[83, 126],[81, 127],[81, 129],[82, 131],[82, 134],[83, 138],[84, 141],[84, 144],[85, 148],[85, 151],[86, 156],[86, 160],[86, 164],[86, 168],[87, 171],[87, 175],[87, 179],[87, 182],[87, 186],[88, 188],[88, 195],[88, 198],[88, 201],[88, 207],[89, 211],[89, 213],[89, 217],[89, 222],[88, 225],[88, 229],[88, 231],[88, 233],[88, 235],[89, 237],[89, 240],[89, 242],[91, 241],[94, 241],[96, 240],[98, 239],[105, 240],[109, 240],[113, 239],[116, 240],[121, 239],[130, 240],[136, 237],[139, 237],[144, 238],[151, 237],[157, 236],[159, 237]]),
# ("right bracket", [[112, 138],[112, 136],[115, 136],[118, 137],[120, 136],[123, 136],[125, 136],[128, 136],[131, 136],[134, 135],[137, 135],[140, 134],[143, 133],[145, 132],[147, 132],[149, 132],[152, 132],[153, 134],[154, 137],[155, 141],[156, 144],[157, 152],[158, 161],[160, 170],[162, 182],[164, 192],[166, 200],[167, 209],[168, 214],[168, 216],[169, 221],[169, 223],[169, 228],[169, 231],[166, 233],[164, 234],[161, 235],[155, 236],[147, 235],[140, 233],[131, 233],[124, 233],[117, 235],[114, 238],[112, 238]]),
# ("v", [[89, 164],[90, 162],[92, 162],[94, 164],[95, 166],[96, 169],[97, 171],[99, 175],[101, 178],[103, 182],[106, 189],[108, 194],[111, 199],[114, 204],[117, 209],[119, 214],[122, 218],[124, 222],[126, 225],[128, 228],[130, 229],[133, 233],[134, 236],[136, 239],[138, 240],[139, 242],[140, 244],[142, 242],[142, 240],[142, 237],[143, 235],[143, 233],[145, 229],[146, 226],[148, 217],[149, 208],[149, 205],[151, 196],[151, 193],[153, 182],[155, 172],[157, 165],[159, 160],[162, 155],[164, 150],[165, 148],[166, 146]]),
# ("delete", [[123, 129],[123, 131],[124, 133],[125, 136],[127, 140],[129, 142],[133, 148],[137, 154],[143, 158],[145, 161],[148, 164],[153, 170],[158, 176],[160, 178],[164, 183],[168, 188],[171, 191],[175, 196],[178, 200],[180, 202],[181, 205],[184, 208],[186, 210],[187, 213],[188, 215],[186, 212],[183, 211],[177, 208],[169, 206],[162, 205],[154, 207],[145, 209],[137, 210],[129, 214],[122, 217],[118, 218],[111, 221],[109, 222],[110, 219],[112, 217],[118, 209],[120, 207],[128, 196],[135, 187],[138, 183],[148, 167],[157, 153],[163, 145],[165, 142],[172, 133],[177, 127],[179, 127],[180, 125]]),
# ("left curly brace", [[150, 116],[147, 117],[145, 116],[142, 116],[139, 117],[136, 117],[133, 118],[129, 121],[126, 122],[123, 123],[120, 125],[118, 127],[115, 128],[113, 129],[112, 131],[113, 134],[115, 134],[117, 135],[120, 135],[123, 137],[126, 138],[129, 140],[135, 143],[137, 144],[139, 147],[141, 149],[140, 152],[139, 155],[134, 159],[131, 161],[124, 166],[121, 166],[117, 166],[114, 167],[112, 166],[114, 164],[116, 163],[118, 163],[120, 162],[122, 163],[125, 164],[127, 165],[129, 166],[130, 168],[129, 171],[127, 175],[125, 179],[123, 184],[121, 190],[120, 194],[119, 199],[120, 202],[123, 207],[127, 211],[133, 215],[142, 219],[148, 220],[151, 221]]),
# ("right curly brace",[[117,132],[115,132],[115,129],[117,129],[119,128],[122,127],[125,127],[127,127],[130,127],[133,129],[136,129],[138,130],[140,131],[143,134],[144,136],[145,139],[145,142],[145,145],[145,147],[145,149],[144,152],[142,157],[141,160],[139,163],[137,166],[135,167],[133,169],[131,172],[128,173],[126,176],[125,178],[125,180],[125,182],[126,184],[128,187],[130,187],[132,188],[135,189],[140,189],[145,189],[150,187],[155,186],[157,185],[159,184],[156,185],[154,185],[149,185],[145,187],[141,188],[136,191],[134,191],[131,192],[129,193],[129,195],[129,197],[131,200],[133,202],[136,206],[139,211],[142,215],[145,220],[147,225],[148,231],[147,239],[144,244],[139,248],[134,250],[126,253],[119,253],[115,253]]),
# ("star", [[75, 250],[75, 247],[77, 244],[78, 242],[79, 239],[80, 237],[82, 234],[82, 232],[84, 229],[85, 225],[87, 222],[88, 219],[89, 216],[91, 212],[92, 208],[94, 204],[95, 201],[96, 196],[97, 194],[98, 191],[100, 185],[102, 178],[104, 173],[104, 171],[105, 164],[106, 158],[107, 156],[107, 152],[108, 145],[109, 141],[110, 139],[112, 133],[113, 131],[116, 127],[117, 125],[119, 122],[121, 121],[123, 120],[125, 122],[125, 125],[127, 130],[128, 133],[131, 143],[136, 153],[140, 163],[144, 172],[145, 175],[151, 189],[156, 201],[161, 213],[166, 225],[169, 233],[171, 236],[174, 243],[177, 247],[178, 249],[179, 251],[180, 253],[180, 255],[179, 257],[177, 257],[174, 255],[169, 250],[164, 247],[160, 245],[149, 238],[138, 230],[127, 221],[124, 220],[112, 212],[110, 210],[96, 201],[84, 195],[74, 190],[64, 182],[55, 175],[51, 172],[49, 170],[51, 169],[56, 169],[66, 169],[78, 168],[92, 166],[107, 164],[123, 161],[140, 162],[156, 162],[171, 160],[173, 160],[186, 160],[195, 160],[198, 161],[203, 163],[208, 163],[206, 164],[200, 167],[187, 172],[174, 179],[172, 181],[153, 192],[137, 201],[123, 211],[112, 220],[99, 229],[90, 237],[80, 244],[73, 250],[69, 254],[69, 252]]),
# ("pigtail", [[81, 219],[84, 218],[86, 220],[88, 220],[90, 220],[92, 219],[95, 220],[97, 219],[99, 220],[102, 218],[105, 217],[107, 216],[110, 216],[113, 214],[116, 212],[118, 210],[121, 208],[124, 205],[126, 202],[129, 199],[132, 196],[136, 191],[139, 187],[142, 182],[144, 179],[146, 174],[148, 170],[149, 168],[151, 162],[152, 160],[152, 157],[152, 155],[152, 151],[152, 149],[152, 146],[149, 142],[148, 139],[145, 137],[141, 135],[139, 135],[134, 136],[130, 140],[128, 142],[126, 145],[122, 150],[119, 158],[117, 163],[115, 170],[114, 175],[117, 184],[120, 190],[125, 199],[129, 203],[133, 208],[138, 213],[145, 215],[155, 218],[164, 219],[166, 219],[177, 219],[182, 218],[192, 216],[196, 213],[199, 212],[201, 211]    ])
]
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
        n = len(points)
        return sum([distance(self.points[i], points[i]) / n for i in range(n)])


def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5




class Input:
    # Preprocess the template points e.g resample,rotate, scale to and translate

    def __init__(self):
        # format the example gestures
        t0 = time.time()

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
        t0 = time.time()

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
            
        return (result,1.0 - b / HalfDiagonal)



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
            print("4444444444444444444444444444444444444444444444444444444",points)
            obj=Input()
            rest= obj.rec_ges(points)
            print("***",rest)
            #canvas.create_text(100, 100, text= obj.rec_ges(points))
            result=rest[0]+"("+str(rest[1])+")"
            self.text_widget.insert("1.0", result)
        else:
            self.text_widget.insert("1.0", "Very Few points")
        
        
        points=[] 
        


Can()
    


