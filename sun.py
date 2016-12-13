# -*- coding: utf-8 -*-
from planet import *

class sun(planet):

    #Class Variable
    #Sun detailed
    sunDiameter = 139140 #original 1391400
    sunRadius = sunDiameter/2
    textureFile = "sunmap.jpg"
    quadSlice = 36
    quadStack = 36

    #Constructor
    def __init__(self, rate):
        super(sun, self).__init__()
        self.setRadius(sun.sunRadius)
        self.setSpinRate(rate)
        self.setTextureFile(sun.textureFile)
        self.sunAroundSelfTheta = 0
        self.textureID = 0
        self.radiusDraw = 0

        self.quad = gluNewQuadric()
        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)

    #Getter Method
    def getDiameter(self):
        return sun.sunDiameter

    def getAroundSelfTheta(self):
        return self.sunAroundSelfTheta

    def getTextureID(self):
        return self.textureID

    def getRadiusDraw(self):
        return self.radiusDraw

    #Setter Method
    def setAroundSelfTheta(self, newTheta):
        self.sunAroundSelfTheta = newTheta

    def setTextureID(self, newID):
        self.textureID = newID

    def setRadiusDraw(self, radius):
        self.radiusDraw = radius

    #Draw Sun
    def draw(self):
        #Sun
        sunPosition = self.getPosition()
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.4,0.4,0.4));
        glBindTexture(GL_TEXTURE_2D, self.textureID)
        glTranslatef(sunPosition[0], sunPosition[1], sunPosition[2])
        glRotate(self.sunAroundSelfTheta, 0, 0, 1)
        gluSphere(self.quad, self.radiusDraw, sun.quadSlice, sun.quadStack)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
