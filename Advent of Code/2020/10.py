
# Started
# Finished

f = open('2020/10.txt', 'r')
inputString = f.read()

#inputString = """28
#33
#18
#42
#31
#14
#46
#20
#48
#47
#24
#23
#49
#45
#19
#38
#39
#11
#1
#32
#25
#35
#8
#17
#7
#9
#4
#2
#34
#10
#3"""

def partOne(i):
    devices = [int(x) for x in i]
    devices += [0]
    devices.sort()
    devices += [devices[-1]+3]
    differences = {1: 0, 2: 0, 3: 0}
    for a, b in zip(devices[:-1], devices[1:]):
        differences[b - a] += 1
    return differences[1] * differences[3]

def explorePath(x, devices, calculated):
    if x in calculated: return [calculated[x], calculated]
    paths = 0
    for j in range(x + 1, x + 4):
        if j in devices: paths += explorePath(j, devices, calculated)[0]
    calculated[x] = paths
    return [paths, calculated]


def partTwo(i):
    devices = [int(x) for x in i]
    devices += [0]
    devices.sort()
    devices += [devices[-1]+3]
    return explorePath(0, devices, {devices[-1]: 1})[0]
    

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
