
# Started 03:00
# Finished

import itertools

f = open('2021/14.txt', 'r')
inputString = f.read()

#inputString = """NNCB

#CH -> B
#HH -> N
#CB -> H
#NH -> C
#HB -> C
#HC -> B
#HN -> C
#NN -> C
#BH -> H
#NC -> B
#NB -> B
#BN -> B
#BB -> N
#BC -> B
#CC -> N
#CN -> C"""

def pairwise(l):
    re = []
    for i in range(len(l) - 1):
        re.append(l[i] + l[i + 1])
    return re

def mergeList(l):
    re = l[0][0]
    for x in l:
        re += x[1:]
    return re

def partOne(start, rules):
    steps = 0
    while steps < 10:
        pairs = pairwise(start)
        advanced = []
        for x in pairs:
            advanced.append(x[0] + rules[x] + x[1])
        start = mergeList(advanced)
        steps += 1
    start = list(start)
    start.sort()
    unduped = [x[0] for x in list(itertools.groupby(start))]
    counted = [[x, start.count(x)] for x in unduped]
    counted.sort(key = lambda x: x[1])
    return counted[-1][1] - counted[0][1]

def partTwo(s, r, c, p):
    ep = p.copy()
    for x in pairwise(s):
        p[x] += 1
    for x in s:
        c[x] += 1
    steps = 0
    while steps < 40:
        np = ep.copy()
        for x in p:
            if p[x]:
                c[r[x]] += p[x]
                np[x[0]+r[x]] += p[x]
                np[r[x]+x[1]] += p[x]
        p = np.copy()
        steps += 1
    ma = max([v for v in c.values()])
    mi = min([v for v in c.values()])
    return ma - mi

inputArray = inputString.splitlines()

start = inputArray[0]
rules = {k: v for k,v in [x.split(' -> ') for x in inputArray[2:]]}
count = {v: 0 for v in [x.split(' -> ')[1] for x in inputArray[2:]]}
pairs = {k: 0 for k in [x.split(' -> ')[0] for x in inputArray[2:]]}

print(partOne(start, rules))

print(partTwo(start, rules, count, pairs))
