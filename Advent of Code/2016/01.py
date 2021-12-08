
# Started 19:13
# Ended 19:34

f = open('2016/01.txt', 'r')
inputString = f.read()

inputArray = inputString.split(', ')

commands = []

for entry in inputArray:
    commands.append([entry[0], int(entry[1:])])

print(commands)

directions = ['N', 'E', 'S', 'W']
facing = 0

currentCoords = [0, 0]
visitedCoords = []

def move(amount):
    global currentCoords, visitedCoords
    for i in range(amount):
        if facing == 0: currentCoords[1] += 1
        elif facing == 1: currentCoords[0] += 1
        elif facing == 2: currentCoords[1] -= 1
        elif facing == 3: currentCoords[0] -= 1
        if currentCoords in visitedCoords: return True
        visitedCoords.append(currentCoords[:])

def turn(direction):
    global facing
    if direction == 'R':
        facing += 1
        if facing > 3: facing = 0
    elif direction == 'L':
        facing -= 1
        if facing < 0: facing = 3

for comm in commands:
    turn(comm[0])
    if move(comm[1]): break

print(visitedCoords)
print(currentCoords)
print(sum([abs(x) for x in currentCoords]))