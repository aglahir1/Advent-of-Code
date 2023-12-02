
# Started
# Finished

from copy import deepcopy


f = open('2017/05.txt', 'r')
inputString = f.read()
#inputString = """0
#3
#0
#1
#-3"""

def partOne(i):
    pointer = 0
    steps = 0
    while pointer >= 0 and pointer < len(i):
        instruction = i[pointer]
        i[pointer] += 1
        pointer += instruction
        steps += 1
    return steps

def partTwo(i):
    pointer = 0
    steps = 0
    while pointer >= 0 and pointer < len(i):
        instruction = i[pointer]
        if instruction >= 3:
            i[pointer] -= 1
        else:
            i[pointer] += 1
        pointer += instruction
        steps += 1
    return steps

inputArray = [int(x) for x in inputString.splitlines()]

print(partOne(deepcopy(inputArray)))

print(partTwo(deepcopy(inputArray)))
