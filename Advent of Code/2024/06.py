
# Started
# Finished

from copy import deepcopy
from enum import Enum


f = open('2024/06.txt', 'r')
inputString = f.read()

# inputString = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

inputArray = inputString.splitlines()

gridH = len(inputArray)
gridW = len(inputArray[0])
    
def findAll(needle: str, haystack: str) -> set[int]:
    founds = set()
    for i, c in enumerate(haystack):
        if c == needle:
            founds.add(i)
    return founds

obstacles = dict()
for i in range(gridH):
    obstacles[i] = findAll('#', inputArray[i])
    guard = inputArray[i].find('^')
    if guard != -1:
        guardPosG = (guard, i)
        guardFacingG = 0
        
def printmap(visited: dict[int,set], obstacles: dict[int,set]):
    for y in range(gridH):
        for x in range(gridW):
            if x in obstacles[y]:
                print('#', end='')
            elif x in visited[y]:
                print('X', end='')
            else:
                print('.', end='')
        print()
        
def partOne():
    guardPos = guardPosG
    guardFacing = guardFacingG
    visited = {i: set() for i in range(gridH)}
    visited[guardPos[1]].add(guardPos[0])
    possibleObstaclesForPartTwo = set()
    while True:
        x = -1
        y = -1
        match guardFacing:
            case 0:
                x = guardPos[0]
                for i in range(guardPos[1])[::-1]:
                    if x in obstacles[i]:
                        y = i + 1
                        break
                if y == -1:
                    y = 0
                for a in range(y, guardPos[1]):
                    visited[a].add(x)
                    possibleObstaclesForPartTwo.add((x, a))
                if y == 0:
                    break
            case 1:
                y = guardPos[1]
                for i in range(guardPos[0] + 1, gridW):
                    if i in obstacles[y]:
                        x = i - 1
                        break
                if x == -1:
                    x = gridW - 1
                for a in range(guardPos[0], x + 1):
                    visited[y].add(a)
                    possibleObstaclesForPartTwo.add((a + 1, y))
                if x == gridW - 1:
                    break
            case 2:
                x = guardPos[0]
                for i in range(guardPos[1] + 1, gridH):
                    if x in obstacles[i]:
                        y = i - 1
                        break
                if y == -1:
                    y = gridH - 1
                for a in range(guardPos[1], y + 1):
                    visited[a].add(x)
                    possibleObstaclesForPartTwo.add((x, a + 1))
                if y == gridH - 1:
                    break
            case 3:
                y = guardPos[1]
                for i in range(guardPos[0])[::-1]:
                    if i in obstacles[y]:
                        x = i + 1
                        break
                if x == -1:
                    x = 0
                for a in range(x, guardPos[0]):
                    visited[y].add(a)
                    possibleObstaclesForPartTwo.add((a, y))
                if x == 0:
                    break
        guardPos = (x, y)
        guardFacing = (guardFacing + 1) % 4
    for y in range(gridH):
        for x in obstacles[y]:
            if (x, y) in possibleObstaclesForPartTwo:
                possibleObstaclesForPartTwo.remove((x, y))
    if (guardPosG[0], guardPosG[1]) in possibleObstaclesForPartTwo:
        possibleObstaclesForPartTwo.remove((guardPosG[0], guardPosG[1]))
    return [sum(len(x) for x in visited.values()), possibleObstaclesForPartTwo]
                
