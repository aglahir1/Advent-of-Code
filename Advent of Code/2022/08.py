
from pprint import pprint

# Started
# Finished

f = open('2022/08.txt', 'r')
inputString = f.read()

#inputString = """30373
#25512
#65332
#33549
#35390"""

def isVisible(t, x, y):
    return any([visibleFromTop(t, x, y)[0], visibleFromBottom(t, x, y)[0], visibleFromLeft(t, x, y)[0], visibleFromRight(t, x, y)[0]])

def scenicScore(t, x, y):
    return visibleFromTop(t, x, y)[1] * visibleFromBottom(t, x, y)[1] * visibleFromLeft(t, x, y)[1] * visibleFromRight(t, x, y)[1]

def visibleFromTop(t, x, y):
    count = 0
    height = t[y][x]
    if y == 0: return (True, 0)
    y -= 1
    while y >= 0:
        count += 1
        if t[y][x] >= height: return (False, count)
        y -= 1
    return (True, count)

def visibleFromBottom(t, x, y):
    count = 0
    height = t[y][x]
    if y == len(t) - 1: return (True, 0)
    y += 1
    while y <= len(t) - 1:
        count += 1
        if t[y][x] >= height: return (False, count)
        y += 1
    return (True, count)

def visibleFromLeft(t, x, y):
    count = 0
    height = t[y][x]
    if x == 0: return (True, 0)
    x -= 1
    while x >= 0:
        count += 1
        if t[y][x] >= height: return (False, count)
        x -= 1
    return (True, count)

def visibleFromRight(t, x, y):
    count = 0
    height = t[y][x]
    if x == len(t[0]) - 1: return (True, 0)
    x += 1
    while x <= len(t[0]) - 1:
        count += 1
        if t[y][x] >= height: return (False, count)
        x += 1
    return (True, count)

def count(v):
    count = 0
    for row in v:
        for tree in row:
            if tree: count += 1
    return count
def findHighest(s):
    highest = 0
    for row in s:
        highest = max(row + [highest])
    return highest

def partOne(i, v):
    for y, row in enumerate(i):
        for x, tree in enumerate(row):
            v[y][x] = isVisible(i, x, y)
    return count(v)

def partTwo(i, s):
    for y, row in enumerate(i):
        for x, tree in enumerate(row):
            s[y][x] = scenicScore(i, x, y)
    return findHighest(s)

inputArray = [list(map(int, list(x))) for x in inputString.splitlines()]

visibilityMatrix = [[False for _ in range(len(inputArray[0]))] for _ in range(len(inputArray))]
scenicMatrix = [[0 for _ in range(len(inputArray[0]))] for _ in range(len(inputArray))]

print(partOne(inputArray, visibilityMatrix))

print(partTwo(inputArray, scenicMatrix))
