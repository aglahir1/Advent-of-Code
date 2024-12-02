
# Started
# Finished

from copy import deepcopy


f = open('2024/02.txt', 'r')
inputString = f.read()

#inputString = """7 6 4 2 1
#1 2 7 8 9
#9 7 6 2 1
#1 3 2 4 5
#8 6 4 4 1
#1 3 6 7 9"""

def partOne(i):
    validreports = 0
    for r in i:
        if (all(r[j] < r[j+1] for j in range(len(r) - 1)) or all(r[j] > r[j+1] for j in range(len(r) - 1))) and all(abs(r[j] - r[j+1]) < 4 for j in range(len(r) - 1)): validreports += 1
    return validreports


def partTwo(i):
    validreports = 0
    for r in i:
        if (all(r[j] < r[j+1] for j in range(len(r) - 1)) or all(r[j] > r[j+1] for j in range(len(r) - 1))) and all(abs(r[j] - r[j+1]) < 4 for j in range(len(r) - 1)): 
            validreports += 1
            continue
        for x in range(len(r)):
            temp = deepcopy(r)
            temp.pop(x)
            if (all(temp[j] < temp[j+1] for j in range(len(temp) - 1)) or all(temp[j] > temp[j+1] for j in range(len(temp) - 1))) and all(abs(temp[j] - temp[j+1]) < 4 for j in range(len(temp) - 1)):
                validreports += 1
                break
    return validreports

reports = [x.split() for x in inputString.splitlines()]
inputArray = [[int(j) for j in x] for x in reports]

print(partOne(inputArray))

print(partTwo(inputArray))
