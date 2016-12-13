# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class spaceCamera:

    #Constructor
    #Camera Mode Definition
    #0 Camera around object(Dew)
    #1 Satellite to Earth(Paco)
    #2 Fixed camera on Earth
    def __init__(self, angle, ratio, near, far, distance, mode, objectList):
        self.cameraDistance = distance
        self.eyeCamera = [self.cameraDistance, 0, 0]
        self.centerCamera = [0, 0, 0]
        self.upCamera = [0, 0, 1]
        self.viewAngle = angle
        self.aspectRatio = ratio
        self.zNear = near
        self.zFar = far
        self.cameraMode = mode
        self.spaceObjectList = objectList
        self.selectedObject = 0
        self.cameraXYTheta = 0
        self.cameraXZTheta = 0
        
        glLoadIdentity()
        gluPerspective(self.viewAngle, self.aspectRatio, self.zNear, self.zFar)
        glDepthFunc(GL_LEQUAL) # LEQUAL
        glEnable(GL_DEPTH_TEST)
        glTranslatef(0.0, 0.0, 0.0)
        glPushMatrix()
        gluLookAt(self.eyeCamera[0], self.eyeCamera[1], self.eyeCamera[2], 
                self.centerCamera[0], self.centerCamera[1], self.centerCamera[2], 
                self.upCamera[0], self.upCamera[1], self.upCamera[2])
        glPopMatrix()


    #Getter Method
    def getEye(self):
        return self.eyeCamera
        
    def getCenter(self):
        return self.centerCamera
        
    def getViewAngle(self):
        return self.viewAngle
        
    def getAspectRatio(self):
        return self.aspectRatio
    
    def getzNear(self):
        return self.zNear
        
    def getzFar(self):
        return self.zFar
        
    def getCameraDistance(self):
        return self.cameraDistance
        
    def getSpaceObjectList(self):
        return self.spaceObjectList
        
    def getCameraXYTheta(self):
        return self.cameraXYTheta
        
    def getCameraXZTheta(self):
        return self.cameraXZTheta
        
    def getCameraMode(self):
        return self.cameraMode
        
    def getSelectedObject(self):
        return self.selectedObject
        
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
        
    def setCameraDistance(self, distance):
        self.cameraDistance = distance
        
    def setSpaceObjectList(self, objectList):
        self.spaceObjectList = objectList
        
    def setSelectedObject(self, selected):
        self.selectedObject = selected
        
    def setCameraXYTheta(self, theta):
        self.cameraXYTheta = theta
        
    def setCameraXZTheta(self, theta):
        self.cameraXZTheta = theta
        
    def setCameraMode(self, mode):
        self.cameraMode = mode
        
    def setSelectedObject(self, selected):
        self.selectedObject = selected
        
    #Update camera position
    def updateCameraPosition(self):
        if self.cameraMode == 0:
            currentPosition = self.spaceObjectList[self.selectedObject].getPosition()
            self.centerCamera[0] = currentPosition[0]
            self.centerCamera[1] = currentPosition[1]
            self.centerCamera[2] = currentPosition[2]
            self.eyeCamera[0] = self.centerCamera[0] + self.cameraDistance * math.cos(self.cameraXYTheta * math.pi / 180) * math.cos(self.cameraXZTheta * math.pi / 180)
            self.eyeCamera[1] = self.centerCamera[1] + self.cameraDistance * math.sin(self.cameraXYTheta * math.pi / 180) * math.cos(self.cameraXZTheta * math.pi / 180)
            self.eyeCamera[2] = self.centerCamera[2] + self.cameraDistance * math.sin(self.cameraXZTheta * math.pi / 180)
    
        elif self.cameraMode == 1:
            print("Satellite to Earth")
        elif self.cameraMode == 2:
            print("Fixed on Earth")
        
        glLoadIdentity()
        gluPerspective(self.viewAngle, self.aspectRatio, self.zNear, self.zFar)
        glTranslatef(0.0, 0.0, 0.0)
        #glPushMatrix()
        gluLookAt(self.eyeCamera[0], self.eyeCamera[1], self.eyeCamera[2], 
                self.centerCamera[0], self.centerCamera[1], self.centerCamera[2], 
                self.upCamera[0], self.upCamera[1], self.upCamera[2])
        #glPopMatrix()
                    
                    
                    
                    
                    
                    
                    
                    
        