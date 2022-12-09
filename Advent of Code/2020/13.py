
# Started
# Finished

f = open('2020/13.txt', 'r')
inputString = f.read()

#inputString = """939
#7,13,x,x,59,x,31,19"""

def partOne(i):
    time = int(i[0])
    results = []
    for x in i[1]:
        if x == 'x': continue
        x = int(x)
        remainingTime = x - (time % x)
        results.append([x, remainingTime])
    results.sort(key = lambda x: x[1])
    return results[0][0] * results[0][1]


def partTwo(i):
    currentTime = -1
    iterator = 1
    buses = [{'id': int(x), 'offset': y} for y, x in enumerate(i) if x != 'x']
    checkingBus = 0
    while True:
        currentTime += iterator
        if (currentTime + buses[checkingBus]['offset']) % buses[checkingBus]['id'] == 0:
            iterator *= buses[checkingBus]['id']
            checkingBus += 1
            if checkingBus == len(buses): return currentTime


inputArray = inputString.splitlines()

i = [inputArray[0], inputArray[1].split(',')]

print(partOne(i))

print(partTwo(i[1]))
