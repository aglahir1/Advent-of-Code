
# Started
# Finished

f = open('2022/05.txt', 'r')
inputString = f.read()

#inputString = """    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2"""

def parseCrates(c):
    c = c.splitlines()
    stacks = int((len(c[-1])+1)/4)
    crates = {}
    for s in range(stacks):
        crates[str(s + 1)] = []
    for level in c[:-1]:
        while level.find(']') != -1:
            stack = int((level.find(']') + 2) / 4)
            crates[str(stack)].append(level[(stack * 4)-3])
            level = level[:(stack * 4) - 2] + ' ' + level[(stack * 4) - 1:]
    return crates

def parseInstructions(i):
    ins = []
    for inst in i:
        insta = inst.split()
        ins.append({'amount': int(insta[1]), 'from': insta[3], 'to': insta[5]})
    return ins

def partOne(c, i):
    for ins in i:
        for x in range(ins['amount']):
            moving = c[ins['from']][0]
            c[ins['to']] = [moving] + c[ins['to']]
            c[ins['from']] = c[ins['from']][1:]
    result = ''
    for x in range(len(c)):
        result += c[str(x + 1)][0]
    return result

def partTwo(c, i):
    for ins in i:
        moving = c[ins['from']][:ins['amount']]
        c[ins['to']] = moving + c[ins['to']]
        c[ins['from']] = c[ins['from']][ins['amount']:]
    result = ''
    for x in range(len(c)):
        result += c[str(x + 1)][0]
    return result

crates = inputString.split('\n\n')[0]
crates = parseCrates(crates)
instructions = inputString.split('\n\n')[1]
instructionArray = instructions.splitlines()
instructionArray = parseInstructions(instructionArray)

print(partOne(crates, instructionArray[:]))

crates = inputString.split('\n\n')[0]
crates = parseCrates(crates)

print(partTwo(crates, instructionArray))
