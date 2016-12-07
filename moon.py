# -*- coding: utf-8 -*-
from planet import * 

class moon(planet):
    
    #Class Variable
    #Moon detailed
    moonDiameter = 3474
    moonRadius = moonDiameter/2
    textureFile = "moonmap.jpg"
    quadSlice = 36
    quadStack = 36

    #Constructor
    def __init__(self, rate):
        super(moon, self).__init__()
        self.setRadius(moon.moonRadius)
        self.setSpinRate(rate)
        self.setTextureFile(moon.textureFile)
        self.textureID = 0
        self.radiusDraw = 0
        self.rotateTheta = 0
        
        self.quad = gluNewQuadric()
        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)
        
    #Getter Method
    def getDiameter(self):
        return moon.moonDiameter
        
    def getRadiusDraw(self):
        return self.radiusDraw
        
    def getTextureID(self):
        return self.textureID
        
    def getRotateTheta(self):
        return self.rotateTheta
        
    #Setter Method
    def setTextureID(self, newID):
        self.textureID = newID
        
    def setRadiusDraw(self, radius):
        self.radiusDraw = radius
        
    def setRotateTheta(self, theta):
        self.rotateTheta = theta
        
    #Draw Moon
    def draw(self):
        #Moon
        moonPosition = self.getPosition()
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textureID)
        glTranslatef(moonPosition[0], moonPosition[1], moonPosition[2])
        glRotate(self.rotateTheta - 180, 0, 0, 1)
        gluSphere(self.quad, self.radiusDraw, moon.quadSlice, moon.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
    
    
    
    
    
    
    