# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pyautogui 
import math
import random 


# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers()  


# Scene render function
def render_Scene():
    # random 3 nubers between 0 and 1  
    
    for i in range(64): # We draw 64 points
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        glPointSize(i//6.4 + 1)
        angle = 2*math.pi * i / 64
        x = 0.5 * math.cos(angle)
        y = 0.5 * math.sin(angle)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)


# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov" )

# Initialize the color to the white color
glClearColor(0, 0, 0, 0)

# get screen width and height
screenWidth,screenHeight   = pyautogui.size()
print(screenWidth,screenHeight )

Width = (screenWidth-500)//2
Height = (screenHeight-500)//2

print(Width,Height)
glutInitWindowPosition(Width,Height)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()