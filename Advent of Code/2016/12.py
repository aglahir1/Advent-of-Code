
# Started
# Finished

f = open('2016/12.txt', 'r')
inputString = f.read()

# inputString = """cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a"""

def executeInst(assembunny: dict) -> dict:
    inst = assembunny['instructions'][assembunny['pointer']]
    inst = inst.split(' ')
    if inst[0] == 'cpy':
        if inst[1].isnumeric():
            assembunny[inst[2]] = int(inst[1])
        else:
            assembunny[inst[2]] = assembunny[inst[1]]
    elif inst[0] == 'inc':
        assembunny[inst[1]] += 1
    elif inst[0] == 'dec':
        assembunny[inst[1]] -= 1
    elif inst[0] == 'jnz':
        if inst[1].isnumeric() and inst[1] != '0':
            assembunny['pointer'] += int(inst[2]) - 1
        elif assembunny[inst[1]] != 0:
            assembunny['pointer'] += int(inst[2]) - 1
    assembunny['pointer'] += 1
    return assembunny

def partOne(i):
    assembunny = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'pointer': 0, 'instructions': i}
    while 0 <= assembunny['pointer'] < len(assembunny['instructions']):
        assembunny = executeInst(assembunny)
    return assembunny

def partTwo(i):
    assembunny = {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'pointer': 0, 'instructions': i}
    while 0 <= assembunny['pointer'] < len(assembunny['instructions']):
        assembunny = executeInst(assembunny)
    return assembunny

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
