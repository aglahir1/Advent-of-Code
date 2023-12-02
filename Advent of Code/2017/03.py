
# Started
# Finished

from collections import defaultdict


inputInt = 325489

def partOne(i):
    currentNum = 1
    x = 0
    y = 0
    for circleNumber in range(1, 287):
        x += 1
        currentNum += 1
        for rightside in range(y + 1, circleNumber + 1):
            y = rightside
            currentNum += 1
            if currentNum == i:
                return abs(y) + abs(x)
        for topside in range(x - 1, -circleNumber - 1, -1):
            x = topside
            currentNum += 1
            if currentNum == i:
                return abs(y) + abs(x)
        for leftside in range(y - 1, -circleNumber - 1, -1):
            y = leftside
            currentNum += 1
            if currentNum == i:
                return abs(y) + abs(x)
        for bottomside in range(x + 1, circleNumber + 1):
            x = bottomside
            currentNum += 1
            if currentNum == i:
                return abs(y) + abs(x)

def getAdjacents(x, y, spiral):
    return spiral.get(x - 1, {}).get(y, 0) + spiral.get(x - 1, {}).get(y - 1, 0) + spiral.get(x - 1, {}).get(y + 1, 0) + spiral.get(x + 1, {}).get(y, 0) +spiral.get(x + 1, {}).get(y - 1, 0) + spiral.get(x + 1, {}).get(y + 1, 0)+ spiral.get(x, {}).get(y - 1, 0) + spiral.get(x, {}).get(y + 1, 0)

def partTwo(i):
    spiral = defaultdict(dict)
    spiral[0][0] = 1
    x = 0
    y = 0
    for circleNumber in range(1, 287):
        x += 1
        num = getAdjacents(x, y, spiral)
        if num > i:
            return num
        spiral[x][y] = num
        for rightside in range(y + 1, circleNumber + 1):
            y = rightside
            num = getAdjacents(x, y, spiral)
            if num > i:
                return num
            spiral[x][y] = num
        for topside in range(x - 1, -circleNumber - 1, -1):
            x = topside
            num = getAdjacents(x, y, spiral)
            if num > i:
                return num
            spiral[x][y] = num
        for leftside in range(y - 1, -circleNumber - 1, -1):
            y = leftside
            num = getAdjacents(x, y, spiral)
            if num > i:
                return num
            spiral[x][y] = num
        for bottomside in range(x + 1, circleNumber + 1):
            x = bottomside
            num = getAdjacents(x, y, spiral)
            if num > i:
                return num
            spiral[x][y] = num

print(partOne(inputInt))

print(partTwo(inputInt))
