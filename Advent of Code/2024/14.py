
# Started
# Finished

import re


f = open('2024/14.txt', 'r')
inputString = f.read()
gridW = 101
gridH = 103

# inputString = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""
# gridW = 11
# gridH = 7

regbot = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
inputArray = inputString.splitlines()

bots = []
for bot in inputArray:
    parse = regbot.match(bot)
    bots.append({'x': int(parse.group(1)), 'y': int(parse.group(2)), 'vx': int(parse.group(3)), 'vy': int(parse.group(4))})
    
def drawBots(positions: set[tuple[int]], time: int):
    print(time)
    for y in range(gridH):
        print('   ', end='')
        for x in range(gridW):
            if (x, y) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
    print('-' * (gridW + 10))
    
def calcSecurityScore(finalPositions: list[tuple[int]]) -> int:
    a = b = c = d = 0
    for bot in finalPositions:
        if 0 <= bot[0] < gridW // 2 and 0 <= bot[1] < gridH // 2:
            a += 1
        elif 0 <= bot[0] < gridW // 2 and gridH // 2 < bot[1] < gridH:
            b += 1
        elif gridW // 2 < bot[0] < gridW and 0 <= bot[1] < gridH // 2:
            c += 1
        elif gridW // 2 < bot[0] < gridW and gridH // 2 < bot[1] < gridH:
            d += 1
    return a * b * c * d

def partOne():
    finalPositions = []
    for b in bots:
        finalPositions.append(((b['x'] + b['vx'] * 100) % gridW, (b['y'] + b['vy'] * 100) % gridH))
    return calcSecurityScore(finalPositions)

def partTwo():
    t = 30
    while True:
        drawBots({((b['x'] + b['vx'] * t) % gridW, (b['y'] + b['vy'] * t) % gridH) for b in bots}, t)
        t += 103
        input()
        


print(partOne())

print(partTwo())
