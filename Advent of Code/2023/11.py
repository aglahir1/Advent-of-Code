
# Started
# Finished

f = open('2023/11.txt', 'r')
inputString = f.read()

#inputString ="""...#......
#.......#..
##.........
#..........
#......#...
#.#........
#.........#
#..........
#.......#..
##...#....."""

def manhattanDistance(pointOne, pointTwo):
    return abs(pointOne[0] - pointTwo[0]) + abs(pointOne[1] - pointTwo[1])

def manhattanDistanceAdjusted(pointOne, pointTwo, multiplier, grid):
    basicDistance = abs(pointOne[0] - pointTwo[0]) + abs(pointOne[1] - pointTwo[1])
    x1 = min([x[1] for x in [pointOne, pointTwo]])
    x2 = max([x[1] for x in [pointOne, pointTwo]])
    y1 = min([x[0] for x in [pointOne, pointTwo]])
    y2 = max([x[0] for x in [pointOne, pointTwo]])
    crosses = grid[y1][x1:x2].count('x') + [grid[x][x1] for x in range(y1, y2)].count('x')
    return basicDistance + (crosses * (multiplier - 1))

    

def partOne(i):
    expandedUniverse: list[str] = []
    for line in i:
        if '#' not in line:
            expandedUniverse.append('x'*len(line))
        else:
            expandedUniverse.append(line)
    cols = []
    for x in range(len(i[0])):
        if all([j[x] != '#' for j in expandedUniverse]):
            cols.append(x)
    for x in cols[::-1]:
        for y in range(len(expandedUniverse)):
            expandedUniverse[y] = expandedUniverse[y][:x] + 'x' + expandedUniverse[y][x + 1:]
    galaxies: list[list[int]] = []
    for y, line in enumerate(expandedUniverse):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append([y, x])
    runningSum = 0
    for x, g in enumerate(galaxies):
        if x == len(galaxies) - 1:
            break
        for c in galaxies[x + 1:]:
            runningSum += manhattanDistanceAdjusted(g, c, 1_000_000, expandedUniverse)
    return runningSum

inputArray = inputString.splitlines()

print(partOne(inputArray))