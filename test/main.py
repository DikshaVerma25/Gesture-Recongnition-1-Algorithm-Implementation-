"""$1 Unistroke Recognizer

This program implements the $1 algorithm in Python.

The user is supposed to draw unistroke gestures and the algorithm should
recognize it.

The documentation original implementations can be found here:
http://depts.washington.edu/madlab/proj/dollar/index.html
"""


from tkinter import Tk, Canvas, Label, StringVar, PhotoImage, Frame
from dollar import Dollar


class Paint:

    PEN_SIZE = 3
    WINDOW_TITLE = 'Recognizer'
    # TEMPLATES_IMAGE_PATH = './templates.gif'
    INITIAL_MESSAGE = 'Draw something'
    MIN_N_POINTS = 10
    NOT_ENOUGH_POINTS_MESSAGE = 'Not enough points'

    def __init__(self):
        # points
        self.old_point = (None, None)
        self.points = []
        self.recognizer = Dollar()
        # root
        self.root = Tk()    2
        self.root.title(self.WINDOW_TITLE)
        # left frame
        left_frame = Frame(self.root)
        left_frame.grid(row=1, column=1)
        # canvas
        self.canvas = Canvas(left_frame, bg='white', width=350, height=330)
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        # label
        self.label_text = StringVar()
        self.label_text.set('Draw something')
        self.label = Label(left_frame, textvariable=self.label_text)
        self.label.pack()
        # image
        self.image = Canvas(self.root, width=352, height=348)
        # file = PhotoImage(file=self.TEMPLATES_IMAGE_PATH)
        # self.image.create_image(177, 175, image=file)
        # self.image.grid(row=1, column=2)
        # start
        self.root.mainloop()

    def paint(self, event):
        point = (event.x, event.y)
        if self.old_point != (None, None):
            self.canvas.create_line(self.old_point, point, width=self.PEN_SIZE)
        else:
            self.canvas.delete('all')
        self.points.append(point)
        self.old_point = point

    def reset(self, event):
        self.old_point = (None, None)
        if (len(self.points) < self.MIN_N_POINTS):
            self.label_text.set(self.NOT_ENOUGH_POINTS_MESSAGE)
            return
        self.label_text.set(self.recognizer.get_gesture(self.points))
        self.points = []
        


Paint()
