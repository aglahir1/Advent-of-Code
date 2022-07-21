
# Started
# Finished

import copy

f = open('2016/08.txt', 'r')
inputString = f.read()

def print2DArray(arr):
    for r in arr:
        for l in r:
            print(end=l)
        print()
    print()

def rect(a,b,screen):
    work = copy.deepcopy(screen)
    for i in range(b):
        for j in range(a):
            work[i][j] = '#'
    return work

def rotateCol(col,amount,screen):
    work = copy.deepcopy(screen)
    for x in range(len(work)):
        work[(x+amount)%len(work)][col] = screen[x][col]
    return work

def rotateRow(row,amount,screen):
    work = copy.deepcopy(screen)
    for x in range(len(work[0])):
        work[row][(x+amount)%len(work[0])] = screen[row][x]
    return work

def countLitPixels(screen):
    count=0
    for y in screen:
        for x in y:
            if x == '#': count += 1
    return count

def parse(instruction, screen):
    work = copy.deepcopy(screen)
    instruction = instruction.split()
    command = instruction.pop(0)
    if command == 'rect':
        a, b = map(int,instruction.pop(0).split('x'))
        work = rect(a, b, work)
    else:
        axisType = instruction.pop(0)
        axis = int(instruction.pop(0)[2:])
        amount = int(instruction.pop())
        if axisType == 'row':
            work = rotateRow(axis, amount, work)
        else:
            work = rotateCol(axis, amount, work)
    return work

def partOne(instructions, screen):
    for i in instructions:
        screen = parse(i, screen)
    print2DArray(screen)
    return countLitPixels(screen)


def partTwo(i):
    pass

inputArray = inputString.splitlines()

screen = [['.']*50 for _ in range(6)]


print(partOne(inputArray, screen))

print(partTwo(inputArray))
