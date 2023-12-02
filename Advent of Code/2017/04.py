
# Started
# Finished

f = open('2017/04.txt', 'r')
inputString = f.read()

def partOne(i):
    runningSum = 0
    for line in i:
        passphrase = line.split()
        if len(passphrase) == len(set(passphrase)): runningSum += 1
    return runningSum

def partTwo(i):
    runningSum = 0
    for line in i:
        passphrase = line.split()
        rearranged = [''.join(sorted(list(x))) for x in passphrase]
        if len(passphrase) == len(set(rearranged)): runningSum += 1
    return runningSum

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
