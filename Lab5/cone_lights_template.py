# Program that draws a solid Cone with lights
# Adapted by Ammar Assoum

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

# Keyboard controls

# F1 exit
# F2 Rotation
# F3 Control light 1
# F4 Control light 2
# F5 Control Camera




# choise Shape
# "Teapot" , "Cone","Sphere","Cube",
ShapeType ="Teapot"


# animation mode
# 1 Rotation, 5 Control Light 1, 6 Control Light , 4 Eye ,
animationMode=5

# eye motion
eyeX = 0
eyeY = -1
eyeZ = 5
eyeMotionSpeed = 0.1


# Keyboard controls
# Events that measue Button press and release
keyUp = False
keyDown = False
keyRight = False
keyLeft = False
keyFront = False
keyBack = False

func1 = False
func2 = False
func3 = False
func4 = False
func5 = False

# Count of keys pressed
KeyPressY = 0
KeyPressX = 0
KeyPressZ = 0


# Traslation Params
move = 0.1  # movement speed
stepsToBorder = 20 # Steps To Border
moveReset = move*stepsToBorder*2  # This is writen because we assume that the window is Square if not we need to create Up and Right borders seperately

translationStep = 0.1

scalingFactor = 200
shininessLevel = 50

#Rotation params
angle = 0 # Roation start angle
rotationScale = 1 # degrees per SleepTime(seconds)
rotX = 0
rotY = 0
rotZ = 0

sleepTime = 0.02 # seconds

# Light 1 Red Light
light_ambient1 = [1.0, 0.0, 0.0, 1.0]
light_diffuse1 = [1.0, 0.0, 0.0, 1.0]
light_specular1 = [1.0, 1.0, 1.0, 1.0]
light_posioion1 = [1.0, 1.0, 1.0, 0.0]

# Light 2 Blue Light
light_ambient2 = [0.0, 0.0, 1.0, 1.0]
light_diffuse2 = [0.0, 0.0, 1.0, 1.0]
light_specular2 = [1.0, 1.0, 1.0, 1.0]
light_posioion2 = [-1.0, 1.0, 1.0, 0.0]

def background():
    # Set the background color of the window to Gray
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def perspective():
    # establish the projection matrix (perspective)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Get the viewport  to use it in chosing the aspect ratio of gluPerspective
    _,_,width,height = glGetDoublev(GL_VIEWPORT) # we don't need x and y
    gluPerspective(45,width/height,0.25,200)

def lookat():
    global eyeX
    global eyeY
    global eyeZ
    # and then the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eyeX,eyeY,eyeZ,0,0,0,0,1,0)


def light1():
	#Setup light 0 and enable lighting
	glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(light_ambient1[0], light_ambient1[1], light_ambient1[2], light_ambient1[3]))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(light_diffuse1[0], light_diffuse1[1], light_diffuse1[2], light_diffuse1[3]))
	glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(light_specular1[0], light_specular1[1], light_specular1[2], light_specular1[3]))
	glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(light_posioion1[0], light_posioion1[1], light_posioion1[2], light_posioion1[3]))   
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

def light2():
    #Setup light 1 and enable lighting
    glLightfv(GL_LIGHT1, GL_AMBIENT, GLfloat_4(light_ambient2[0], light_ambient2[1], light_ambient2[2], light_ambient2[3]))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, GLfloat_4(light_diffuse2[0], light_diffuse2[1], light_diffuse2[2], light_diffuse2[3]))
    glLightfv(GL_LIGHT1, GL_SPECULAR, GLfloat_4(light_specular2[0], light_specular2[1], light_specular2[2], light_specular2[3]))
    glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(light_posioion2[0], light_posioion2[1], light_posioion2[2], light_posioion2[3]))   
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.9, 0.9, 1.0))
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHTING)

def depth():
	#Setup depth testing
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)    

def coneMaterial():
	#Setup material for cone
	glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
	glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(0.5, 0.5, 0.5, 1.0))
	glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(shininessLevel))

def transformations():
    # Setting Rotation animation
    glRotatef(rotX,0,1,0)
    glRotatef(rotY,1,0,0)
    glRotatef(rotZ,0,0,1)

