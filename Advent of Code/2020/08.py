
# Started
# Finished

f = open('2020/08.txt', 'r')
inputString = f.read()

#inputString = """nop +0
#acc +1
#jmp +4
#acc +3
#jmp -3
#acc -99
#acc +1
#jmp -4
#acc +6"""

def run(i):
    visited = []
    pos = 0
    acc = 0
    while pos not in visited:
        visited += [pos]
        instruction = i[pos].split()
        if instruction[0] == 'acc':
            pos += 1
            acc += int(instruction[1])
        elif instruction[0] == 'jmp':
            pos += int(instruction[1])
        elif instruction[0] == 'nop':
            pos += 1
    return acc

def checkRun(i):
    visited = []
    pos = 0
    acc = 0
    while pos not in visited and 0 <= pos < len(i):
        visited += [pos]
        instruction = i[pos].split()
        if instruction[0] == 'acc':
            pos += 1
            acc += int(instruction[1])
        elif instruction[0] == 'jmp':
            pos += int(instruction[1])
        elif instruction[0] == 'nop':
            pos += 1
    return [len(i) <= pos or pos < 0, acc]



def partOne(i):
    return run(i)


def partTwo(i):
    for x in range(len(i)):
        if i[x].split()[0] == 'nop':
            test = checkRun(i[:x] + ['jmp' + i[x][3:]] + i[x+1:])
        elif i[x].split()[0] == 'jmp':
            test = checkRun(i[:x] + ['nop' + i[x][3:]] + i[x+1:])
        if test[0]: return test[1]

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
