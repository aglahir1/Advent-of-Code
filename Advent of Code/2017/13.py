
# Started
# Finished

f = open('2017/13.txt', 'r')
inputString = f.read()

# inputString = """0: 3
# 1: 2
# 4: 4
# 6: 4"""

def partOne(i):
    runningSum = 0
    for line in i:
        d = (line[1] - 1) * 2
        if line[0] % d == 0:
            runningSum += line[0] * line[1]
    return runningSum

def partTwo(i):
    delay = 0
    while True:
        if all([(line[0] + delay) % ((line[1] - 1) * 2) > 0 for line in i]):
            return delay
        delay += 1

inputArray = [[int(j) for j in x.split(': ')] for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
