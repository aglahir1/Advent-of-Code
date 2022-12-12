
# Started
# Finished

from pprint import pprint
from typing import List
from copy import deepcopy

f = open('2022/12.txt', 'r')
inputString = f.read()

#inputString = """Sabqponm
#abcryxxl
#accszExk
#acctuvwj
#abdefghi"""

class Field:
    pass

class Node:
    pass

class Node:
    x: int
    y: int
    h: int
    visited: bool
    distance: int
    field: Field

    def __init__(self, x: int, y: int, h: int, visited: bool, distance: int, field: Field):
        self.x = x
        self.y = y
        self.h = h
        self.visited = visited
        self.distance = distance
        self.field = field

    def __str__(self) -> str:
        return '{:02d}'.format(self.h)

    def isValidPathFrom(self, otherNode: Node) -> bool:
        return otherNode.h <= self.h + 1

    def isValidPathTo(self, otherNode: Node) -> bool:
        return otherNode.h >= self.h -1

    def getPathsFrom(self) -> List[Node]:
        neighbours: List[Node] = []
        if self.x > 0:
            if self.isValidPathFrom(self.field.getNode(self.x - 1, self.y)): 
                neighbours.append(self.field.getNode(self.x - 1, self.y))
        if self.x < self.field.width - 1:
            if self.isValidPathFrom(self.field.getNode(self.x + 1, self.y)): 
                neighbours.append(self.field.getNode(self.x + 1, self.y))
        if self.y > 0:
            if self.isValidPathFrom(self.field.getNode(self.x, self.y - 1)): 
                neighbours.append(self.field.getNode(self.x, self.y - 1))
        if self.y < self.field.height - 1:
            if self.isValidPathFrom(self.field.getNode(self.x, self.y + 1)): 
                neighbours.append(self.field.getNode(self.x, self.y + 1))
        return neighbours

    
class Field:
    nodes: List[List[Node]]
    currentNode: List[int]
    goalNode: List[int]

    def __init__(self, height: int, width: int):
        self.nodes = [[Node(x, y, 0, False, 9999999999, self) for x in range(width)] for y in range(height)]
        self.height = height
        self.width = width

    def getNode(self, x, y) -> Node:
        return self.nodes[y][x]

    def getCurrentNode(self) -> Node:
        return self.nodes[self.currentNode[1]][self.currentNode[0]]

    def makePossibleStartingNodes(self):
        for y, row in enumerate(self.nodes):
            for x, peak in enumerate(row):
                if peak.h == 1:
                    peak.distance = 0

    def switchToSmallestNode(self):
        d: int = 99999999999999
        n: List[int] = []
        for y, row in enumerate(self.nodes):
            for x, peak in enumerate(row):
                if peak.distance < d and peak.visited == False:
                    d = peak.distance
                    n = [peak.x, peak.y]
        self.currentNode = n

    def __str__(self) -> str:
        rString = ''
        bString = ''
        for row in self.nodes:
            rString += ' '.join([str(x.distance) for x in row]) + '\n'
        return rString

    def run(self, startingNode: List[int]):
        self.currentNode = startingNode
        self.getCurrentNode().distance = 0
        while True:
            self.switchToSmallestNode()
            if self.currentNode == self.goalNode: break
            for n in self.getCurrentNode().getPathsFrom():
                if n.distance > self.getCurrentNode().distance + 1:
                    self.getNode(n.x, n.y).distance = self.getCurrentNode().distance + 1
            self.getCurrentNode().visited = True
        return self.getCurrentNode().distance

xGoal: int
yGoal: int
xStart: int
yStart: int

inputArray = [list(x) for x in inputString.splitlines()]

field = Field(len(inputArray), len(inputArray[0]))


for y, row in enumerate(inputArray):
    for x, peak in enumerate(row):
        if peak == 'E':
            xGoal = x
            yGoal = y
            field.getNode(x, y).h = ord('z') - 96
            field.goalNode = [x, y]
        elif peak == 'S':
            xStart = x
            yStart = y
            field.getNode(x, y).h = ord('a') - 96
        else:
            field.getNode(x, y).h = ord(peak) - 96

fieldone = deepcopy(field)

print(fieldone.run([xStart, yStart]))

fieldtwo = deepcopy(field)

possibleStarts = fieldtwo.makePossibleStartingNodes()
print(fieldtwo.run([xStart, yStart]))