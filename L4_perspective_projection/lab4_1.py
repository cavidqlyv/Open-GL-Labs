# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import pyautogui

width,height = pyautogui.size()
len = 0.6
arrowHeadLen = len*4/5
arrowHead = 0.04
angle = 1


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
    glRotatef(angle,1,0,0)
    glRotatef(angle,0,1,0)
    glRotatef(angle,0,0,1)
    


# Scene render function
def render_Scene():
    global len 
    global arrowHeadLen
    global arrowHead

    glLineWidth(1.5)
    # Draw a Line from the origin to the point (len,0,0)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0, 0,0)
    glVertex3f(len, 0,0)
    glEnd()

    # arrow heads of the red line
    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(arrowHeadLen, arrowHead,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(arrowHeadLen, -arrowHead,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(arrowHeadLen, 0,arrowHead)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(len, 0,0)
    glVertex3f(arrowHeadLen, 0,-arrowHead)
    glEnd()

    # Draw a green line
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(0, 0,0)
    glVertex3f(0, len,0)
    glEnd()

    # arrow heads of the green line
    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(arrowHead, arrowHeadLen,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(-arrowHead, arrowHeadLen,0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(0, arrowHeadLen,arrowHead)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, len,0)
    glVertex3f(0, arrowHeadLen,-arrowHead)
    glEnd()


    # Draw a blue line
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0, 0,0)
    glVertex3f(0, 0,len)
    glEnd()

    # arrow heads of the blue line
    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(arrowHead, 0,arrowHeadLen)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(-arrowHead, 0,arrowHeadLen)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(0, arrowHead,arrowHeadLen)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0, 0,len)
    glVertex3f(0, -arrowHead,arrowHeadLen)
    glEnd()

def reshape(x,y):
    # Set a new projection matrix
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()     
    gluPerspective(20.0,x/y,4.5,20.0)
    gluLookAt(2,-4,-2,0,0,0,0,1,0)
    glViewport(0,0,x,y)  # Use the whole window for rendering  



def idle():
    time.sleep(0.05)

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