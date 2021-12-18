# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pyautogui 
import math
import random 

# get screen with and heigth
width,height = pyautogui.size()

# Disply callback function
def display():
    # Set the color of the screen
    glClearColor(1,1,1,0)

    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()
    # Flush buffer
    glFlush()
    # Swap buffers
    glutSwapBuffers()

# Scene render function
def render_Scene():        
    # Set current color to red
    glColor3f(1.0,0.0,0.0)
    # Draw a square
    glBegin(GL_POLYGON)
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5,0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,-0.5)
    glEnd()

    

# Initialize GLUT
glutInit()
# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)
# Set the initial window position to (center, center)
glutInitWindowPosition ((width -500) // 2, (height-500) // 2)

# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov")
# Define callbacks
glutDisplayFunc(display)
# Begin event loop
glutMainLoop()