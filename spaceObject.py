# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class spaceObject:

    #Constructor
    def __init__(self):
        self.position = [0, 0, 0] #Position in x, y, z
        self.surfaceType = GLU_SMOOTH

    #Getter Method
    def getPosition(self):
        return self.position

    def getSurfaceType(self):
        return self.surfaceType

    #Setter Method
    #x, y, z can be any number
    def setPosition(self, x, y, z):
        self.position = [x, y, z]

    #Type can be GLU_NONE , GLU_FLAT , and GLU_SMOOTH
    def setSurfaceType(self, newType):
        self.surfaceType = newType
