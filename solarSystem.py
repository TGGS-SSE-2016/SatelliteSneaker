# -*- coding: utf-8 -*-
import math
from earth import *
from sun import *
from moon import *
from orbitalPath import *

class solarSystem:

    #Class Variable
    earthToSun = 149600 #original 149600000
    earthToMoon = 38440/2 #original 384400
    dayInOneYear = 365
    earthAroundSunDay = 365
    moonAroundEarthDay = 27
    sunAroundItSelfDay = 30
    earthAroundItSelfDay = 1
    
    #Calculate Variable
    
    #Constructor
    def __init__(self, reference, frameDay):
        self.referenceScreen = reference
        self.sun = sun(frameDay)
        self.moon = moon(frameDay)
        self.earth = earth(frameDay)
        self.usageDistance = (self.moon.getDiameter() * 2) + (solarSystem.earthToSun * 2) + (solarSystem.earthToMoon * 2)

        self.drawDistanceScaleUnit = self.referenceScreen / self.usageDistance
        self.sunRadiusDraw = int(self.sun.getRadius() * self.drawDistanceScaleUnit)
        self.earthRadiusDraw = int(self.earth.getRadius() * self.drawDistanceScaleUnit)
        self.moonRadiusDraw = int(self.moon.getRadius() * self.drawDistanceScaleUnit)
        self.earthToSunDraw = int(solarSystem.earthToSun * self.drawDistanceScaleUnit)
        self.earthToMoonDraw = int(solarSystem.earthToMoon * self.drawDistanceScaleUnit)
        self.framePerDay = frameDay
        self.earthSunThetaStep = 360 / (solarSystem.earthAroundSunDay * self.framePerDay)
        self.earthMoonThetaStep = 360 / (solarSystem.moonAroundEarthDay * self.framePerDay)
        self.sunAroundSelfThetaStep = 360 / (solarSystem.sunAroundItSelfDay * self.framePerDay)
        self.earthAroundSelfThetaStep = 360 / (solarSystem.earthAroundItSelfDay * self.framePerDay)
        self.earthSunTheta = 0
        self.earthMoonTheta = 0
        
        print(self.sunRadiusDraw)
        
        self.earth.setRadiusDraw(self.earthRadiusDraw)
        self.sun.setRadiusDraw(self.sunRadiusDraw)
        self.moon.setRadiusDraw(self.moonRadiusDraw)
        self.earthOrbitalPath = orbitalPath(self.sun, self.earthToSunDraw, (0, 0, 255))
        self.moonOrbitalPath = orbitalPath(self.earth, self.earthToMoonDraw, (255, 255, 0))
        
    #Getter Method
    def getFramePerDay(self):
        return self.framePerDay
        
    def getEarth(self):
        return self.earth
        
    def getSun(self):
        return self.sun
        
    def getMoon(self):
        return self.moon
    
    #Setter Method
    def setFramePerDay(self, frameDay):
        self.framePerDay = frameDay
        self.earthSunThetaStep = 360 / (solarSystem.earthAroundSunDay * self.framePerDay)
        self.earthMoonThetaStep = 360 / (solarSystem.moonAroundEarthDay * self.framePerDay)
        self.sunAroundSelfThetaStep = 360 / (solarSystem.sunAroundItSelfDay * self.framePerDay)
        self.earthAroundSelfThetaStep = 360 / (solarSystem.earthAroundItSelfDay * self.framePerDay)
    
    #Calculate Method
    def calculateEarth(self):
        self.earthSunTheta = (self.earthSunTheta + self.earthSunThetaStep) % 360
        self.earth.setAroundSelfTheta((self.earth.getAroundSelfTheta() + self.earthAroundSelfThetaStep) % 360)
        sunPosition = self.sun.getPosition()
        self.earth.setPosition(int(sunPosition[0] + (self.earthToSunDraw * math.cos(self.earthSunTheta * math.pi / 180))), int(sunPosition[1] + (self.earthToSunDraw * math.sin(self.earthSunTheta * math.pi / 180))), 0)
        
    
    def calculateMoon(self):
        self.earthMoonTheta = (self.earthMoonTheta - self.earthMoonThetaStep) % 360
        self.moon.setRotateTheta(self.earth.getAroundSelfTheta())
        earthPosition = self.earth.getPosition()
        self.moon.setPosition(int(earthPosition[0] + (self.earthToMoonDraw * math.cos(self.earthMoonTheta * math.pi / 180))), int(earthPosition[1] + (self.earthToMoonDraw * math.sin(self.earthMoonTheta * math.pi / 180))), 0)

    def calculateSun(self):
        self.sun.setAroundSelfTheta((self.sun.getAroundSelfTheta() + self.sunAroundSelfThetaStep) % 360)
        
    def updateSolarSystem(self):
        self.calculateSun()
        self.calculateEarth()
        self.calculateMoon()
        
        self.sun.draw()
        self.earth.draw()
        self.moon.draw()
        self.earthOrbitalPath.draw()
        self.moonOrbitalPath.draw()
    
    
        
        