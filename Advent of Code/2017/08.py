
# Started
# Finished


f = open('2017/08.txt', 'r')
inputString = f.read()

#inputString = """b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10"""

def compare(r, c, n):
    if c == '==': return r == n
    if c == '>': return r > n
    if c == '>=': return r >= n
    if c == '<': return r < n
    if c == '<=': return r <= n
    if c == '!=': return r != n

def partOne(i):
    highest = 0
    registers = {r: 0 for r in i['registers']}
    for ins in i['instructions']:
        struct = ins.split()
        if not compare(registers[struct[4]], struct[5], int(struct[6])):
            continue
        if struct[1] == 'inc':
            registers[struct[0]] += int(struct[2])
        else:
            registers[struct[0]] -= int(struct[2])
        if registers[struct[0]] > highest:
            highest = registers[struct[0]]
    print(max(registers.values()))
    return highest


instructions = inputString.splitlines()

inputArray = {'registers': set([x.split()[0] for x in instructions]), 'instructions': instructions} 

print(partOne(inputArray))
