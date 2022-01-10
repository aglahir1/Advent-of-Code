
# Started
# Finished

import math
import copy

f = open('2021/19.txt', 'r')
inputString = f.read()

def listOverlap(l1, l2):
    overlap = []
    for x in l1:
        if math.floor(x[0]) in [math.floor(z[0]) for z in l2]:
            overlap.append(copy.deepcopy(x))
    return overlap

class Beacon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def calcDistance(self, otherbeacon): 
        xdiff = otherbeacon.x - self.x
        ydiff = otherbeacon.y - self.y
        zdiff = otherbeacon.z - self.z
        distance = math.sqrt(xdiff ** 2 + ydiff ** 2 + zdiff ** 2)
        return distance

class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.beacons = []
        for b in beacons:
            self.beacons.append(Beacon(int(b[0]), int(b[1]), int(b[2])))
        self.generateFingerprint()

    def generateFingerprint(self):
        fingerprint = []
        for x in self.beacons:
            groove = []
            for j in self.beacons:
                dist = x.calcDistance(j)
                if dist:
                    groove.append([dist,j])
            fingerprint.append(groove[:])
        self.fingerprint = fingerprint[:]
class Constellation:
    def __init__(self):
        self.beacons = []

    def addBeacon(self, beacon):
        self.beacons.append(beacon)

    def generateFingerprint(self):
        fingerprint = []
        for x in self.beacons:
            groove = []
            for j in self.beacons:
                dist = x.calcDistance(j)
                if dist:
                    groove.append([dist,j])
            fingerprint.append(groove[:])
        self.fingerprint = fingerprint[:]

    def checkOverlap(self, scanner):
        fingerprint1 = copy.deepcopy(self.fingerprint)
        fingerprint2 = copy.deepcopy(scanner.fingerprint)
        matching = False
        for groove in fingerprint1:
            if matching: break
            for groove2 in fingerprint2:
                if len(listOverlap(groove, groove2)) == 12:
                    matching = True
                    break
        return matching


a = Beacon(1, 1, 0)
b = Beacon(2, 1, 2)

print(a.calcDistance(b))

scanners = inputString.split('\n\n')
scannerList = []
for i, s in enumerate(scanners):
    s = s.splitlines()
    beacons = []
    for b in s[1:]:
        beacons.append(b.split(','))
    scannerList.append(Scanner(i, beacons))
    
constellation = Constellation()

for x in scannerList[0].beacons:
    constellation.addBeacon(x)
constellation.generateFingerprint()
scannerList.pop(0)

while scannerList:
    for i, x in enumerate(scannerList):
        if constellation.checkOverlap(x):
            break
    