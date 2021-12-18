# Exercise:
#  Modify the code that draws the cone with lighting effect (File cone_template.py) to allow to see a face view of it (like in the previous set of images).
#  Add some animations (e.g. rotation).
#  Add more lights to the scene (at least one).
#  The control of the animation and the lights should be done using keyboard.
#  The parameters of the animation (transformations) should be set at the beginning of the code
# (translation step, rotation angle, scaling factor, light position, shininess level).

# Program that draws a solid Cone with lights
# Adapted by Ammar Assoum

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
    # and then the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5,0,-1,0,0,0,0,0,1)

def light():
	#Setup light 0 and enable lighting
	glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.0, 1.0, 0.0, 1.0))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
	glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
	glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1.0, 1.0, 1.0, 0.0));   
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

def depth():
	#Setup depth testing
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)    

def coneMaterial():
	#Setup material for cone
	glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
	glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
	glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 0.0, 1.0, 1.0))
	glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(50.0))

def transformations():
    pass

def drawCone(radius, height, slices,stacks):
    glPushMatrix()
    glutSolidCone(radius, height, slices, stacks )
    glPopMatrix()   
    
def display():
    background()
    perspective()
    lookat()
    light()
    depth()
    coneMaterial()
    transformations()
    drawCone(1,2,50,10)
    glutSwapBuffers()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Javid Guliyev and Mahir Israyilov")

glClearColor(0.0,0.0,0.0,0.0)

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define display callback
glutDisplayFunc(display)
    
# Begin event loop
glutMainLoop()