def drawObject():
    glPushMatrix()
    if ShapeType == "Cone":
        glutSolidCone(1,2,50,10 )
    elif ShapeType == "Sphere":
        glutSolidSphere(1,50,50)
    elif ShapeType == "Cube":
        glutSolidCube(1)
    elif ShapeType == "Teapot":
        glutSolidTeapot(1)
    glPopMatrix()   
    
def display():
    background()
    perspective()
    lookat()
    light1()
    light2()
    depth()
    coneMaterial()
    transformations()
    drawObject()
    Scaling()
    glutSwapBuffers()

def Traslation():
    global KeyPressX
    global KeyPressY
    global KeyPressZ

    global moveReset

    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global move
    
    # Up
    if (keyUp):
        glTranslatef(0,move,0)
        KeyPressY += 1
        print("KeyPressY: ", KeyPressY)
    
    # Down
    elif (keyDown):
        glTranslatef(0,-move,0)
        KeyPressY -= 1
        print("KeyPressY: ", KeyPressY)
    
    # Right
    elif (keyRight):
        glTranslatef(move,0,0)
        KeyPressX += 1
        print("KeyPressX: ", KeyPressX)

    # Left
    elif (keyLeft):
        glTranslatef(-move,0,0)
        KeyPressX -= 1
        print("KeyPressX: ", KeyPressX)
    
    # Front
    elif (keyFront):
        glTranslatef(0,0,move)
        KeyPressZ += 1
        print("KeyPressZ: ", KeyPressZ)
    
    # Back
    elif (keyBack):
        glTranslatef(0,0,-move)
        KeyPressZ -= 1
        print("KeyPressZ: ", KeyPressZ)

    
    # Up Border Collision
    if (KeyPressY > stepsToBorder):  # If the key is pressed more than stepsToBorder times then reset to Bottom
        keyUpPressTimes = -stepsToBorder
        keyUpPressed = 0
        print("Collision with Up Border")
        glTranslatef(0,move*moveReset*keyUpPressTimes-move,0)

    # Down Border Collision
    elif (KeyPressY < -stepsToBorder):
        keyUpPressTimes = stepsToBorder
        keyUpPressed = 0
        glTranslatef(0,move*moveReset*keyUpPressTimes+move,0)
        print("Collision with Down Border")

    # Right Border Collision
    elif (KeyPressX > stepsToBorder):
        keyRightPressTimes = -stepsToBorder
        keyRightPressed = 0
        glTranslatef(move*moveReset*keyRightPressTimes-move,0,0)
        print("Collision with Right Border")

    # Left Border Collision
    elif (KeyPressX < -stepsToBorder):
        keyRightPressTimes = stepsToBorder
        keyRightPressed = 0
        glTranslatef(move*moveReset*keyRightPressTimes+move,0,0)
        print("Collision with Left Border")

    # Front Border Collision
    elif (KeyPressZ > stepsToBorder):
        keyFrontPressTimes = -stepsToBorder
        keyFrontPressed = 0
        glTranslatef(0,0,move*moveReset*keyFrontPressTimes-move)
        print("Collision with Front Border")

    # Back Border Collision
    elif (KeyPressZ < -stepsToBorder):
        keyFrontPressTimes = stepsToBorder
        keyFrontPressed = 0
        glTranslatef(0,0,move*moveReset*keyFrontPressTimes+move)
        print("Collision with Back Border")

def Scaling():
    glScalef(scalingFactor,scalingFactor,scalingFactor)
    

def Rotation():
    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global rotX
    global rotY
    global rotZ

    if keyUp:
        rotY += rotationScale
    if keyDown:
        rotY -= rotationScale
    if keyRight:
        rotX += rotationScale
    if keyLeft:
        rotX -= rotationScale
    if keyFront:
        rotZ += rotationScale
    if keyBack:
        rotZ -= rotationScale

    global angle
    angle += rotationScale
    if (angle > 360):
        angle = 0

