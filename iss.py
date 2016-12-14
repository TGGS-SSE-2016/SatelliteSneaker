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
        self.spaceshipTexture1 = "spaceshipmap1.jpg"
        self.spaceshipTexture2 = "spaceshipmap2.jpg"
        self.spaceshipTexture3 = "spaceshipmap3.jpg"
        self.solarPanelTexture = "solarpanelmap.jpg"

        self.solarPanelImg = pygame.image.load("texture/"+self.solarPanelTexture)
        self.solarPanelImgString = pygame.image.tostring(self.solarPanelImg, "RGB", 1)

        self.spaceshipImg1 = pygame.image.load("texture/"+self.spaceshipTexture1)
        self.spaceshipImgString1 = pygame.image.tostring(self.spaceshipImg1, "RGB", 1)

        self.spaceshipImg2 = pygame.image.load("texture/"+self.spaceshipTexture2)
        self.spaceshipImgString2 = pygame.image.tostring(self.spaceshipImg2, "RGB", 1)

        self.spaceshipImg3 = pygame.image.load("texture/"+self.spaceshipTexture3)
        self.spaceshipImgString3 = pygame.image.tostring(self.spaceshipImg3, "RGB", 1)

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
        self.makeSolarPanelLeft3()
        self.makeSolarPanelRight3()
        self.makeSolarPanelLeft4()
        self.makeSolarPanelRight4()

        self.makeSolarPanelLeft5()
        self.makeSolarPanelRight5()
        self.makeSolarPanelLeft6()
        self.makeSolarPanelRight6()

    def makeSolarPanelLeft1(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,0)
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
        glTranslatef(0,-bodyToSolarPanel,0)
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
        glTranslatef(0,bodyToSolarPanel,20)
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
        glTranslatef(0,-bodyToSolarPanel,20)
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

    def makeSolarPanelLeft3(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,self.heightBody-20)
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

    def makeSolarPanelRight3(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,-bodyToSolarPanel,self.heightBody-20)
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

    def makeSolarPanelLeft4(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,bodyToSolarPanel,self.heightBody)
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

    def makeSolarPanelRight4(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(0,-bodyToSolarPanel,self.heightBody)
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

    def makeSolarPanelLeft5(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(self.heightBody//3,self.heightBody//2 ,self.heightBody//2+outterSolar)
        glScalef(1,1,1);
        glRotate(90, 0, 0, 1)
        glRotate(90, 1, 0, 0)
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

    def makeSolarPanelRight5(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(self.heightBody//3,self.heightBody//2 ,(self.heightBody//2+outterSolar)-self.radiusBody-outterSolar-30)
        glScalef(1,1,1);
        glRotate(90, 0, 0, 1)
        glRotate(90, 1, 0, 0)
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

    def makeSolarPanelLeft6(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(self.heightBody//3-10,self.heightBody//2 ,self.heightBody//2+outterSolar)
        glScalef(1,1,1);
        glRotate(90, 0, 0, 1)
        glRotate(90, 1, 0, 0)
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

    def makeSolarPanelRight6(self):
        innerSolar = 0
        outterSolar = 40
        sliceSolar = 4
        stackSolar = 4
        bodyToSolarPanel = 40
        glPushMatrix()
        glTranslatef(self.heightBody//3-10,self.heightBody//2 ,(self.heightBody//2+outterSolar)-self.radiusBody-outterSolar-30)
        glScalef(1,1,1);
        glRotate(90, 0, 0, 1)
        glRotate(90, 1, 0, 0)
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
        self.makeBody3()

    def makeBody1(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
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
        gluCylinder(self.quad, self.radiusBody, self.radiusBody, self.heightBody, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody2(self):
        radius = self.radiusBody-2
        glPushMatrix()
        glTranslatef(self.radiusBody,self.heightBody//2 ,self.heightBody//2)
        glScalef(1,1,1);
        glRotate(90, 1, 0, 0)
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
        gluCylinder(self.quad, radius, radius, self.heightBody//2+30, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def makeBody3(self):
        radius = self.radiusBody-5
        glPushMatrix()
        glTranslatef(self.radiusBody,self.heightBody//2 ,self.heightBody//2)
        glScalef(1,1,1);
        glRotate(90, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D,
                        0,
                        GL_RGB,
                        self.spaceshipImg3.get_width(),
                        self.spaceshipImg3.get_height(),
                        0,
                        GL_RGB,
                        GL_UNSIGNED_BYTE,
                        self.spaceshipImgString3)
        gluCylinder(self.quad, radius, radius, self.heightBody//3, self.quadSlice, self.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
