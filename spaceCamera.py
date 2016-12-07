# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class spaceCamera:

    #Constructor
    def __init__(self, angle, ratio, near, far, distance):
        self.cameraDistance = distance
        self.eyeCamera = [0, self.cameraDistance, 0]
        self.centerCamera = [0, 0, 0]
        self.upCamera = [0, 0, 1]
        self.viewAngle = angle
        self.aspectRatio = ratio
        self.zNear = near
        self.zFar = far

    #Getter Method
    def getEye(self):
        return self.eyeCamera
        
    def getCenter(self):
        return self.centerCamera
        
    #Setter Method
    def setEye(self, x, y, z):
        self.eyeCamera = [x, y, z]
        
    def setCenter(self, x, y, z):
        self.centerCamera = [x, y, z]
        
    def setViewAngle(self, angle):
        self.viewAngle = angle
        
    def setAspectRatio(self, ratio):
        self.aspectRatio = ration
        
    def setzNear(self, near):
        self.zNear = near
        
    def setzFar(self, far):
        self.zFar = far
        
    #Update camera position
    def updateCameraPosition(self):
        glLoadIdentity()
        gluPerspective(self.viewAngle, self.aspectRatio, self.zNear, self.zFar)
        glTranslatef(0.0,0.0, 0.0)
        gluLookAt(self.eyeCamera[0], self.eyeCamera[1], self.eyeCamera[2], 
                self.centerCamera[0], self.centerCamera[1], self.centerCamera[2], 
                self.upCamera[0], self.upCamera[1], self.upCamera[2])
    