
# Started
# Finished

from copy import deepcopy


f = open('2024/01.txt', 'r')
inputString = f.read()

# inputString = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

def partOne(i):
    l1 = deepcopy(i[0])
    l2 = deepcopy(i[1])
    l1.sort()
    l2.sort()
    return sum([abs(a[0] - a[1]) for a in zip(l1, l2)])

def partTwo(i):
    l1 = deepcopy(i[0])
    l2 = deepcopy(i[1])
    runningsum = 0
    for x in l1:
        runningsum += x * l2.count(x)
    return runningsum

lines = inputString.splitlines()

inputArray = [[int(x.split()[0]) for x in lines], [int(x.split()[1]) for x in lines]]

print(partOne(inputArray))

print(partTwo(inputArray))
