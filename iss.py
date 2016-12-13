# -*- coding: utf-8 -*-
from satellite import *
from spaceObject import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class iss(spaceObject):
    def __init__(self):
        super(iss, self).__init__()
        self.setPosition(220,0,0)
        self.quad = gluNewQuadric()
        self.height = 80
        self.radius = 10
        self.quadSlice = 10
        self.quadStack = 10
        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, self.getSurfaceType()) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH

    def draw(self):
        issPosition = self.getPosition()
        glTranslatef(issPosition[0], issPosition[1], issPosition[2])
        self.makeISS()
        glColor3f(1,1,1)

    def makeISS(self):
        self.makeBody()

    def makeBody(self):
        gluCylinder(self.quad, self.radius, self.radius, self.height, self.quadSlice, self.quadStack)
