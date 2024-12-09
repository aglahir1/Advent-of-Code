
# Started
# Finished

import itertools


f = open('2024/08.txt', 'r')
inputString = f.read()

# inputString ="""............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

inputArray = inputString.splitlines()

gridH = len(inputArray)
gridW = len(inputArray[0])

def partOne(i):
    frequencies = dict()
    for y in range(gridH):
        for x in range(gridW):
            if i[y][x] == '.': continue
            freq = i[y][x]
            if not freq in frequencies.keys():
                frequencies[freq] = set()
            frequencies[freq].add((x, y))
    antipoles = set()
    for freq in frequencies.values():
        for pair in itertools.combinations(freq, 2):
            matrix = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
            a = (pair[0][0] + matrix[0], pair[0][1] + matrix[1])
            b = (pair[1][0] - matrix[0], pair[1][1] - matrix[1])
            if 0 <= a[0] < gridW and 0 <= a[1] < gridH: antipoles.add(a)
            if 0 <= b[0] < gridW and 0 <= b[1] < gridH: antipoles.add(b)
    return len(antipoles)

def partTwo(i):
    frequencies = dict()
    for y in range(gridH):
        for x in range(gridW):
            if i[y][x] == '.': continue
            freq = i[y][x]
            if not freq in frequencies.keys():
                frequencies[freq] = set()
            frequencies[freq].add((x, y))
    antipoles = set()
    for freq in frequencies.values():
        for pair in itertools.combinations(freq, 2):
            matrix = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
            line = set()
            a = pair[0]
            while True:
                line.add(a)
                a = (a[0] + matrix[0], a[1] + matrix[1])
                if not (0 <= a[0] < gridW and 0 <= a[1] < gridH):
                    break
            b = pair[1]
            while True:
                line.add(b)
                b = (b[0] - matrix[0], b[1] - matrix[1])
                if not (0 <= b[0] < gridW and 0 <= b[1] < gridH):
                    break
            antipoles = antipoles.union(line)
    return len(antipoles)

print(partOne(inputArray))

print(partTwo(inputArray))
