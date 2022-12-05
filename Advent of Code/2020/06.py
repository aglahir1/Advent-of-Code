
# Started
# Finished

f = open('2020/06.txt', 'r')
inputString = f.read()

#inputString = """abc

#a
#b
#c

#ab
#ac

#a
#a
#a
#a

#b"""

def commonString(s1, s2):
    sr = ''
    for c in s1:
        if c in s2: sr += c
    return sr

def partOne(i):
    total = 0
    for x in i:
        x = set(x.replace('\n',''))
        total += len(x)
    return total

def partTwo(i):
    total = 0
    for x in i:
        x = x.splitlines()
        s = x[0]
        if len(x) > 1: 
            for c in x[1:]: 
                s = commonString(s, c)
        total += len(s)
    return total

inputArray = inputString.split('\n\n')

print(partOne(inputArray))

print(partTwo(inputArray))
