# -*- coding: utf-8 -*-
from spaceObject import *

class orbitalPath(spaceObject):

    #Class Variable
    #Orbital detailed
    quadSlice = 50
    quadStack = 50

    #Constructor
    def __init__(self, around, radius, color):
        super(orbitalPath, self).__init__()
        self.orbitAround = around
        self.orbitalRadius = radius
        self.orbitalColor = color
        
        self.quad = gluNewQuadric()
        gluQuadricDrawStyle(self.quad, GLU_SILHOUETTE) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        
    #Getter Method
    def getRadius(self):
        return self.orbitalRadius
        
    def getOrbitAround(self):
        return self.orbitAround
        
    def getOrbitalColor(self):
        return self.orbitalColor
        
    #Setter Method
    #Radius size in pixel unit
    def setRadius(self, newRadius):
        self.orbitalRadius = newRadius
        
    def setOrbitAround(self, newAround):
        self.orbitAround = newAround
        
    def setOrbitalColor(self, color):
        self.orbitalColor = color
        
    #Draw Orbital Path
    def draw(self):
        position = self.orbitAround.getPosition()
        glPushMatrix()
        glColor(self.orbitalColor)
        glTranslatef(position[0], position[1], position[2])
        gluDisk(self.quad, 0, self.orbitalRadius, orbitalPath.quadSlice, orbitalPath.quadStack)
        glColor((255, 255, 255))
        glPopMatrix()
    