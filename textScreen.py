# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

class textScreen:

    #Constructor
    def __init__(self, position, text, color, size, radius):
        self.drawPosition = position
        self.textMessage = text
        self.textColor = color
        self.fontSize = size
        self.objectRadius = radius
        
    #Getter Method
    def getDrawPosition(self):
        return self.drawPosition
        
    def getTextMessage(self):
        return self.textMessage
        
    def getTextColor(self):
        return self.textColor
    
    def getFontSize(self):
        return self.fontSize
        
    def getObjectRadius(self):
        return self.objectRadius
        
    #Setter Method
    def setDrawPosition(self, position):
        self.drawPosition = position
        
    def setTextMessage(self, text):
        self.textMessage = text
        
    def setTextColor(self, color):
        self.textColor = color
        
    def setFontSize(self, size):
        self.fontSize = size
        
    def setObjectRadius(self, radius):
        self.objectRadius = radius
        
    def draw(self):
        textBox = pygame.font.Font(None, self.fontSize).render(self.textMessage, 0, self.textColor)  #Create text to show on screen
        textHeight = textBox.get_height() #real calculate text height and width
        textWidth = textBox.get_width()

        glColor(self.textColor)
        glPushMatrix()
        textureData = pygame.image.tostring(textBox, "RGBA", 1)
        glRasterPos3d(self.drawPosition[0], self.drawPosition[1], self.drawPosition[2] + textHeight + self.objectRadius)
        glDrawPixels(textWidth, textHeight, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        glPopMatrix()