
# Started 14:24
# Finished 15:05

import itertools

f = open('2021/09.txt', 'r')
inputString = f.read()

#inputString="""2199943210
#3987894921
#9856789892
#8767896789
#9899965678"""

inputArray = inputString.splitlines()

heightmap = []

for entry in inputArray:
    heightmap.append(list(entry))

lowpoints = []

def exploreBasin(x, y):
    lowestpoint = int(heightmap[y][x])
    basin = [[x, y]]
    if x > 0:
        if lowestpoint < int(heightmap[y][x - 1]) != 9:
            basin.append([x - 1, y])
            basin += exploreBasin(x - 1, y)
    if x < len(heightmap[y]) - 1:
        if lowestpoint < int(heightmap[y][x + 1]) != 9:
            basin.append([x + 1, y])
            basin += exploreBasin(x + 1, y)
    if y > 0:
        if lowestpoint < int(heightmap[y - 1][x]) != 9:
            basin.append([x, y - 1])
            basin += exploreBasin(x, y - 1)
    if y < len(heightmap) - 1:
        if lowestpoint < int(heightmap[y + 1][x]) != 9:
            basin.append([x, y + 1])
            basin += exploreBasin(x, y + 1)
    basin.sort()
    endresult = list(k for k,_ in itertools.groupby(basin))
    return endresult


for y, row in enumerate(heightmap):
    for x, value in enumerate(row):
        if x > 0:
            if row[x - 1] <= value:
                continue
        if x < len(row) - 1:
            if row[x + 1] <= value:
                continue
        if y > 0:
            if heightmap[y - 1][x] <= value:
                continue
        if y < len(heightmap) - 1:
            if heightmap[y + 1][x] <= value:
                continue
        basin = exploreBasin(x, y)
        lowpoints.append([x, y, int(value), basin])


riskLevels = sum([x[2] + 1 for x in lowpoints])

basins = [x[3] for x in lowpoints]

print([len(x) for x in basins])

basins.sort(key = lambda x: len(x), reverse = True)

print([len(x) for x in basins])

print(len(basins[0]) * len(basins[1]) * len(basins[2]))

print(basins[-1])