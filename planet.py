# -*- coding: utf-8 -*-
from spaceObject import *

class planet(spaceObject):

    #Constructor
    def __init__(self):
        super(planet, self).__init__()
        self.radius = 0
        self.textureFile = "texture/"
        self.spinRate = 0
        
    #Getter Method
    def getRadius(self):
        return self.radius
        
    def getTextureFile(self):
        return self.textureFile
        
    def getSpinRate(self):
        return self.spinRate
        
    #Setter Method
    #Radius size in pixel unit
    def setRadius(self, newRadius):
        self.radius = newRadius
        
    #Enter only file name and put file to texture folder
    def setTextureFile(self, newTextureFile):
        self.textureFile = "texture/" + newTextureFile
        
    def setSpinRate(self, rate):
        self.spinRate = rate