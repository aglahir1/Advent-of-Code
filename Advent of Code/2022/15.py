
# Started
# Finished

from pprint import pprint
from typing import List

f = open('2022/15.txt', 'r')
inputString: str = f.read()

testString: str = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


field: dict = {}
# {rowNumber: {colNumber}}

def calculateManhattanDistance(originX: int, originY: int, edgePointX: int, edgePointY: int):
    manhattanDistance: int = abs(originX - edgePointX) + abs(originY - edgePointY)
    return manhattanDistance

def drawManhattanSquare(originX: int, originY: int, edgePointX: int, edgePointY: int):
    manhattanDistance: int = calculateManhattanDistance(originX, originY, edgePointX, edgePointY)
    if not (originY + manhattanDistance > 2000000 > originY - manhattanDistance): return
    for y in list(range(-(manhattanDistance), manhattanDistance + 1))[::-1]:
        if y + originY != 2000000: continue
        for x in range(-(manhattanDistance - abs(y)), manhattanDistance - abs(y) + 1):
            if (x == 0 and y == 0) or (x == edgePointX - originX and y == edgePointY - originY): continue
            if not y + originY in field: field[y + originY] = set()
            field[y + originY].add(x + originX)

def parseInput(inputArray: List[str]):
    outputArray: List[List[int]] = []
    for instruction in inputArray:
        instruction = instruction.split()
        x1: int = int(instruction[2].split('=')[1][:-1])
        y1: int = int(instruction[3].split('=')[1][:-1])
        x2: int = int(instruction[8].split('=')[1][:-1])
        y2: int = int(instruction[9].split('=')[1])
        outputArray.append([x1, y1, x2, y2])
    return outputArray

def partOne(i):
    for sensor in i:
        drawManhattanSquare(sensor[0], sensor[1], sensor[2], sensor[3])
    line = 10
    line = 2000000

    return len(field[line])

def checkIfInRange(originX: int, originY: int, edgePointX: int, edgePointY: int, distanceToCheck: int):
    distance = calculateManhattanDistance(originX, originY, edgePointX, edgePointY)
    return distance <= distanceToCheck

def partTwo(i):
    sensors: List = []
    for sensor in i:
        sensors.append([[sensor[0], sensor[1]], calculateManhattanDistance(sensor[0], sensor[1], sensor[2], sensor[3])])
    for y in range(4000001):
        for x in range(4000001):
            pass
    return 'done'

inputArray = inputString.splitlines()
inputArray = parseInput(inputArray)

#print(partOne(inputArray))

print(partTwo(inputArray))