
# Started
# Finished

f = open('2022/09.txt', 'r')
inputString = f.read()

#inputString = """R 5
#U 8
#L 8
#D 3
#R 17
#D 10
#L 25
#U 20"""

#inputString = """R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2"""

def isAdjacent(xH, yH, xT, yT):
    return (abs(xH - xT) < 2) and (abs(yH - yT) < 2)

def calculateDirection(xH, yH, xT, yT):
    if abs(xH - xT) == 2:
        if xH > xT: 
            if yH > yT: return 'UR'
            elif yH < yT: return 'DR'
            return 'R'
        if yH > yT: return 'UL'
        elif yH < yT: return 'DL'
        return 'L'
    if abs(yH - yT) == 2:
        if yH > yT: 
            if xH > xT: return 'UR'
            elif xH < xT: return 'UL'
            return 'U'
        if xH > xT: return 'DR'
        elif xH < xT: return 'DL'
        return 'D'

def move(direction, x, y):
    if direction == 'U': y += 1
    elif direction == 'D': y -= 1
    elif direction == 'L': x -= 1
    elif direction == 'R': x += 1
    elif direction == 'DL': 
        y -= 1
        x -= 1
    elif direction == 'DR': 
        y -= 1
        x += 1
    elif direction == 'UL': 
        y += 1
        x -= 1
    elif direction == 'UR': 
        y += 1
        x += 1
    return (x, y)

def partOne(i):
    visitedSet = {'0,0'}
    xH = 0
    xT = 0
    yH = 0
    yT = 0
    for instruction in i:
        direction = instruction[0]
        distance = int(instruction.split()[1])
        for _ in range(distance):
            (xH, yH) = move(direction, xH, yH)
            if isAdjacent(xH, yH, xT, yT): continue
            tailDirection = calculateDirection(xH, yH, xT, yT)
            (xT, yT) = move(tailDirection, xT, yT)
            visitedSet.add(str(xT) + ',' + str(yT))
    return len(visitedSet)
    


def partTwo(i):
    visitedSet = {'0,0'}
    knots = [[0, 0] for _ in range(10)]
    for instruction in i:
        direction = instruction[0]
        distance = int(instruction.split()[1])
        for _ in range(distance):
            (knots[0][0], knots[0][1]) = move(direction, knots[0][0], knots[0][1])
            for x in range(1, len(knots)):
                if isAdjacent(knots[x - 1][0], knots[x - 1][1], knots[x][0], knots[x][1]): continue
                knotDirection = calculateDirection(knots[x - 1][0], knots[x - 1][1], knots[x][0], knots[x][1])
                (knots[x][0], knots[x][1]) = move(knotDirection, knots[x][0], knots[x][1])
            visitedSet.add(str(knots[-1][0]) + ',' + str(knots[-1][1]))
    return len(visitedSet)

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
