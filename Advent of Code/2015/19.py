
# Started 17:41
# Finished 21:12

import re
import itertools

f = open('2015/19.txt', 'r')
inputString = f.read()

#inputString = """H => HO
#H => OH
#O => HH
#e => H
#e => O

#HOHOHO"""

inputArray = inputString.splitlines()

operations = []

goal = ['e']

regex = re.compile(r'.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z0-9])(?=[A-Z0-9])|$)')

for entry in inputArray[:-2]:
    entry = entry.split()
    matches = regex.finditer(entry[2])
    replacement = [m.group(0) for m in matches]
    operations.append([[entry[0]],replacement])

molecule = inputArray[-1]

matches = regex.finditer(molecule)
molecule = [m.group(0) for m in matches]

step = 0

def find_first_sublist(seq, sublist, start=0):
    length = len(sublist)
    for index in range(start, len(seq)):
        if seq[index:index+length] == sublist:
            return index, index+length
       

def oneStep(mol):
    results = []
    for op in operations:
        if len(mol) > 3 and op[0] == ['e']: continue
        pos = True
        checking = 0
        while pos:
            pos = find_first_sublist(mol, op[1], checking)
            if pos: 
                checking = pos[0] + 1
                results.append(mol[:])
                results[-1][pos[0]:pos[1]] = op[0]
                
    results.sort()
    endresult = list(k for k,_ in itertools.groupby(results))
    return endresult

def overlap(a, b):
    for x in a:
        if x in b: return x
    return False

def workDown(subset):
    global step
    workers = [subset[:]]
    while not overlap(workers, [x[1] for x in operations]):
        nA =[]
        for w in workers:
            nA += oneStep(w)
        nA.sort()
        if nA: 
            workers = list(k for k,_ in itertools.groupby(nA))
            step += 1
            print(len(workers))
            print('step' + str(step))
        if step == 48: 
            pass
        if len(workers[0]) == 4 or not nA: break
    if overlap(workers, [x[1] for x in operations]): return overlap(workers, [x[1] for x in operations])
    if len(workers) == 1: subset = workers[0][:]
    returner = []
    returner += [subset[0], '1'] + subset[2:-1] + ['2']
    return returner

def RnParse(mol):
    global step
    while 'Rn' in mol:
        b = find_first_sublist(mol, ['Ar'])[1]
        a = b - find_first_sublist(mol[::-1][len(mol) - b:], ['Rn'])[1]
        if mol[a-1:b] in [x[1] for x in operations]: 
            mol[a-1:b] = operations[[x[1] for x in operations].index(mol[a-1:b])][0]
            step +=1
            print('Rn' + str(step))
        else: mol[a-1:b] = workDown(mol[a-1:b])
    return mol

possibilities = [molecule[:]]

print(len(molecule) - molecule.count('Rn') * 2 - molecule.count('Y') * 2 - 1)

#while goal not in possibilities:
#    newarray = []
#    for x in possibilities:
#        newarray.append(RnParse(x))
#    newarray.sort()
#    possibilities = list(k for k,_ in itertools.groupby(newarray))
#    newarray = []
#    for x in possibilities:
#        newarray += oneStep(x)
#    newarray.sort()
#    possibilities = list(k for k,_ in itertools.groupby(newarray))
#    print(len(possibilities))
#    print(len(possibilities[0]))
#    step += 1

count = molecule.count('Rn')

print(step + count)