def partTwowompwomp():
    visited = {y: {x: set() for x in range(gridW)} for y in range(gridH)}
    firstPos = str(guardPosG[0]) + ',' + str(guardPosG[1])
    guardPos = guardPosG
    guardFacing = guardFacingG
    visited[guardPos[1]][guardPos[0]].add(guardFacing)
    possiblePositions = set()
    possiblePositions.add(firstPos)
    for y in range(gridH):
        for x in obstacles[y]:
            possiblePositions.add(str(x) + ',' + str(y))
    while True:
        facingSearch = (guardFacing + 1) % 4
        x1 = -1
        x2 = -1
        y1 = -1
        y2 = -1
        match guardFacing:
            case w if w in (0, 2):
                x1 = guardPos[0]
                for i in range(guardPos[1])[::-1]:
                    if x1 in obstacles[i]:
                        y1 = i + 1
                        break
                for i in range(guardPos[1], gridH):
                    if x1 in obstacles[i]:
                        y2 = i - 1
                        break
                if y1 == -1:
                    y1 = 0
                if y2 == -1:
                    y2 = gridH - 1
                for a in range(y1, y2 + 1):
                    visited[a][x1].add(guardFacing)
                    if facingSearch in visited[a][x1]:
                        if guardFacing == 0 and a != 0:
                            possiblePositions.add(str(x1) + ',' + str(a - 1))
                        if guardFacing == 2 and a != gridH - 1:
                            possiblePositions.add(str(x1) + ',' + str(a + 1))
                if (y1 == 0 and guardFacing == 0) or (y2 == gridH - 1 and guardFacing == 2):
                    break
            case w if w in (1, 3):
                y1 = guardPos[1]
                for i in range(guardPos[0])[::-1]:
                    if i in obstacles[y1]:
                        x1 = i + 1
                        break
                for i in range(guardPos[0], gridW):
                    if i in obstacles[y1]:
                        x2 = i - 1
                        break
                if x1 == -1:
                    x1 = 0
                if x2 == -1:
                    x2 = gridW - 1
                for a in range(x1, x2 + 1):
                    visited[y1][a].add(guardFacing)
                    if facingSearch in visited[y1][a]:
                        if guardFacing == 1 and a != gridW - 1:
                            possiblePositions.add(str(a + 1) + ',' + str(y1))
                        if guardFacing == 3 and a != 0:
                            possiblePositions.add(str(a - 1) + ',' + str(y1))
                if (x1 == 0 and guardFacing == 3) or (x2 == gridW - 1 and guardFacing == 1):
                    break
        guardX = {0: guardPos[0], 2: guardPos[0], 1: x2, 3: x1}[guardFacing]
        guardY = {1: guardPos[1], 3: guardPos[1], 0: y1, 2: y2}[guardFacing]
        guardPos = (guardX, guardY)
        guardFacing = (guardFacing + 1) % 4
    possiblePositions.remove(firstPos)
    for y in range(gridH):
        for x in obstacles[y]:
            possiblePositions.remove(str(x) + ',' + str(y))

    print(possiblePositions)
    return len(possiblePositions)

#brute force :(
def partTwo():
    possiblePositions = set()
    options = partOne()[1]
    for idx, o in enumerate(options):
        if not (0 <= o[0] < gridW and 0 <= o[1] < gridH): continue
        obs = deepcopy(obstacles)
        obs[o[1]].add(o[0])
        visited = {y: {x: set() for x in range(gridW)} for y in range(gridH)}
        guardPos = guardPosG
        guardFacing = guardFacingG
        visited[guardPos[1]][guardPos[0]].add(guardFacing)
        found = False
        while True:
            x = -1
            y = -1
            match guardFacing:
                case 0:
                    x = guardPos[0]
                    for i in range(guardPos[1])[::-1]:
                        if x in obs[i]:
                            y = i + 1
                            break
                    if y == -1:
                        y = 0
                    for a in range(y, guardPos[1]):
                        if guardFacing in visited[a][x]:
                            found = True
                            break
                        visited[a][x].add(guardFacing)
                    if y == 0:
                        break
                case 1:
                    y = guardPos[1]
                    for i in range(guardPos[0] + 1, gridW):
                        if i in obs[y]:
                            x = i - 1
                            break
                    if x == -1:
                        x = gridW - 1
                    for a in range(guardPos[0], x + 1):
                        if guardFacing in visited[y][a]:
                            found = True
                            break
                        visited[y][a].add(guardFacing)
                    if x == gridW - 1:
                        break
                case 2:
                    x = guardPos[0]
                    for i in range(guardPos[1] + 1, gridH):
                        if x in obs[i]:
                            y = i - 1
                            break
                    if y == -1:
                        y = gridH - 1
                    for a in range(guardPos[1], y + 1):
                        if guardFacing in visited[a][x]:
                            found = True
                            break
                        visited[a][x].add(guardFacing)
                    if y == gridH - 1:
                        break
                case 3:
                    y = guardPos[1]
                    for i in range(guardPos[0])[::-1]:
                        if i in obs[y]:
                            x = i + 1
                            break
                    if x == -1:
                        x = 0
                    for a in range(x, guardPos[0]):
                        if guardFacing in visited[y][a]:
                            found = True
                            break
                        visited[y][a].add(guardFacing)
                    if x == 0:
                        break
            guardPos = (x, y)
            guardFacing = (guardFacing + 1) % 4
            if found: 
                possiblePositions.add(o)
                break
        print(f'{idx} / {len(options)}')
    return len(possiblePositions)
        
        

print(partOne()[0])

print(partTwo())
