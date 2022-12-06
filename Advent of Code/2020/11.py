
# Started
# Finished

from copy import deepcopy
from pprint import pprint


f = open('2020/11.txt', 'r')
inputString = f.read()

#inputString = """L.LL.LL.LL
#LLLLLLL.LL
#L.L.L..L..
#LLLL.LL.LL
#L.LL.LL.LL
#L.LLLLL.LL
#..L.L.....
#LLLLLLLLLL
#L.LLLLLL.L
#L.LLLLL.LL"""

def checksurrounding(y, x, layout):
    occupied = 0
    for a in [y - 1, y, y + 1]:
        if a < 0 or a >= len(layout): continue
        for b in [x - 1, x, x + 1]:
            if b < 0 or b >= len(layout[0]): continue
            if a == y and b == x: continue
            if layout[a][b] == '#': occupied += 1
    return occupied

def advancedsurrounding(y, x, layout, vision):
    occupied = 0
    for s in vision[str(y) + ',' + str(x)]:
        if layout[s[0]][s[1]] == '#': occupied += 1
    return occupied

def findNeighbours(x, y, layout):
    seats = []
    t, tr, r, br, b, bl, l, tl = [False] * 8
    i = y
    j = x
    while not b:
        i += 1
        if i >= len(layout): break
        if layout[i][j] == '.': continue
        b = True
        seats.append([i, j])
    i = y
    j = x
    while not t:
        i -= 1
        if i < 0: break
        if layout[i][j] == '.': continue
        t = True
        seats.append([i, j])
    i = y
    j = x
    while not l:
        j -= 1
        if j < 0: break
        if layout[i][j] == '.': continue
        l = True
        seats.append([i, j])
    i = y
    j = x
    while not r:
        j += 1
        if j >= len(layout[0]): break
        if layout[i][j] == '.': continue
        r = True
        seats.append([i, j])
    i = y
    j = x
    while not br:
        i += 1
        j += 1
        if j >= len(layout[0]) or i >= len(layout): break
        if layout[i][j] == '.': continue
        br = True
        seats.append([i, j])
    i = y
    j = x
    while not bl:
        i += 1
        j -= 1
        if j < 0 or i >= len(layout): break
        if layout[i][j] == '.': continue
        bl = True
        seats.append([i, j])
    i = y
    j = x
    while not tl:
        i -= 1
        j -= 1
        if j < 0 or i < 0: break
        if layout[i][j] == '.': continue
        tl = True
        seats.append([i, j])
    i = y
    j = x
    while not tr:
        i -= 1
        j += 1
        if j >= len(layout[0]) or i < 0: break
        if layout[i][j] == '.': continue
        tr = True
        seats.append([i, j])
    return seats

def mapVision(layout):
    vision = {}
    for y, r in enumerate(layout):
        for x, s in enumerate(r):
            vision[str(y) + ',' + str(x)] = findNeighbours(x, y, layout)
    return vision

def round(layout):
    change = 0
    newLayout = deepcopy(layout)
    y = 0
    x = 0
    while y < len(layout):
        while x < len(layout[0]):

            if layout[y][x] == 'L':
                if checksurrounding(y, x, layout) == 0: 
                    newLayout[y][x] = '#'
                    change += 1
            if layout[y][x] == '#':
                if checksurrounding(y, x, layout) >= 4:
                    newLayout[y][x] = 'L'
                    change += 1

            x += 1
        x = 0
        y += 1
    return (newLayout, change)

def advancedround(layout, vision):
    change = 0
    newLayout = deepcopy(layout)
    y = 0
    x = 0
    while y < len(layout):
        while x < len(layout[0]):

            if layout[y][x] == 'L':
                if advancedsurrounding(y, x, layout, vision) == 0: 
                    newLayout[y][x] = '#'
                    change += 1
            if layout[y][x] == '#':
                if advancedsurrounding(y, x, layout, vision) >= 5:
                    newLayout[y][x] = 'L'
                    change += 1

            x += 1
        x = 0
        y += 1
    return (newLayout, change)

def count(layout):
    occupied = 0
    for r in layout:
        for s in r:
            if s == '#': occupied += 1
    return occupied

def partOne(i):
    j = 1
    while j != 0:
        (i, j) = round(i)
    return count(i)

def partTwo(i):
    vision = mapVision(i)
    j = 1
    while j != 0:
        (i, j) = advancedround(i, vision)
    return count(i)

inputArray = [list(x) for x in inputString.splitlines()]


print(partOne(inputArray))

print(partTwo(inputArray))
