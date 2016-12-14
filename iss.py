# -*- coding: utf-8 -*-
from satellite import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import math

class iss(satellite):
    def __init__(self):
        super(iss, self).__init__()
        self.setPosition(220,0,0)
        self.quad = gluNewQuadric()
        self.heightBody = 180
        self.radiusBody = 10
        self.quadSlice = 5
        self.quadStack = 5
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
        glPushMatrix()
        issPosition = self.getPosition()
        glTranslatef(issPosition[0], issPosition[1], issPosition[2])
        self.makeISS()
        glColor3f(1,1,1)
        glPopMatrix()

    def makeISS(self):
        self.makeBody()
        self.makeSolarPanel()

    def makeSolarPanel(self):
        self.makeSolarPanelLeft1()
        self.makeSolarPanelRight1()
        self.makeSolarPanelLeft2()
        self.makeSolarPanelRight2()

    def makeSolarPanelLeft1(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,self.heightBody//5)
        glScalef(1,1,1);
        glRotate(45, 0, 0, 1)
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

    def makeSolarPanelRight1(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,-bodyToSolarPanel,self.heightBody//5)
        glScalef(1,1,1);
        glRotate(45, 0, 0, 1)
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

    def makeSolarPanelLeft2(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,self.heightBody//5+20)
        glScalef(1,1,1);
        glRotate(45, 0, 0, 1)
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

    def makeSolarPanelRight2(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,-bodyToSolarPanel,self.heightBody//5+20)
        glScalef(1,1,1);
        glRotate(45, 0, 0, 1)
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
        glTranslatef(0,self.heightBody//4 ,self.heightBody)
        glScalef(1,1,1);
        glRotate(90, 1, 0, 0)
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
        gluCylinder(self.quad, self.radiusBody, self.radiusBody, self.heightBody//2, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody2(self):
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
