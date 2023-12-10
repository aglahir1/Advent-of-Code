
# Started
# Finished

import re


f = open('2017/16.txt', 'r')
inputString = f.read()

# inputString = "s1,x3/4,pe/b"

def partOne(i):
    programs = 'a b c d e f g h i j k l m n o p'.split()
    # programs = 'a b c d e'.split()
    size = len(programs)
    for inst in i:
        if inst[0] == 's':
            amount = int(inst[1:])
            programs = programs[size - amount:] + programs[:size -amount]
        elif inst[0] == 'x':
            result = re.search(r'x(\d+)/(\d+)', inst)
            posA = int(result.group(1))
            posB = int(result.group(2))
            progA = programs[posA]
            progB = programs[posB]
            programs[posA] = progB
            programs[posB] = progA
        elif inst[0] == 'p':
            result = re.search(r'p(\D)/(\D)', inst)
            progA = result.group(1)
            progB = result.group(2)
            posA = programs.index(progA)
            posB = programs.index(progB)
            programs[posA] = progB
            programs[posB] = progA
    return ''.join(programs)

def partTwo(i):
    programs = 'a b c d e f g h i j k l m n o p'.split()
    # programs = 'a b c d e'.split()
    size = len(programs)
    history = [''.join(programs)]
    count = 0
    while True:
        count += 1
        for inst in i:
            if inst[0] == 's':
                amount = int(inst[1:])
                programs = programs[size - amount:] + programs[:size -amount]
            elif inst[0] == 'x':
                result = re.search(r'x(\d+)/(\d+)', inst)
                posA = int(result.group(1))
                posB = int(result.group(2))
                progA = programs[posA]
                progB = programs[posB]
                programs[posA] = progB
                programs[posB] = progA
            elif inst[0] == 'p':
                result = re.search(r'p(\D)/(\D)', inst)
                progA = result.group(1)
                progB = result.group(2)
                posA = programs.index(progA)
                posB = programs.index(progB)
                programs[posA] = progB
                programs[posB] = progA
        if ''.join(programs) in history:
            return history[1000000000 % count]
        else:
            history.append(''.join(programs))
            
    return ''.join(programs)

inputArray = inputString.split(',')

print(partOne(inputArray))

print(partTwo(inputArray))
