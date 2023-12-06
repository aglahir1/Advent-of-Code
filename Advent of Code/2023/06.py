
# Started
# Finished

from math import ceil, floor, sqrt


f = open('2023/06.txt', 'r')
inputString = f.read()

#inputString = """Time:      7  15   30
#Distance:  9  40  200"""

def partOne(i):
    runningResult = 1
    for r in range(len(i[0])):
        d = int(i[0][r])
        r = int(i[1][r])
        under = (d * d) - (4 * r)
        root = sqrt(under)
        pos = (-d + root) / (-2)
        neg = (-d - root) / (-2)
        length = len(range(ceil(pos), floor(neg)))
        length += 1
        if ceil(pos) == pos: length -= 1
        if floor(neg) == neg: length -= 1
        runningResult *= length
    return runningResult

def partTwo(i):
    d = int(''.join(i[0]))
    r = int(''.join(i[1]))
    under = (d * d) - (4 * r)
    root = sqrt(under)
    pos = (-d + root) / (-2)
    neg = (-d - root) / (-2)
    length = len(range(ceil(pos), floor(neg)))
    length += 1
    if ceil(pos) == pos: length -= 1
    if floor(neg) == neg: length -= 1
    return length

inputArray = [x.split(':')[1].split() for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
