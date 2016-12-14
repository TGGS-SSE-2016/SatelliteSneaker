# -*- coding: utf-8 -*-
from satellite import *
from spaceObject import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import math

class iss(spaceObject):
    def __init__(self):
        super(iss, self).__init__()
        self.setPosition(220,0,0)
        self.quad = gluNewQuadric()
        self.heightBody = 80
        self.radiusBody = 10
        self.quadSlice = 10
        self.quadStack = 10
        self.spaceshipTexture = "spaceshipmap.jpg"
        self.solarPanelTexture = "solarpanelmap.jpg"

        #texture variable
        self.solarPanelImg = pygame.image.load("texture/"+self.solarPanelTexture)
        self.solarPanelImgString = pygame.image.tostring(self.solarPanelImg, "RGB", 1) # Flip image for OpenGL. See pygame doc.
        self.spaceshipImg = pygame.image.load("texture/"+self.spaceshipTexture)
        self.spaceshipImgString = pygame.image.tostring(self.spaceshipImg, "RGB", 1) # Flip image for OpenGL. See pygame doc.

        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)

    def draw(self):
        issPosition = self.getPosition()
        glTranslatef(issPosition[0], issPosition[1], issPosition[2])
        self.makeISS()
        glColor3f(1,1,1)

    def makeISS(self):
        self.makeBody()
        self.makeSolarPanel()

    def makeSolarPanel(self):
        innerSolar = 20
        outterSolar = 40
        glPushMatrix()
        glTranslatef(0,0,40)
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D,
                        0,
                        GL_RGB,
                        self.solarPanelImg.get_width(),
                        self.solarPanelImg.get_height(),
                        0,
                        GL_RGB,
                        GL_UNSIGNED_BYTE,
                        self.solarPanelImgString)
        gluDisk(self.quad, innerSolar, outterSolar, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D,
                        0,
                        GL_RGB,
                        self.spaceshipImg.get_width(),
                        self.spaceshipImg.get_height(),
                        0,
                        GL_RGB,
                        GL_UNSIGNED_BYTE,
                        self.spaceshipImgString)
        gluCylinder(self.quad, self.radiusBody, self.radiusBody, self.heightBody, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
