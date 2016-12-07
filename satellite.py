# -*- coding: utf-8 -*-

class satellite(spaceObject):

    #Constructor
    def __init__(self):
        super(satellite, self).__init__()
        self.TLE = ""
        self.lattitude = 0
        self.longtitude = 0
    
    #Getter Method
    def getTLE(self):
        return self.TLE
        
    def getALT(self, date):
        return None
        
    def convertToXYZ(self, alt):
        return None
        
    def setTLE(self, newTLE):
        self.TLE = newTLE