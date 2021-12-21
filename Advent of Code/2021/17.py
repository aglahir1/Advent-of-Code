
# Started 11:00
# Finished 11:38

f = open('2021/17.txt', 'r')
inputString = f.read()

def advancePos(pos, vel):
    pos['x'] += vel['x']
    pos['y'] += vel['y']
    if vel['x'] > 0: vel['x'] -= 1
    if vel['x'] < 0: vel['x'] += 1
    vel['y'] -= 1
    return pos, vel

def checkTarget(pos, target):
    return target['y'][0] <= pos['y'] <= target['y'][1] and target['x'][0] <= pos['x'] <= target['x'][1]

def partOne(target):
    if True:
        targetLength = target['y'][1] - target['y'][0]
        depth = -target['y'][1]
        return sum(range(targetLength + depth))
    else:
        position = {'x': 0, 'y': 0}
        initVelocity = {'x': 7, 'y': 9}
        velocity = initVelocity.copy()
        while True:
            position, velocity = advancePos(position, velocity)
            if checkTarget(position, target): break
            if position['y'] < target['y'][0]: break
        print(position)
        print(velocity)
        return sum(range(initVelocity['y'] + 1))

def partTwo(target):
    maxY = -target['y'][0]
    maxX = target['x'][1]
    minX = 0
    check = 0
    while not minX:
        if sum(range(check + 1)) >= target['x'][0]: minX = check
        check += 1
    possibleVelocities = []
    for y in range(target['y'][0], maxY + 1):
        for x in range(maxX + 1):
            position = {'x': 0, 'y': 0}
            initVelocity = {'x': x, 'y': y}
            velocity = initVelocity.copy()
            while True:
                position, velocity = advancePos(position, velocity)
                if checkTarget(position, target): break
                if position['y'] < target['y'][0]: break
            if checkTarget(position, target):
                possibleVelocities.append(initVelocity)
    return len(possibleVelocities)
target = {'y': [-148, -89], 'x': [139, 187]}

#target = {'y': [-10, -5], 'x': [20, 30]}

print(partOne(target))

print(partTwo(target))


