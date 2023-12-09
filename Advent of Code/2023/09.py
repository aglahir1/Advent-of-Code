
# Started
# Finished

from copy import copy


f = open('2023/09.txt', 'r')
inputString = f.read()

# inputString = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

def partOne(i: list[list[int]]):
    runningSum = 0
    runningAntiSum = 0
    for line in i:
        linehistory: list[list[int]] = [copy(line)]
        while any([x != 0 for x in line]):
            newlist = []
            for x in range(len(line) - 1):
                newlist.append(line[x + 1] - line[x])
            line = newlist
            linehistory.append(copy(newlist))
        nextVal = sum([x[-1] for x in linehistory])
        prevVal = 0
        for l in linehistory[::-1]:
            prevVal = l[0] - prevVal
        runningSum += nextVal
        runningAntiSum += prevVal
    print(runningSum)
    return runningAntiSum

inputArray = [[int(x) for x in y.split()] for y in inputString.splitlines()]

print(partOne(inputArray))
