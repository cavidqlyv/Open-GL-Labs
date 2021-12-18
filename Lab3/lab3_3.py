# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
movementConstant = 0.05
move = 0.05
stepsToBorder = 24
step=0


def idle():
    global move
    global step
    glTranslatef(move,0,0)
    
    # Border reach check
    if step==stepsToBorder:
        step=-step # change the direction
        move = move*step*2 # if you have reached to the border go 2xmove back
    else: 
        move = movementConstant # move forward
        step+=1

    time.sleep(0.05)
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
# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov")
# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)
# Define display callback
glutDisplayFunc(display)
# Define idle callback
glutIdleFunc(idle)
# Begin event loop
glutMainLoop()

