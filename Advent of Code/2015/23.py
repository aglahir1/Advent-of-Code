
# Started 04:56
# Finished 05:21



f = open('2015/23.txt', 'r')
inputString = f.read()

#inputString = """inc a
#jio a, +2
#tpl a
#inc a"""

inputArray = inputString.splitlines()

registerA = 1
registerB = 0

commandArray = []

for entry in inputArray:
    entry = entry.split()
    commandArray.append(entry)

i = 0

while 0 <= i < len(commandArray):
    comm = commandArray[i][0]
    affect = commandArray[i][1]
    if comm == 'hlf':
        i += 1
        if affect == 'a':
            registerA = int(registerA / 2)
        if affect == 'b':
            registerB = int(registerB / 2)
        continue
    if comm == 'tpl':
        i += 1
        if affect == 'a':
            registerA *= 3
        if affect == 'b':
            registerB *= 3
        continue
    if comm == 'inc':
        i += 1
        if affect == 'a':
            registerA += 1
        if affect == 'b':
            registerB += 1
        continue
    if comm == 'jmp':
        i += int(affect)
        continue
    if comm == 'jie':
        if affect[0] == 'a':
            if registerA % 2 == 0: 
                i += int(commandArray[i][2])
            else: i+= 1
        if affect[0] == 'b':
            if registerB % 2 == 0: 
                i += int(commandArray[i][2])
            else: i+= 1
        continue
    if comm == 'jio':
        if affect[0] == 'a':
            if registerA == 1: 
                i += int(commandArray[i][2])
            else: i+= 1
        if affect[0] == 'b':
            if registerB == 1: 
                i += int(commandArray[i][2])
            else: i+= 1
        continue
    
print('A: ' + str(registerA))
print('B: ' + str(registerB))