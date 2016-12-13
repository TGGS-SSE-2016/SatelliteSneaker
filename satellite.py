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

try:
    from urllib.request import URLopener
except ImportError:
    from urllib import URLopener

try:
    input = raw_input
except NameError:
    pass

class satellite():

    #Constructor
    def __init__(self):
        super(satellite, self).__init__()
        self.tleSource = [
                            {
                             'name':  'Default',
                             'file':  'tle.txt',
                            },
                           ]
        self.saveSatellite = ""
        self.lattitude = 0
        self.longtitude = 0
        self.home = ephem.Observer()

    #Getter Method
    def getTLE(self,id):
        return None

    def getALT(self, id):
        satelligeInfo = self.saveSatellite[id]
        self.home.date = datetime.utcnow()
        satelligeInfo['body'].compute(home)
        alt = satelligeInfo['body']

        return alt


    def convertToXYZ(self, alt):
        return None

    def setTLE(self, newTLE=None):
        self.saveSatellite =  self.processTLEdata(self.tleSource)

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
            tempContent = self.readTLEfile(source=source)
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
                                     'color': source['color'],
                                     'body': body, })
                    i_name += 1
        return sats
