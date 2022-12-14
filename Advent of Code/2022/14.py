
# Started
# Finished

from typing import List

f = open('2022/14.txt', 'r')
inputString: str = f.read()

#inputString = """498,4 -> 498,6 -> 496,6
#503,4 -> 502,4 -> 502,9 -> 494,9"""

rock: set = set()
sand: set = set()
greatestY: int = 0

def checkBelow(coords: List[int]):
    coordLiteral: str = str(coords[0]) + ',' + str(coords[1] + 1)
    return not (coordLiteral in rock.union(sand))

def checkBelowLeft(coords: List[int]):
    coordLiteral: str = str(coords[0] - 1) + ',' + str(coords[1] + 1)
    return not (coordLiteral in rock.union(sand))

def checkBelowRight(coords: List[int]):
    coordLiteral: str = str(coords[0] + 1) + ',' + str(coords[1] + 1)
    return not (coordLiteral in rock.union(sand))

def checkMove(coords: List[int]):
    return (checkBelow(coords) or checkBelowLeft(coords) or checkBelowRight(coords)) and (coords[1] < greatestY)

def move(coords: List[int]):
    if checkBelow(coords): return [coords[0], coords[1] + 1]
    if checkBelowLeft(coords): return [coords[0] - 1, coords[1] + 1]
    return [coords[0] + 1, coords[1] + 1]

def draw(node1, node2):
    global greatestY
    x1, x2, y1, y2 = node1[0], node2[0], node1[1], node2[1]
    if y1 > greatestY: greatestY = y1
    if y2 > greatestY: greatestY = y2
    if y1 == y2:
        if x1 > x2:
            for j in range(x1 - x2 + 1):
                rock.add(str(j + x2) + ',' + str(y1))
            return
        for j in range(x2 - x1 + 1):
            rock.add(str(j + x1) + ',' + str(y1))
        return
    if y1 > y2:
        for j in range(y1 - y2 + 1):
            rock.add(str(x1) + ',' + str(j + y2))
        return
    for j in range(y2 - y1 + 1):
        rock.add(str(x1) + ',' + str(j + y1))
    return

inputArray: List[List[List[int]]] = [[list(map(int, j.split(','))) for j in x.split(' -> ')] for x in inputString.splitlines()]

# draw loop
for path in inputArray:
    for node1, node2 in zip(path, path[1:]):
        draw(node1, node2)

sandOrigin: List[int] = [500, 0]

while True:
    currentSand = sandOrigin[:]
    while checkMove(currentSand):
        currentSand = move(currentSand)
    if currentSand[1] >= greatestY: break
    sand.add(str(currentSand[0]) + ',' + str(currentSand[1]))

print(len(sand))