
# Started 22:24
# Finished 22:40

f = open('2022/03.txt', 'r')
inputString = f.read()

#inputString = """vJrwpWtwJgWrhcsFMMfFFhFp
#jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#PmmdzqPrVvPwwTWBwg
#wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#ttgJtRGJQctTZtZT
#CrZsJsPPZsGzwwsLwLmpwMDw"""

def checkError(c1, c2):
    for c in c1:
        if c in c2: return c

def getPriority(c):
    prio = ord(c) - 96
    if prio < 1: prio += 58
    return prio

def findCommon(c1, c2):
    r = ''
    for c in c1:
        if c in c2: r += c
    return r

def partOne(i):
    sum = 0
    for r in i:
        c1 = r[:int(len(r)/2)]
        c2 = r[int(len(r)/2):]
        sum += getPriority(checkError(c1, c2))
    return sum

def partTwo(i):
    sum = 0
    i = iter(i)
    for e1, e2, e3 in zip(i, i, i):
        sum += getPriority(checkError(findCommon(e1, e2), e3))
    return sum

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
