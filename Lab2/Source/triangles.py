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
    glClear(GL_COLOR_BUFFER_BIT)

    x1, x2, x3 = 0.3, 0.7, 0.5
    y1, y2, y3 = 0.2, 0.5, 0.7

    # Draw triangle
    glColor3f(1, 1, 0)
    glBegin(GL_LINE_LOOP)       #start drawing a line loop
    glVertex2f(x1, y1)          
    glVertex2f(x2, y2)          
    glVertex2f(x3, y3)       
    glEnd()                     #end drawing of line loop

    glBegin(GL_LINE_LOOP)       #start drawing a line loop
    glVertex2f(-x1, y1)          
    glVertex2f(-x2, y2)          
    glVertex2f(-x3, y3) 
    glEnd()                     #end drawing of line loop
 
    glBegin(GL_LINE_LOOP)       #start drawing a line loop
    glVertex2f(x1, -y1)          
    glVertex2f(x2, -y2)        
    glVertex2f(x3, -y3)     
    glEnd()                     #end drawing of line loop

    glBegin(GL_LINE_LOOP)       #start drawing a line loop
    glVertex2f(-x1, -y1)          
    glVertex2f(-x2, -y2)          
    glVertex2f(-x3, -y3)   
    glEnd()                     #end drawing of line loop

    glColor3f(1, 0, 0)
    glPointSize(5.0)
    glBegin(GL_LINES)

    # X-AXIS (from (-1, 0) to (1, 0))
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)

    # Y-AXIS (from (0, 1) to (0, -1))
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
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

Width = (screenWidth-250)//2
Height = (screenHeight-250)//2

print(Width,Height)
glutInitWindowPosition(Width,Height)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()