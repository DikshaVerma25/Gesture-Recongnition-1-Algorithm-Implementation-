# \$1-Algorithm-Implementation

This project goal will be to implement the $1 algorithm from the \$-family of gesture recognition algorithms. We will build up the components needed to do a  live demo and run offline recognition tests of the algorithm step by step each week, until the final deliverables are due.

## Drawing on Canvas

### Goal 
The goals of Part 1 of Project #1 are for you to do the following:  
a) set up your project development environment;  
b) instantiate a blank ‘canvas’ to the screen using GUI elements;  
c) listen for mouse or touch events on the canvas and draw them as the user makes them; and  
d) allow the user to clear the canvas.

**Code Explaination:**

*A) Importing the libraries and initializing the canvas*

Line **1-3** the libraries are imported.<br>

*B) Creating canvas*

Line **6-7** Instance of Tk class is created which is stored in the variable root. And renaming the the canvas as Group 21. <br>
Line **9-10** Instance of class "Canvas" is craeted which is stored in varible "canvas". Later the height and width are specified. Pack method helps in managing the canvas to occupy the space available in the window. 

*C) Using "mouseclickevent" and "draw" to enable drawing*

Line **13-24** The "mouseclickevent" and "draw" is triggered when the mouse button is pressed and moved. Event is passed as the argument which stored the x and y coordinates of the drawing. 

*D) Adding eraser*

Line **25-26** Here button widget named "erase_button" is made, where the button is given as "Erase". Lamba is passed the command calling delete method for erasing everything on canvas (all). This button is added to root using the method pack. 






