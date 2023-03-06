from tkinter import *

# Define the dimensions of the canvas
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

# Create a list to store the points for each shape
shapes = [[] for i in range(3)]  # Three shapes: square, circle, triangle

# Create the canvas and pack it into the window
root = Tk()
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

# Define a function to handle mouse clicks on the canvas
def mouse_click(event):
    x = event.x
    y = event.y
    # Add the point to the list for the current shape
    shapes[current_shape].append((x, y))
    # Draw a dot on the canvas to indicate where the user clicked
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')


# Define a function to prompt the user to draw a shape
def draw_shape(shape):
    global current_shape
    current_shape = shape
    # Prompt the user to draw the shape 10 times
    for i in range(10):
        # Clear the canvas
        canvas.delete('all')
        # Bind the mouse click event to the canvas
        canvas.bind('<Button-1>', mouse_click)
        # Display a message indicating the current shape and iteration
        message = 'Draw a {} ({} of 10)'.format(['square', 'circle', 'triangle'][shape], i+1)
        canvas.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, text=message)
        # Wait for the user to finish drawing the shape
        canvas.mainloop()
    # Unbind the mouse click event
    canvas.unbind('<Button-1>')

# Prompt the user to draw each shape
canvas.bind("<B1-Motion>", draw_shape(0))


# Print the list of points for each shape
print('Square:', shapes[0])
print('Circle:', shapes[1])
print('Triangle:', shapes[2])




