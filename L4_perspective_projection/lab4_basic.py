# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import pyautogui

width,height = pyautogui.size()

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
    len = 0.7
    support = 0.6
    angle = 0.1*math.cos(4)

    # Draw a Line from the origin to the point (len,0,0)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0, 0,0)
    glVertex3f(len, 0,0)
    glEnd()

    # support lines of the red line
    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(support, angle,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(support, -angle,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(support, 0,angle)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(support, 0,-angle)
    glEnd()


    # Draw a green line
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(0, 0,0)
    glVertex3f(0, len,0)
    glEnd()

    # support lines of the green line
    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(angle, support,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(-angle, support,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(0, support,angle)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(0, support,-angle)
    glEnd()


    
    # Draw a blue line
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0, 0,0)
    glVertex3f(0, 0,len)
    glEnd()

    # support lines of the blue line
    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(angle, 0,support)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(-angle, 0,support)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(0, angle,support)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(0, -angle,support)
    glEnd()

def reshape(x,y):
    # Set a new projection matrix
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()     
    gluPerspective(20.0,x/y,4.5,20.0)
    gluLookAt(2,-4,-2,0,0,0,0,1,0)
    glViewport(0,0,x,y)  # Use the whole window for rendering  

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

# Begin event loop
glutMainLoop()