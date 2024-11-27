
# Started
# Finished

import re


f = open('2016/22.txt', 'r')
inputString = f.read()

# inputString = """root@ebhq-gridcenter# df -h
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%"""


nodepathreg = re.compile(r'^/dev/grid/node-x(\d+)-y(\d+)$')

class Node:
    def __init__(self, line):
        line = line.split()
        match = nodepathreg.match(line[0])
        self.x = int(match.group(1))
        self.y = int(match.group(2))
        self.cap = int(line[1][:-1])
        self.used = int(line[2][:-1])
        
    def fits(self, data):
        return data < self.cap - self.used
    
    def __str__(self):
        return 'node at x: ' + str(self.x) + ', y: ' + str(self.y) + ', cap: ' + str(self.cap) + ', used: ' + str(self.used)
        

def partOne(i):
    count = 0
    for n in i:
        if n.used == 0: continue
        for c in i:
            if n.x == c.x and n.y == c.y: continue
            if c.fits(n.used): count += 1
    return count

def partTwo(i):
    m = [['_' for _ in range(32)] for _ in range(31)]
    for n in i:
        c = '_'
        if n.used == 0:
            c = 'O'
        if n.cap > 200:
            c = '#'
        m[n.y][n.x] = c
    for l in m:
        print(''.join(l))

inputNodes = []

for n in inputString.splitlines()[2:]:
    inputNodes.append(Node(n))

print(partOne(inputNodes))

print(partTwo(inputNodes))
