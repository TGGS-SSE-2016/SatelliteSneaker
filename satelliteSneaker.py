# -*- coding: utf-8 -*-
import sys
from solarSystem import *
from spaceCamera import *
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#initialize and calculate some variable setup
glutInit(sys.argv)
pygame.init()
displayInfo = pygame.display.Info() #get resolution size of screen
width = displayInfo.current_w
height = displayInfo.current_h
running = True
clock = pygame.time.Clock()
FPS = 10
cameraXZMaxTheta = 89
cameraXZMinTheta = -89
maxCameraMode = 3 #0-2
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.OPENGL)    #setup screen to fullscreen mode

#Solar System initialize
mySolarSystem = solarSystem(height, 10) #Screen Reference, Frame per day

#texture variable
sunSurf = pygame.image.load(mySolarSystem.getSun().getTextureFile())
sunImage = pygame.image.tostring(sunSurf, "RGB", 1) # Flip image for OpenGL. See pygame doc.
earthSurf = pygame.image.load(mySolarSystem.getEarth().getTextureFile())
earthImage = pygame.image.tostring(earthSurf, "RGB", 1) # Flip image for OpenGL. See pygame doc.
moonSurf = pygame.image.load(mySolarSystem.getMoon().getTextureFile())
moonImage = pygame.image.tostring(moonSurf, "RGB", 1) # Flip image for OpenGL. See pygame doc.

# Defining texture
allTexture = glGenTextures(3)

#Sun texture
glBindTexture(GL_TEXTURE_2D, allTexture[0])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       sunSurf.get_width(),  # width
                       sunSurf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       sunImage)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

#Earth texture
glBindTexture(GL_TEXTURE_2D, allTexture[1])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       earthSurf.get_width(),  # width
                       earthSurf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       earthImage)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

#Moon texture
glBindTexture(GL_TEXTURE_2D, allTexture[2])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       moonSurf.get_width(),  # width
                       moonSurf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       moonImage)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

mySolarSystem.getSun().setTextureID(allTexture[0])
mySolarSystem.getEarth().setTextureID(allTexture[1])
mySolarSystem.getMoon().setTextureID(allTexture[2])

# light setup
light_position = [0.0, 0.0, 0.0, 1.0]
light_ambient = [0.0, 0.0, 0.0, 1.0]
light_diffuse = [height*2, height*2, height*2, height*2]
light_specular = [1.0, 1.0, 1.0, 1.0]

# material setup
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = [100.0]
glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, mat_diffuse)
glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

# light setup
glLightfv(GL_LIGHT0, GL_POSITION, light_position)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.5)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.5)
glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.25)
glEnable(GL_LIGHT0)

glEnable(GL_LIGHTING)

#Camera Setting
allSpaceObject = [mySolarSystem.getSun(), mySolarSystem.getEarth(), mySolarSystem.getMoon()]
cameraObject = spaceCamera(60, (width/height), 1, height*2, height, 0, allSpaceObject)

#Keyboard Handler
def keyboardHandler(mode):
    global cameraObject, cameraXZMaxTheta, cameraXZMinTheta, allSpaceObject, mySolarSystem
    cameraMode = cameraObject.getCameraMode()
    selectedObject = cameraObject.getSelectedObject()
    if mode == 0:
        if cameraMode == 0:
            if cameraObject.getCameraXZTheta() < cameraXZMaxTheta:
                cameraObject.setCameraXZTheta(cameraObject.getCameraXZTheta() + 1)
        elif cameraMode == 1:
            print("Do something")
    elif mode == 1:
        if cameraMode == 0:
            if cameraObject.getCameraXZTheta() > cameraXZMinTheta:
                cameraObject.setCameraXZTheta(cameraObject.getCameraXZTheta() - 1)
        elif cameraMode == 1:
            print("Do something")
    elif mode == 2:
        if cameraMode == 0:
            cameraObject.setCameraXYTheta((cameraObject.getCameraXYTheta() - 1) % 360)
        elif cameraMode == 1:
            print("Do something")
    elif mode == 3:
        if cameraMode == 0:
            cameraObject.setCameraXYTheta((cameraObject.getCameraXYTheta() + 1) % 360)
        elif cameraMode == 1:
            print("Do something")
    elif mode == 4:
        cameraObject.setCameraMode((cameraMode + 1) % maxCameraMode)
    elif mode == 5:
        cameraObject.setCameraMode((cameraMode - 1) % maxCameraMode)
    elif mode == 6:
        cameraObject.setSelectedObject((cameraObject.getSelectedObject() + 1) % len(allSpaceObject))
    elif mode == 7:
        cameraObject.setSelectedObject((cameraObject.getSelectedObject() - 1) % len(allSpaceObject))
    elif mode == 8:
        cameraObject.setCameraDistance(cameraObject.getCameraDistance() - 1)
    elif mode == 9:
        if cameraObject.getCameraDistance() > 0:
            cameraObject.setCameraDistance(cameraObject.getCameraDistance() + 1)
    elif mode == 10:
        mySolarSystem.setFramePerDay(mySolarSystem.getFramePerDay() + 1)
    elif mode == 11:
        if mySolarSystem.getFramePerDay() > 1:
            mySolarSystem.setFramePerDay(mySolarSystem.getFramePerDay() - 1)


#Key Definition
#Up Arrow Camera go Up
#Down Arrow Camera go Down
#Left Arrow Camera go Left
#Right Arrow Camera go Down
#1 Next Camera view
#2 Previous Camera view
#3 Next Object
#4 Previous Object
#Z Camera zoom In
#X Camera zoom Out
#A Increase Frame per day
#S Decrease Frame Per day
#Q Time step Foward
#W Time step Backward
#Event watch dog
while running:
    clock.tick(FPS)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        keyboardHandler(0)
    if pressed[pygame.K_DOWN]:
        keyboardHandler(1)
    if pressed[pygame.K_LEFT]:
        keyboardHandler(2)
    if pressed[pygame.K_RIGHT]:
        keyboardHandler(3)
    if pressed[pygame.K_z]:
        keyboardHandler(8)
    if pressed[pygame.K_x]:
        keyboardHandler(9)
    if pressed[pygame.K_a]:
        keyboardHandler(10)
    if pressed[pygame.K_s]:
        keyboardHandler(11)
    if pressed[pygame.K_q]:
        keyboardHandler(12)
    if pressed[pygame.K_w]:
        keyboardHandler(13)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    mySolarSystem.updateSolarSystem()
    cameraObject.updateCameraPosition()
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glFlush()
    pygame.display.flip()
    for event in pygame.event.get():
        #check event to do something with program
        if pressed[pygame.K_1]:
            keyboardHandler(4)
        if pressed[pygame.K_2]:
            keyboardHandler(5)
        if pressed[pygame.K_3]:
            keyboardHandler(6)
        if pressed[pygame.K_4]:
            keyboardHandler(7)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