def EyePosition():
    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global eyeX
    global eyeY
    global eyeZ

    if keyUp:
        eyeY += eyeMotionSpeed
    if keyDown:
        eyeY -= eyeMotionSpeed
    if keyRight:
        eyeX += eyeMotionSpeed
    if keyLeft:
        eyeX -= eyeMotionSpeed
    if keyFront:
        eyeZ += eyeMotionSpeed
    if keyBack:
        eyeZ -= eyeMotionSpeed

def LightPosition(position):
    lightMotionSpeed = 0.1

    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global light_posioion1
    global light_posioion2
    

    if keyUp:
        position[1] += lightMotionSpeed
    if keyDown:
        position[1] -= lightMotionSpeed
    if keyRight:
        position[0] += lightMotionSpeed
    if keyLeft:
        position[0] -= lightMotionSpeed
    if keyFront:
        position[2] += lightMotionSpeed
    if keyBack:
        position[2] -= lightMotionSpeed

    return position


def idle():
# F1 exit
# F2 Rotation
# F3 Control light 1
# F4 Control light 2
# F5 Control Camera
    global light_posioion1
    global light_posioion2

    global func1
    global func2
    global func3
    global func4
    global func5
    
    if func1:
        pass
        func1 = False
        func2 = False
        func3 = False
        func4 = False
        func5 = False
    elif func2:
        print("Rotation")
        Rotation()
    elif func3:
        print("Light 1")
        light_posioion1 = LightPosition(light_posioion1)
    elif func4:
        print("Light 2")
        light_posioion2 = LightPosition(light_posioion2)
    elif func5:
        print("Camera")
        EyePosition()
        # Traslation()
    
    time.sleep(sleepTime)
    glutPostRedisplay()

# Button Press
def ProcessSpecialKeys(key,  x,  y):
    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global func1
    global func2
    global func3
    global func4
    global func5

    print("Key: ", key)

    if key == GLUT_KEY_UP:
        keyUp = True
    elif key == GLUT_KEY_DOWN:
        keyDown = True
    elif key == GLUT_KEY_RIGHT:
        keyRight = True
    elif key == GLUT_KEY_LEFT:
        keyLeft = True
    elif key == GLUT_KEY_PAGE_UP:
        keyFront = True
    elif key == GLUT_KEY_PAGE_DOWN:
        keyBack = True
    elif key == GLUT_KEY_F1:
        func1 = True
    elif key == GLUT_KEY_F2:
        func2 = True
    elif key == GLUT_KEY_F3:
        func3 = True
    elif key == GLUT_KEY_F4:
        func4 = True
    elif key == GLUT_KEY_F5:
        func5 = True
    else:
        print("Unknown key pressed")


# Button Release
def ReleaseSpecialKeys(key,  x,  y):
    global keyUp
    global keyDown
    global keyRight
    global keyLeft
    global keyFront
    global keyBack
    global func1
    global func2
    global func3
    global func4
    global func5


    if key == GLUT_KEY_UP:
        keyUp = False
    elif key == GLUT_KEY_DOWN:
        keyDown = False
    elif key == GLUT_KEY_RIGHT:
        keyRight = False
    elif key == GLUT_KEY_LEFT:
        keyLeft = False
    elif key == GLUT_KEY_PAGE_UP:
        keyFront = False
    elif key == GLUT_KEY_PAGE_DOWN:
        keyBack = False
    # elif key == GLUT_KEY_F1:
    #     func1 = False
    # elif key == GLUT_KEY_F2:
    #     func2 = False
    # elif key == GLUT_KEY_F3:
    #     func3 = False
    # elif key == GLUT_KEY_F4:
    #     func4 = False
    # elif key == GLUT_KEY_F5:
    #     func5 = False
    

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Set the initial window position to (50, 50)
glutInitWindowPosition(150, 150)

# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov")

glClearColor(0.0,0.0,0.0,0.0)

# Define display callback
glutDisplayFunc(display)

# define the idle callback
glutIdleFunc(idle)

# defin Keyboard input
glutSpecialFunc(ProcessSpecialKeys)
glutSpecialUpFunc(ReleaseSpecialKeys)
    
# Begin event loop
glutMainLoop()
