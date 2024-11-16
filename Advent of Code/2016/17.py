
# Started
# Finished

from copy import deepcopy
from hashlib import md5

OPEN = 'bcdef'

passcode = 'vwbaicqe'

# passcode = 'ulqzkmiv'
# passcode = 'kglvqrro'
# passcode = 'ihgpwlah'

def getDoors(position: tuple[int,int], route: str) -> str:
    hash = md5(str.encode(passcode + route)).hexdigest()
    availableDoors = ''
    if position[1] != 0 and hash[0] in OPEN:
        availableDoors += 'U'
    if position[1] != 3 and hash[1] in OPEN:
        availableDoors += 'D'
    if position[0] != 0 and hash[2] in OPEN:
        availableDoors += 'L'
    if position[0] != 3 and hash[3] in OPEN:
        availableDoors += 'R'
    return availableDoors


def partOne():
    runningPaths = [((0,0), '')]
    steps = 0
    while True:
        newRunningPaths = []
        for p in runningPaths:
            doors = getDoors(p[0], p[1])
            if doors == '': continue
            for d in doors:
                match d:
                    case 'U':
                        newPos = (p[0][0], p[0][1] - 1)
                    case 'D':
                        newPos = (p[0][0], p[0][1] + 1)
                    case 'L':
                        newPos = (p[0][0] - 1, p[0][1])
                    case 'R':
                        newPos = (p[0][0] + 1, p[0][1])
                if newPos == (3,3): return p[1] + d
                newRunningPaths.append((newPos, p[1] + d))
        steps += 1
        print(steps)
        runningPaths = deepcopy(newRunningPaths)
    

def partTwo():
    runningPaths = [((0,0), '')]
    steps = 0
    currentLongest = 0
    while True:
        newRunningPaths = []
        for p in runningPaths:
            doors = getDoors(p[0], p[1])
            if doors == '': continue
            for d in doors:
                match d:
                    case 'U':
                        newPos = (p[0][0], p[0][1] - 1)
                    case 'D':
                        newPos = (p[0][0], p[0][1] + 1)
                    case 'L':
                        newPos = (p[0][0] - 1, p[0][1])
                    case 'R':
                        newPos = (p[0][0] + 1, p[0][1])
                if newPos == (3,3):
                    currentLongest = len(p[1]) + 1
                    continue
                newRunningPaths.append((newPos, p[1] + d))
        steps += 1
        if len(newRunningPaths) == 0: return currentLongest
        runningPaths = deepcopy(newRunningPaths)


print(partOne())

print(partTwo())
