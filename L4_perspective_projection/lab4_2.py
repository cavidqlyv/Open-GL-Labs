# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import pyautogui

width,height = pyautogui.size()

# The Rotation angle we whant to apply
angle = 5


# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()
    
    animation()

    # Swap buffers
    glutSwapBuffers()

def animation():
    global angle
    # Rotate
    glRotatef(angle,0,1,0)


# Scene render function
def render_Scene():
    glColor3f(0,1,0.5)
    glutWireCube(0.5)

def reshape(x,y):
    # Set a new projection matrix
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()     
    gluPerspective(20.0,x/y,4.5,20.0)
    gluLookAt(2,-6,-2,0,0,0,0,1,0)
    glViewport(0,0,x,y)  # Use the whole window for rendering  



def idle():
    time.sleep(0.1)

    glutPostRedisplay()

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

glutReshapeFunc(reshape)

# Define idle callback
glutIdleFunc(idle)

# Begin event loop
glutMainLoop()