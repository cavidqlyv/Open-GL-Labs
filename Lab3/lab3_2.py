# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

move = 0.3

def idle():
    global move
    if move==-0.3:
        move=-0.6

    glTranslatef(0,move,0)
    move *= -1
    time.sleep(0.2)
    glutPostRedisplay()

# Scene render function
def render_Scene():
    glColor3f(0,1,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3,-0.1)
    glVertex2f(0.3,-0.1)
    glVertex2f(0,0.3)
    glEnd()

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)
    # Render scene
    render_Scene()
    # Swap buffers
    glutSwapBuffers()

# Initialize GLUT
glutInit()
# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

import pyautogui
width, height = pyautogui.size()

# Set the initial window position to (center, center)
glutInitWindowPosition ((width -500) // 2, (height-500) // 2)

# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov")
# Define display callback
glutDisplayFunc(display)
# Define idle callback
glutIdleFunc(idle)
# Begin event loop
glutMainLoop()

