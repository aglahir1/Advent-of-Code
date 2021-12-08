
import re
import pprint
import json
import itertools

f = open('2021/05.txt', 'r')
inputString = f.read()

#inputString = """0,9 -> 5,9
#8,0 -> 0,8
#9,4 -> 3,4
#2,2 -> 2,1
#7,0 -> 7,4
#6,4 -> 2,0
#0,9 -> 2,9
#3,4 -> 1,4
#0,0 -> 8,8
#5,5 -> 8,2"""

inputArray = inputString.splitlines()

entries = []

oceanFloor = [[0]*1000 for _ in range(1000)]

def affectedArray(a, c):
    result = []
    for x in range(a[0],c[0]+1):
        for y in range(a[1],c[1]+1):
            result.append([x,y])
    return result

for entry in inputArray:
    entry = entry.split()
    x1y1 = entry[0].split(',')
    x1y1 = [int(x1y1[0]), int(x1y1[1])]
    x2y2 = entry[2].split(',')
    x2y2 = [int(x2y2[0]), int(x2y2[1])]
    entries.append([x1y1, x2y2])

for entry in entries:
    entry.sort()
    if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]:
        line = affectedArray(entry[0], entry[1])
    else:
        line = []
        for x in range(abs(entry[0][1] - entry[1][1]) + 1):
            if entry[0][1] > entry[1][1]: coords = [entry[0][0] + x, entry[0][1] - x]
            else: coords = [entry[0][0] + x, entry[0][1] + x]
            line.append(coords[:])
    for dot in line:
        oceanFloor[dot[1]][dot[0]] += 1


count = 0

for x in oceanFloor:
    print(x)
    for y in x:
        if y > 1: count += 1

print(count)