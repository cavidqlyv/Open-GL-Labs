# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

# Variables
move = 0.05  # movement speed
stepsToBorder = 20 # Steps To Border
moveReset = move*stepsToBorder*2  # This is writen because we assume that the window is Square if not we need to create Up and Right borders seperately

# Events that measue Button press and release
keyUpPressed = False
keyDownPressed = False
keyRightPressed = False
keyLeftPressed = False

# Count of pressed keys
keyUpPressTimes = 0
keyRightPressTimes = 0

# Button Press
def ProcessSpecialKeys(key,  x,  y):
    global keyUpPressed
    global keyDownPressed
    global keyRightPressed
    global keyLeftPressed

    if key == GLUT_KEY_UP:
        keyUpPressed = True
    elif key == GLUT_KEY_DOWN:
        keyDownPressed = True
    elif key == GLUT_KEY_RIGHT:
        keyRightPressed = True
    elif key == GLUT_KEY_LEFT:
        keyLeftPressed = True

# Button Release
def ReleaseSpecialKeys(key,  x,  y):
    global keyUpPressed
    global keyDownPressed
    global keyRightPressed
    global keyLeftPressed

    if key == GLUT_KEY_UP:
        keyUpPressed = False
    elif key == GLUT_KEY_DOWN:
        keyDownPressed = False
    elif key == GLUT_KEY_RIGHT:
        keyRightPressed = False
    elif key == GLUT_KEY_LEFT:
        keyLeftPressed = False

def idle():
    global move
    global keyUpPressed
    global keyUpPressTimes
    global keyDownPressed
    global keyRightPressed
    global keyRightPressTimes
    global keyLeftPressed
    global moveReset

    # Motion of Triangle
    # Up
    if (keyUpPressed):
        glTranslatef(0,move,0)
        keyUpPressTimes += 1
        print("keyUpPressTimes: ", keyUpPressTimes)
    
    # Down
    elif (keyDownPressed):
        glTranslatef(0,-move,0)
        keyUpPressTimes -= 1
        print("keyDownPressTime: ", keyUpPressTimes)
    
    # Right
    elif (keyRightPressed):
        glTranslatef(move,0,0)
        keyRightPressTimes += 1
        print("keyRightPressTime: ", keyRightPressTimes)

    # Left
    elif (keyLeftPressed):
        glTranslatef(-move,0,0)
        keyRightPressTimes -= 1
        print("keyLeftPressTime: ", keyRightPressTimes)


    # Up Border Collision
    if (keyUpPressTimes > stepsToBorder):  # If the key is pressed more than stepsToBorder times then reset to Bottom
        keyUpPressTimes = -stepsToBorder
        keyUpPressed = 0
        print("Collision with Up Border")
        glTranslatef(0,move*moveReset*keyUpPressTimes-move,0)

    # Down Border Collision
    elif (keyUpPressTimes < -stepsToBorder):
        keyUpPressTimes = stepsToBorder
        keyUpPressed = 0
        glTranslatef(0,move*moveReset*keyUpPressTimes+move,0)
        print("Collision with Down Border")

    # Right Border Collision
    elif (keyRightPressTimes > stepsToBorder):
        keyRightPressTimes = -stepsToBorder
        keyRightPressed = 0
        glTranslatef(move*moveReset*keyRightPressTimes-move,0,0)
        print("Collision with Right Border")

    # Left Border Collision
    elif (keyRightPressTimes < -stepsToBorder):
        keyRightPressTimes = stepsToBorder
        keyRightPressed = 0
        glTranslatef(move*moveReset*keyRightPressTimes+move,0,0)
        print("Collision with Left Border")

    time.sleep(0.1)
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

# defin Keyboard input
glutSpecialFunc(ProcessSpecialKeys)
glutSpecialUpFunc(ReleaseSpecialKeys)

# Begin event loop
glutMainLoop()

