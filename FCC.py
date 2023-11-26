import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import csvoutput as c
import radiussaver as rs


file = "data.txt"
verticies = c.vert
edges = c.edge
face = c.face
positions = c.pos
radius = rs.read(file)
pygame.init()
display = (900, 900)

pygame.display.set_caption('Face Centric Lattice')
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL , 8 , 0, 1)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric() 

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
#its at a distance -12 units in y axis
gluLookAt(0, -12, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
#radius = 0.3
def inject_sphere(x , y, z ,r):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor4f(0.5, 0.2, 0.2, 1)
    gluSphere(sphere, r  , 32, 16)
    glPopMatrix() 

'''
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
positions =(
        (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1), 
    (-1, 1, 1),
    (0,0,0),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (-1,0,0),
    (0,-1,0),
    (0,0,-1)
)
'''
def Cube():
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor4f(0,1,0,1)
    for edge in edges:
        for vertex in edge:
            #print(vertex)
            glVertex3fv(verticies[vertex])
    glEnd()

paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
                exec(open("ui.py").read())
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                
    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # init model view matrix
        glLoadIdentity()

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment 
        if keypress[pygame.K_w]:
            #glTranslatef(0 ,-0.1,0)
            #glRotatef (3, 0, 1, 0)
            radius = radius + 0.01
        if keypress[pygame.K_s]:
            #glTranslatef(0,0,-0.1)
            #glRotatef(-3,0,1,0)
            radius = radius - 0.01
        if keypress[pygame.K_d]:
            glTranslatef(-0.1,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1,0,0)
        if keypress[pygame.K_UP]:
            glTranslatef(0,-0.2,0)
            glRotatef(1 , 1, 0,0)
        if keypress[pygame.K_DOWN]:
            glTranslatef(0,0.2,0)
            glRotatef(-1 , 1, 0,0)
        if keypress[pygame.K_LEFT]:
            glTranslatef(0.2,0,0)
            glRotatef(1 , 0, 1,0)
        if keypress[pygame.K_RIGHT]:
            glTranslatef(-0.2,0,0)
            glRotatef(-1 , 0, 1,0)
        if keypress[pygame.K_1]:
            rs.save(file, radius)

        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #begins the rendering of the 3d stuff
        glPushMatrix()
        Cube()
        glPopMatrix()
        


        for pos in positions:
            inject_sphere(pos[0], pos[1] , pos[2], radius)

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()