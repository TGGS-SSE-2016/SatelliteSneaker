from __future__ import print_function   # PEP 3105: Make print a function

import math
import time
from datetime import datetime, timedelta
import sys
import os.path
import ephem
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import geocoder

from spaceObject import *

try:
    from urllib.request import URLopener
except ImportError:
    from urllib import URLopener

try:
    input = raw_input
except NameError:
    pass

class satellite(spaceObject):

    #Class Variable
    #Satellite variable
    distanceFromEarth = 3578 + (38440/2) #original 35780

    #Constructor
    def __init__(self):
        super(satellite, self).__init__()        
        self.tleSource = [
                            {
                             'name':  'Default',
                             'file':  'tle.txt',
                            },
                           ]
        self.saveSatellite = self.processTLEdata(self.tleSource)
        self.lattitude = 0
        self.longtitude = 0
        self.home = ephem.Observer()
        self.drawScale = 0

    def getTLE(self,id):
        return None

    def getALT(self, id):
        satelligeInfo = self.saveSatellite[id]
        self.home.date = datetime.utcnow()
        satelligeInfo['body'].compute(self.home)
        alt = satelligeInfo['body']
        return alt
    
    def getDrawScale(self):
        return self.drawScale

    def convertToXYZ(self, alt, earthPosition):
        xyzPosition = []
        xyTheta = alt.sublat / ephem.degree
        xzTheta = alt.sublong / ephem.degree
        xyzPosition.append(earthPosition[0] + satellite.distanceFromEarth * self.drawScale * math.cos(xyTheta * math.pi / 180) * math.cos(xzTheta * math.pi / 180))
        xyzPosition.append(earthPosition[1] + satellite.distanceFromEarth * self.drawScale * math.sin(xyTheta * math.pi / 180) * math.cos(xzTheta * math.pi / 180))
        xyzPosition.append(earthPosition[2] + satellite.distanceFromEarth * self.drawScale * math.sin(xzTheta * math.pi / 180))
        return xyzPosition

    def setTLE(self, newTLE=None):
        self.saveSatellite =  self.processTLEdata(self.tleSource)
        
    def setDrawScale(self, scale):
        self.drawScale = scale

    def readTLEFile(self, source):
        ''' Read a TLE file (unzip if necessary) '''
        sourceName = source['name']
        sourceFile = source['file']

        tempContent = []
        with open(sourceFile) as f:
            for aline in f:
                tempContent.append(aline.replace('\n', ''))
            print(len(tempContent) // 3,
                  'TLEs loaded from {}'.format(sourceFile))

        return tempContent

    def processTLEdata(self, tleSource):
        ''' Process each TLE entry '''
        sats = []
        for source in tleSource:
            print("Processing {}".format(source['name']))
            tempContent = self.readTLEFile(source=source)
            print()
            if tempContent:
                i_name = 0
                while 3 * i_name + 2 <= len(tempContent):
                    rawTLEname = tempContent[3 * i_name + 0]
                    rawTLEdat1 = tempContent[3 * i_name + 1]
                    rawTLEdat2 = tempContent[3 * i_name + 2]
                    partsTLEdat1 = rawTLEdat1.split()
                    try:
                        body = ephem.readtle(rawTLEname, rawTLEdat1, rawTLEdat2)
                    except ValueError:
                        print("Error: line does not conform to tle format")
                        print("       " + rawTLEname)
                        print("       " + rawTLEdat1)
                        print("       " + rawTLEdat2)
                        print()
                    else:
                        name = body.name
                        number = partsTLEdat1[1]
                        designator = partsTLEdat1[2]
                        sats.append({'name': name,
                                     'number': number,
                                     'designator': designator,
                                     'body': body, })
                    i_name += 1
        return sats
