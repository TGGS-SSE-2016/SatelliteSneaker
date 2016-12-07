# -*- coding: utf-8 -*-
from solarSystem import *
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#initialize and calculate some variable setup
pygame.init()
displayInfo = pygame.display.Info() #get resolution size of screen
width = displayInfo.current_w
height = displayInfo.current_h
running = True
clock = pygame.time.Clock()
FPS = 60
frame_per_day = 10

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.OPENGL)    #setup screen to fullscreen mode

#Solar System init
mySolarSystem = solarSystem(height, 1)

#texture variable
sun_surf = pygame.image.load(mySolarSystem.getSun().getTextureFile())
sun_image = pygame.image.tostring(sun_surf, "RGB", 1) # Flip image for OpenGL. See pygame doc.
earth_surf = pygame.image.load(mySolarSystem.getEarth().getTextureFile())
earth_image = pygame.image.tostring(earth_surf, "RGB", 1) # Flip image for OpenGL. See pygame doc.
moon_surf = pygame.image.load(mySolarSystem.getMoon().getTextureFile())
moon_image = pygame.image.tostring(moon_surf, "RGB", 1) # Flip image for OpenGL. See pygame doc.

# Defining texture
all_texture = glGenTextures(3)

#Sun texture
glBindTexture(GL_TEXTURE_2D, all_texture[0])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       sun_surf.get_width(),  # width
                       sun_surf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       sun_image)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

#Earth texture
glBindTexture(GL_TEXTURE_2D, all_texture[1])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       earth_surf.get_width(),  # width
                       earth_surf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       earth_image)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

#Moon texture
glBindTexture(GL_TEXTURE_2D, all_texture[2])
glTexImage2D(GL_TEXTURE_2D,
                       0,   # level
                       3,   # components (3 for RGB)
                       moon_surf.get_width(),  # width
                       moon_surf.get_height(),  # height
                       0,   #border
                       GL_RGB, # format
                       GL_UNSIGNED_BYTE,  # type
                       moon_image)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

mySolarSystem.getSun().setTextureID(all_texture[0])
mySolarSystem.getEarth().setTextureID(all_texture[1])
mySolarSystem.getMoon().setTextureID(all_texture[2])

eye_camera = [0, height, 0]
center_camera = [0, 0, 0]
up_camera = [0, 0, 1]

gluPerspective(60, (width/height), 1, height*1.5)
glDepthFunc(GL_LEQUAL) # LEQUAL
glEnable(GL_DEPTH_TEST)
glTranslatef(0.0,0.0, 0.0)
gluLookAt(eye_camera[0], eye_camera[1], eye_camera[2], center_camera[0], center_camera[0], center_camera[0], up_camera[0], up_camera[1], up_camera[2])

#Event watch dog
while running:
    clock.tick(FPS)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    mySolarSystem.updateSolarSystem()
    pygame.display.flip()
    for event in pygame.event.get():
        #check event to do something with program
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()





