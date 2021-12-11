
# Started 16:17
# Finished 16:58


inputString = """3172537688
4566483125
6374512653
8321148885
4342747758
1362188582
7582213132
6887875268
7635112787
7242787273"""

#inputString = """5483143223
#2745854711
#5264556173
#6141336146
#6357385478
#4167524645
#2176841721
#6882881134
#4846848554
#5283751526"""

def energise(i):
    result = []
    flashers = []
    for y in range(len(i)):
        result.append([])
        for x in range(len(i[y])):
            a = i[y][x] + 1
            if a == 10:
                flashers.append([x, y])
            result[-1].append(a)
    return [result, flashers]

def energiseLocal(o, i):
    x = o[0]
    y = o[1]
    f = []
    if y > 0 and x > 0:
        i[y-1][x-1] += 1
        if i[y-1][x-1] == 10:
            f.append([x-1, y-1])
    if y > 0:
        i[y-1][x] += 1
        if i[y-1][x] == 10:
            f.append([x, y-1])
    if y > 0 and x < 9:
        i[y-1][x+1] += 1
        if i[y-1][x+1] == 10:
            f.append([x+1, y-1])
    if x > 0:
        i[y][x-1] += 1
        if i[y][x-1] == 10:
            f.append([x-1, y])
    if x < 9:
        i[y][x+1] += 1
        if i[y][x+1] == 10:
            f.append([x+1, y])
    if y < 9 and x > 0:
        i[y+1][x-1] += 1
        if i[y+1][x-1] == 10:
            f.append([x-1, y+1])
    if y < 9:
        i[y+1][x] += 1
        if i[y+1][x] == 10:
            f.append([x, y+1])
    if y < 9 and x < 9:
        i[y+1][x+1] += 1
        if i[y+1][x+1] == 10:
            f.append([x+1, y+1])
    return [i, f]

def resetFlashed(i):
    for y in range(len(i)):
        for x in range(len(i[y])):
            if i[y][x] > 9: i[y][x] = 0
    return i

def partOne(i):
    step = 100
    flashed = 0
    while step > 0:
        energised = energise(i)
        i = energised[0][:]
        flashing = energised[1][:]
        while flashing:
            e = energiseLocal(flashing.pop(), i)
            flashing += e[1][:]
            i = e[0][:]
            flashed += 1
        i = resetFlashed(i)[:]
        step -= 1
    return flashed

def partTwo(i):
    step = 0
    while True:
        flashed = 0
        energised = energise(i)
        i = energised[0][:]
        flashing = energised[1][:]
        while flashing:
            e = energiseLocal(flashing.pop(), i)
            flashing += e[1][:]
            i = e[0][:]
            flashed += 1
        i = resetFlashed(i)[:]
        step += 1
        if flashed == 100: break

    return step

inputArray = inputString.splitlines()

octopi =[]
for entry in inputArray:
    octopi.append([int(x) for x in entry])

print(partOne(octopi))

print(partTwo(octopi))