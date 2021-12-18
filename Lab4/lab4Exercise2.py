# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import pyautogui
width,height = pyautogui.size()

len = 0.7


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
    global len

    # Draw a Line from the origin to the point (len,0,0)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0, 0,0)
    glVertex3f(len, 0,0)
    glEnd()

    # Draw a green line
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(0, 0,0)
    glVertex3f(0, len,0)
    glEnd()

    # Draw a blue line
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0, 0,0)
    glVertex3f(0, 0,len)
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