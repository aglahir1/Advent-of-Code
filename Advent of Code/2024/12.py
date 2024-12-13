
# Started
# Finished

from operator import itemgetter


f = open('2024/12.txt', 'r')
inputString = f.read()

#inputString = """RRRRIICCFF
#RRRRIICCCF
#VVRRRCCFFF
#VVRCCCJFFF
#VVVVCJJCFE
#VVIVCCJJEE
#VVIIICJJEE
#MIIIIIJJEE
#MIIISIJEEE
#MMMISSJEEE"""

field = inputString.splitlines()
fieldY = len(field)
fieldX = len(field[0])


def findRegion(region: set[tuple[int]], plantType: str, currentPos: tuple[int]) -> set[tuple[int]]:
    up = (currentPos[0], currentPos[1] - 1)
    down = (currentPos[0], currentPos[1] + 1)
    left = (currentPos[0] - 1, currentPos[1])
    right = (currentPos[0] + 1, currentPos[1])
    dirs = [up, down, left, right]
    newfleems = []
    for d in dirs:
        if 0 <= d[0] < fieldX and 0 <= d[1] < fieldY:
            if field[d[1]][d[0]] == plantType and d not in region:
                newfleems.append(d)
                region.add(d)
    for p in newfleems:
        region = region.union(findRegion(region, plantType, p))
    return region

def findPerim(pos: tuple[int], plantType: str) -> int:
    up = (pos[0], pos[1] - 1)
    down = (pos[0], pos[1] + 1)
    left = (pos[0] - 1, pos[1])
    right = (pos[0] + 1, pos[1])
    dirs = [up, down, left, right]
    runningSum = 0
    for d in dirs:
        if 0 <= d[0] < fieldX and 0 <= d[1] < fieldY:
            if field[d[1]][d[0]] != plantType:
                runningSum += 1
        else:
            runningSum += 1
    return runningSum

def findSides(region: set[tuple[int]], plantType: str) -> int:
    sides = {'l': set(), 'r': set(), 'u': set(), 'd': set()}
    for pos in region:
        up = (pos[0], pos[1] - 1)
        down = (pos[0], pos[1] + 1)
        left = (pos[0] - 1, pos[1])
        right = (pos[0] + 1, pos[1])
        dirs = [(up, 'u'), (down, 'd'), (left, 'l'), (right, 'r')]
        runningSum = 0
        for d, x in zip([i[0] for i in dirs], [i[1] for i in dirs]):
            if 0 <= d[0] < fieldX and 0 <= d[1] < fieldY:
                if field[d[1]][d[0]] != plantType:
                    sides[x].add(pos)
            else:
                sides[x].add(pos)
    sideCount = 0
    currentY = -1
    currentX = -1
    for l in sorted(list(sides['d']),key=itemgetter(1,0)):
        if l[1] != currentY:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        if abs(l[0] - currentX) > 1:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        currentX = l[0]
    currentY = -1
    currentX = -1
    for l in sorted(list(sides['u']),key=itemgetter(1,0)):
        if l[1] != currentY:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        if abs(l[0] - currentX) > 1:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        currentX = l[0]
    currentY = -1
    currentX = -1
    for l in sorted(list(sides['l']),key=itemgetter(0,1)):
        if l[0] != currentX:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        if abs(l[1] - currentY) > 1:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        currentY = l[1]
    currentY = -1
    currentX = -1
    for l in sorted(list(sides['r']),key=itemgetter(0,1)):
        if l[0] != currentX:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        if abs(l[1] - currentY) > 1:
            sideCount += 1
            currentY = l[1]
            currentX = l[0]
            continue
        currentY = l[1]
    return sideCount





regions = []
searched = set()

for y, l in enumerate(field):
    for x, p in enumerate(l):
        if (x, y) in searched: continue
        newRegion = findRegion({(x, y)}, p, (x, y))
        searched = searched.union(newRegion)
        region = {'plant': p, 'region': newRegion, 'area': len(newRegion), 'perimeter': sum([findPerim(x, p) for x in newRegion]), 'sides': findSides(newRegion, p)}
        regions.append(region)

def partOne():
    return sum([x['area'] * x['perimeter'] for x in regions])

def partTwo():
    return sum([x['area'] * x['sides'] for x in regions])


print(partOne())

print(partTwo())
