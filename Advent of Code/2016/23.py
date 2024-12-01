
# Started
# Finished

from copy import deepcopy


f = open('2016/23.txt', 'r')
inputString = f.read()

# inputString = """cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a"""

def actualisnumeric(n: str) -> bool:
    return n.lstrip('-').isnumeric()


def executeInst(assembunny: dict) -> dict:
    inst = assembunny['instructions'][assembunny['pointer']]
    if inst[0] == 'cpy':
        if inst[2] not in 'abcd': return assembunny
        if actualisnumeric(inst[1]):
            assembunny[inst[2]] = int(inst[1])
        else:
            assembunny[inst[2]] = assembunny[inst[1]]
    elif inst[0] == 'inc':
        if inst[1] not in 'abcd': return assembunny
        assembunny[inst[1]] += 1
    elif inst[0] == 'dec':
        if inst[1] not in 'abcd': return assembunny
        assembunny[inst[1]] -= 1
    elif inst[0] == 'jnz':
        if actualisnumeric(inst[2]):
            jmpval = int(inst[2])
        else:
            jmpval = assembunny[inst[2]]
        if jmpval == -2 and inst[1] in 'abcd':
            insts = assembunny['instructions'][assembunny['pointer'] - 2: assembunny['pointer']]
            if [i[0] for i in insts] in [['inc', 'dec'], ['dec', 'inc']]:
                if insts[0][0] == 'inc':
                    incer = insts[0]
                    decer = insts[1]
                else:
                    incer = insts[1]
                    decer = insts[0]
                if inst[1] == decer[1] and incer[1] in 'abcd':
                    assembunny[incer[1]] += assembunny[decer[1]]
                    assembunny[decer[1]] = 0
                    return assembunny
        if jmpval == -5 and inst[1] in 'abcd':
            insts = assembunny['instructions'][assembunny['pointer'] - 5: assembunny['pointer']]
            if [i[0] for i in insts] in [['cpy', 'inc', 'dec', 'jnz', 'dec'], ['cpy', 'dec', 'inc', 'jnz', 'dec']]:
                if insts[1][0] == 'inc':
                    incer = insts[1]
                    decer = insts[2]
                else:
                    incer = insts[2]
                    decer = insts[1]
                if inst[1] == insts[4][1] and insts[0][1] == decer[1] and insts[3][1] == insts[0][1] and incer[1] in 'abcd' and decer[1] in 'abcd':
                    assembunny[incer[1]] += (assembunny[decer[1]] * assembunny[inst[1]])
                    assembunny[inst[1]] = 0
                    return assembunny
        if actualisnumeric(inst[1]) and inst[1] != '0':
            assembunny['pointer'] += jmpval - 1
        elif assembunny[inst[1]] != 0:
            assembunny['pointer'] += jmpval - 1
    elif inst[0] == 'tgl':
        arg = assembunny['pointer'] + assembunny[inst[1]]
        if not 0 <= arg < len(assembunny['instructions']): return assembunny
        if len(assembunny['instructions'][arg]) == 2:
            if assembunny['instructions'][arg][0] != 'inc':
                assembunny['instructions'][arg][0] = 'inc'
            else:
                assembunny['instructions'][arg][0] = 'dec'
        else:
            if assembunny['instructions'][arg][0] != 'jnz':
                assembunny['instructions'][arg][0] = 'jnz'
            else:
                assembunny['instructions'][arg][0] = 'cpy'
    return assembunny

def partOne(i):
    assembunny = {'a': 7, 'b': 0, 'c': 0, 'd': 0, 'pointer': 0, 'instructions': i}
    while 0 <= assembunny['pointer'] < len(assembunny['instructions']):
        assembunny = executeInst(assembunny)
        assembunny['pointer'] += 1
    return assembunny

def partTwo(i):
    assembunny = {'a': 12, 'b': 0, 'c': 0, 'd': 0, 'pointer': 0, 'instructions': i}
    while 0 <= assembunny['pointer'] < len(assembunny['instructions']):
        assembunny = executeInst(assembunny)
        assembunny['pointer'] += 1
    return assembunny

inputArray = [x.split() for x in inputString.splitlines()]

print(partOne(deepcopy(inputArray)))

print(partTwo(deepcopy(inputArray)))
