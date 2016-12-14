# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from satellite import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import math

class theos(satellite):
    def __init__(self):
        super(theos, self).__init__()
        self.setPosition(220,200,0)
        self.quad = gluNewQuadric()
        self.heightBody = 50
        self.radiusBody = 30
        self.quadSlice = 6
        self.quadStack = 6
        self.spaceshipTexture1 = "yellowmap3.jpg"
        self.spaceshipTexture2 = "yellowmap2.jpg"
        self.solarPanelTexture = "solarpanelmap.jpg"

        self.solarPanelImg = pygame.image.load("texture/"+self.solarPanelTexture)
        self.solarPanelImgString = pygame.image.tostring(self.solarPanelImg, "RGB", 1)

        self.spaceshipImg1 = pygame.image.load("texture/"+self.spaceshipTexture1)
        self.spaceshipImgString1 = pygame.image.tostring(self.spaceshipImg1, "RGB", 1)

        self.spaceshipImg2 = pygame.image.load("texture/"+self.spaceshipTexture2)
        self.spaceshipImgString2 = pygame.image.tostring(self.spaceshipImg2, "RGB", 1)


        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)

    def draw(self):
        glPushMatrix()
        theosPosition = self.getPosition()
        glTranslatef(theosPosition[0], theosPosition[1], theosPosition[2])
        self.makeTheos()
        glColor3f(1,1,1)
        glPopMatrix()

    def makeTheos(self):
        self.makeBody()
        self.makeSolarPanel()

    def makeSolarPanel(self):
        self.makeSolarPanelLeft1()

    def makeSolarPanelLeft1(self):
        innerSolar = 0
        outterSolar = 50
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = self.radiusBody//2+15
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,30)
        glScalef(1,1,1)
        glRotate(90, 0, 0, 1)
        glRotate(45, 1, 0, 0)
        glRotate(90, 0, 1, 0)
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
        gluDisk(self.quad, innerSolar, outterSolar, sliceSolar, stackSolar  )
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody(self):
        self.makeBody1()
        self.makeBody2()

    def makeBody1(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D,
                        0,
                        GL_RGB,
                        self.spaceshipImg1.get_width(),
                        self.spaceshipImg1.get_height(),
                        0,
                        GL_RGB,
                        GL_UNSIGNED_BYTE,
                        self.spaceshipImgString1)
        gluCylinder(self.quad, self.radiusBody, self.radiusBody, self.heightBody, self.quadSlice, self.quadStack)
        gluDisk(self.quad, 0, self.radiusBody, self.quadSlice, self.quadStack)
        glTranslatef(0, 0, self.heightBody)
        gluDisk(self.quad, 0, self.radiusBody, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody2(self):
        radius = 15
        glPushMatrix()
        sliceBody = 8
        stackBody = 8
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
        glTranslatef(0, (self.radiusBody+20)//2, self.heightBody+radius//2)
        glScalef(1,1,1)
        glRotate(90, 1, 0, 0)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D,
                        0,
                        GL_RGB,
                        self.spaceshipImg2.get_width(),
                        self.spaceshipImg2.get_height(),
                        0,
                        GL_RGB,
                        GL_UNSIGNED_BYTE,
                        self.spaceshipImgString2)
        gluCylinder(self.quad, radius, radius, self.radiusBody+20, sliceBody, stackBody)
        gluCylinder(self.quad, radius-5, radius-5, self.radiusBody+20, sliceBody, stackBody)
        gluDisk(self.quad, radius-5, radius, sliceBody, stackBody)
        glTranslatef(0, 0, self.heightBody)
        gluDisk(self.quad, 0, radius-5, sliceBody, stackBody)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
