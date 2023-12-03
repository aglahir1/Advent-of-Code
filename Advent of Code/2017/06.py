
# Started
# Finished

from copy import deepcopy


f = open('2017/06.txt', 'r')
inputString = f.read()

#inputString = '0 2 7 0'

def partOne(i):
    cycle = 1
    amountOfBanks = len(i)
    history = set([','.join([str(x) for x in i])])
    while True:
        bankToEmpty = i.index(max(i))
        blocksToPush = i[bankToEmpty]
        i[bankToEmpty] = 0
        dist = blocksToPush // amountOfBanks
        i = [x + dist for x in i]
        blocksToPush = blocksToPush % amountOfBanks
        for j in range(1, blocksToPush + 1):
            i[(bankToEmpty + j) % amountOfBanks] += 1
        prior = len(history)
        history.add(','.join([str(x) for x in i]))
        if prior == len(history): return cycle
        cycle += 1

def partTwo(i):
    cycle = 1
    amountOfBanks = len(i)
    history = [','.join([str(x) for x in i])]
    while True:
        bankToEmpty = i.index(max(i))
        blocksToPush = i[bankToEmpty]
        i[bankToEmpty] = 0
        dist = blocksToPush // amountOfBanks
        i = [x + dist for x in i]
        blocksToPush = blocksToPush % amountOfBanks
        for j in range(1, blocksToPush + 1):
            i[(bankToEmpty + j) % amountOfBanks] += 1
        prior = len(history)
        history.append(','.join([str(x) for x in i]))
        if prior == len(set(history)): break
        cycle += 1
    return len(history) - history.index(history[-1]) - 1

inputArray = [int(x) for x in inputString.split()]

print(partOne(deepcopy(inputArray)))

print(partTwo(inputArray))
