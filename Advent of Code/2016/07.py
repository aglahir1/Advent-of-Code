
# Started 02:59
# Finished 03:49

import re

f = open('2016/07.txt', 'r')
inputString = f.read()

#inputString = """aba[bab]xyz
#xyx[xyx]xyx
#aaa[kek]eke
#zazbz[bzb]cdb"""

def partOne(i):
    abba = re.compile(r'(.)(.)\2\1')
    xabba = re.compile(r'\[[^\]]*(.)(.)\2\1')
    count = 0
    for entry in i:
        s = abba.search(entry)
        if s:
            if not xabba.search(entry):
                if s.group(1) != s.group(2):
                    count += 1
    return count


def partTwo(i):
    aba = re.compile(r'(.)(.)\1')
    count = 0
    for entry in i:
        a = entry.split('[')
        entry = []
        for x in range(len(a)):
            entry += a[x].split(']')
        possibleABAs = []
        for x in [x for x in entry if entry.index(x) % 2 == 0]:
            check = 0
            while True:
                z = aba.search(x[check:])
                if z:
                    possibleABAs.append(z.group(2) + z.group(1) + z.group(2))
                    check += z.start() + 1
                else:
                    break
        for x in [x for x in entry if entry.index(x) % 2 == 1]:
            cor = False
            for z in possibleABAs:
                if x.find(z) != -1: 
                    cor = True
                    break
            if cor:
                count += 1
                break
    return count




inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
