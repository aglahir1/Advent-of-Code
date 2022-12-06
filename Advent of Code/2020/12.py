
# Started
# Finished

from copy import deepcopy

f = open('2020/12.txt', 'r')
inputString = f.read()

#inputString = """F10
#N3
#F7
#R90
#F11"""

def turn(facing, instruction):
    cardinals = 'NESW'
    current = cardinals.find(facing)
    amount = int(instruction[1] / 90) * (-1, 1)[instruction[0] == 'R']
    new = current + amount
    return cardinals[new % 4]

def rotate(x, y, instruction):
    amount = (int(instruction[1] / 90) * (-1, 1)[instruction[0] == 'R']) % 4
    newX = x
    newY = y
    if amount == 1:
        newX = y
        newY = -x
    if amount == 2:
        newX = -x
        newY = -y
    if amount == 3:
        newX = -y
        newY = x
    return (newX, newY)

def partOne(i):
    facing = 'E'
    yDiff = 0
    xDiff = 0
    instructions = deepcopy(i)
    for j, x in enumerate(i):
        if x[0] == 'F': instructions[j][0] = facing
        if x[0] in ('L', 'R'): 
            facing = turn(facing, x)
    for x in instructions:
        if x[0] == 'N': yDiff += x[1]
        if x[0] == 'S': yDiff -= x[1]
        if x[0] == 'E': xDiff += x[1]
        if x[0] == 'W': xDiff -= x[1]
    return abs(xDiff) + abs(yDiff)

def partTwo(i):
    xPos = 0
    yPos = 0
    xDiff = 10
    yDiff = 1
    for x in i:
        if x[0] == 'F':
            xPos += xDiff * x[1]
            yPos += yDiff * x[1]
        if x[0] == 'N': yDiff += x[1]
        if x[0] == 'S': yDiff -= x[1]
        if x[0] == 'E': xDiff += x[1]
        if x[0] == 'W': xDiff -= x[1]
        if x[0] in ('L', 'R'): (xDiff, yDiff) = rotate(xDiff, yDiff, x)
    return abs(xPos) + abs(yPos)


inputArray = inputString.splitlines()

instructions = [[x[0], int(x[1:])] for x in inputArray]

print(partOne(instructions))

print(partTwo(instructions))
