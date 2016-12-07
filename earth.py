# -*- coding: utf-8 -*-
from planet import * 

class earth(planet):
    
    #Class Variable
    #Earth detailed
    earthDiameter = 12742
    earthRadius = earthDiameter/2
    textureFile = "earthmap.jpg"
    quadSlice = 36
    quadStack = 36

    #Constructor
    def __init__(self, rate):
        super(earth, self).__init__()
        self.setRadius(earth.earthRadius)
        self.setSpinRate(rate)
        self.setTextureFile(earth.textureFile)
        self.earthAroundSelfTheta = 0
        self.textureID = 0
        self.radiusDraw = 0
        
        self.quad = gluNewQuadric()
        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)
        
    #Getter Method
    def getDiameter(self):
        return earth.earthDiameter
        
    def getAroundSelfTheta(self):
        return self.earthAroundSelfTheta
        
    def getTextureID(self):
        return self.textureID
        
    def getRadiusDraw(self):
        return self.radiusDraw
        
    #Setter Method
    def setAroundSelfTheta(self, newTheta):
        self.earthAroundSelfTheta = newTheta
        
    def setTextureID(self, newID):
        self.textureID = newID
        
    def setRadiusDraw(self, radius):
        self.radiusDraw = radius
        
    #Draw Earth
    def draw(self):
        #Earth
        earthPosition = self.getPosition()
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textureID)
        glTranslatef(earthPosition[0], earthPosition[1], earthPosition[2])
        glRotate(self.earthAroundSelfTheta, 0, 0, 1)
        gluSphere(self.quad, self.radiusDraw, earth.quadSlice, earth.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        
        