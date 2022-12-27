
# Started
# Finished

from pprint import pprint
from typing import List
import time

start = time.time()

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

def drawManhattanSquare(originX: int, originY: int, edgePointX: int, edgePointY: int, line: int):
    manhattanDistance: int = calculateManhattanDistance(originX, originY, edgePointX, edgePointY)
    if not (originY + manhattanDistance > line > originY - manhattanDistance): return
    for y in list(range(-(manhattanDistance), manhattanDistance + 1))[::-1]:
        if y + originY != line: continue
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
    line = 10
    line = 2000000
    for sensor in i:
        drawManhattanSquare(sensor[0], sensor[1], sensor[2], sensor[3], line)
    return len(field[line])

def checkIfInRange(originX: int, originY: int, edgePointX: int, edgePointY: int, distanceToCheck: int):
    distance = calculateManhattanDistance(originX, originY, edgePointX, edgePointY)
    return distance <= distanceToCheck

def findBorderForSensor(originX, originY, radius):
    border = {}
    for y in range(-radius - 1, radius + 2):
        if not (0 < originY + y < 4000000): continue
        width = [-(radius - abs(y) + 1), radius - abs(y) + 2]
        border[originY + y] = []
        for x in [width[0], width[1]]:
            border[originY + y].append(originX + x)
    return border

def partTwo(i):
    sensors = []
    for sensor in i:
        sensors.append([sensor[0], sensor[1], calculateManhattanDistance(sensor[0], sensor[1], sensor[2], sensor[3])])
    for i, sensor in enumerate(sensors):
        border = findBorderForSensor(sensor[0], sensor[1], sensor[2])
        print('calculated border for ' + str(i + 1) + '/' + str(len(sensors)))
        for y in border.keys():
            for x in border[y]:
                if not (0 < x < 4000000 and 0 < y < 4000000): continue
                for s in sensors:
                    inRange = checkIfInRange(x, y, s[0], s[1], s[2])
                    if inRange: break
                if not inRange: return 4000000 * x + y
        print('checked border for ' + str(i + 1) + '/' + str(len(sensors)))

inputArray = inputString.splitlines()
inputArray = parseInput(inputArray)

#print(partOne(inputArray))

print(partTwo(inputArray))

end = time.time()
print(end - start)