
# Started
# Finished


f = open('2017/18.txt', 'r')
inputString = f.read()

def partOne(i):
    registers = {'i': 0, 'a': 0, 'p': 0, 'b': 0, 'f': 0}
    pointer = 0
    lastPlayed = 0
    while 0 <= pointer < len(i):
        inst = i[pointer]
        match inst['command']:
            case 'snd':
                val = inst['values'][0]
                if val.lstrip('-').isdigit():
                    lastPlayed = int(val)
                else:
                    lastPlayed = registers[val]
            case 'set':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[reg] = int(val)
                else:
                    registers[reg] = registers[val]
            case 'add':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[reg] += int(val)
                else:
                    registers[reg] += registers[val]
            case 'mul':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[reg] *= int(val)
                else:
                    registers[reg] *= registers[val]
            case 'mod':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[reg] %= int(val)
                else:
                    registers[reg] %= registers[val]
            case 'rcv':
                reg = inst['values'][0]
                if registers[reg] != 0:
                    if lastPlayed != 0:
                        return lastPlayed
            case 'jgz':
                reg = inst['values'][0]
                val = inst['values'][1]
                if registers[reg] > 0:
                    if val.lstrip('-').isdigit():
                        pointer += int(val) - 1
                    else:
                        pointer += registers[val] - 1
        pointer += 1

def partTwo(i):
    runningCount = 0
    currentlyRunning = 0
    waiting = {0: False, 1: False}
    terminated = {0: False, 1: False}
    pointers = {0: 0, 1: 0}
    registers = {0: {'i': 0, 'a': 0, 'p': 0, 'b': 0, 'f': 0}, 1: {'i': 0, 'a': 0, 'p': 1, 'b': 0, 'f': 0}}
    queues = {0: [], 1: []}
    while not all(waiting.values()):
        if waiting[currentlyRunning]:
            currentlyRunning = (currentlyRunning + 1) % 2
        inst = i[pointers[currentlyRunning]]
        match inst['command']:
            case 'snd':
                val = inst['values'][0]
                if val.lstrip('-').isdigit():
                    queues[(currentlyRunning + 1) % 2].append(int(val))
                else:
                    queues[(currentlyRunning + 1) % 2].append(registers[currentlyRunning][val])
                if not terminated[(currentlyRunning + 1) % 2]:
                    waiting[(currentlyRunning + 1) % 2] = False
                if currentlyRunning == 1:
                    runningCount += 1
                    if runningCount % 100000 == 0: print(runningCount)
            case 'set':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[currentlyRunning][reg] = int(val)
                else:
                    registers[currentlyRunning][reg] = registers[currentlyRunning][val]
            case 'add':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[currentlyRunning][reg] += int(val)
                else:
                    registers[currentlyRunning][reg] += registers[currentlyRunning][val]
            case 'mul':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[currentlyRunning][reg] *= int(val)
                else:
                    registers[currentlyRunning][reg] *= registers[currentlyRunning][val]
            case 'mod':
                reg = inst['values'][0]
                val = inst['values'][1]
                if val.lstrip('-').isdigit():
                    registers[currentlyRunning][reg] %= int(val)
                else:
                    registers[currentlyRunning][reg] %= registers[currentlyRunning][val]
            case 'rcv':
                reg = inst['values'][0]
                if len(queues[currentlyRunning]) > 0:
                    registers[currentlyRunning][reg] = queues[currentlyRunning].pop(0)
                else:
                    waiting[currentlyRunning] = True
                    pointers[currentlyRunning] -= 1
            case 'jgz':
                reg = inst['values'][0]
                if reg.lstrip('-').isdigit():
                    compVal = int(reg)
                else:
                    compVal = registers[currentlyRunning][reg]
                val = inst['values'][1]
                if compVal > 0:
                    if val.lstrip('-').isdigit():
                        pointers[currentlyRunning] += int(val) - 1
                    else:
                        pointers[currentlyRunning] += registers[currentlyRunning][val] - 1
        pointers[currentlyRunning] += 1
        if not (0 <= pointers[currentlyRunning] < len(i)):
            waiting[currentlyRunning] = True
            terminated[currentlyRunning] = True   
    return runningCount
        

inputArray = [{'command': line.split()[0], 'values': line.split()[1:]} for line in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
