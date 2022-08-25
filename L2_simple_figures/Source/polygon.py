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
    
    #Number of polygon
    polygon = 8

    RadiusX = 0.8 # radius of polygon

    #Using types of drawing Triangles
    triangleType=GL_TRIANGLE_FAN # GL_TRIANGLES GL_TRIANGLE_STRIP

    glColor3f(0,1,1)
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)

    # GL_TRIANGLE_FAN
    if triangleType==GL_TRIANGLE_FAN:
        glBegin(GL_TRIANGLE_FAN)       #start drawing a line loop
        glVertex2f(0.0, 0.0)           # center of polygon
        for i in range(polygon+1): # We draw 8 points
            angle = 2*math.pi * i / polygon
            x = RadiusX * math.cos(angle)
            y = RadiusX * math.sin(angle)
            glColor3f(random.random(),random.random(),random.random())
            glVertex2f(x, y)
        glEnd()                     #end drawing of line loop


    # GL_TRIANGLES
    if triangleType==GL_TRIANGLES:
        for i in range(polygon): # We draw 8 points
            glBegin(GL_TRIANGLES)       #start drawing a line loop
            glVertex2f(0.0, 0.0)           # center of polygon
            angle = 2*math.pi * i / polygon
            x = RadiusX * math.cos(angle)
            y = RadiusX * math.sin(angle)
            glColor3f(random.random(),random.random(),random.random())
            glVertex2f(x, y)
            angle = 2*math.pi * (i+1) / polygon
            x = RadiusX * math.cos(angle)
            y = RadiusX * math.sin(angle)
            glVertex2f(x, y)
            glEnd()                     #end drawing of line loop


    # GL_TRIANGLE_STRIP
    if triangleType==GL_TRIANGLE_STRIP:
        glBegin(GL_TRIANGLE_STRIP)       #start drawing a line loop
        for i in range(polygon+1): # We draw 8 points
            glVertex2f(0.0, 0.0)           # center of polygon
            angle = 2*math.pi * i / polygon
            x = RadiusX * math.cos(angle)
            y = RadiusX * math.sin(angle)
            glColor3f(random.random(),random.random(),random.random())
            glVertex2f(x, y)
        glEnd()                     #end drawing of line loop
    



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