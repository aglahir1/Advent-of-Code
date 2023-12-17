
# Started
# Finished

from functools import cache
import sys


f = open('2023/16.txt', 'r')
inputString = f.read()

# inputString = """.|...!....
# |.-.!.....
# .....|-...
# ........|.
# ..........
# .........!
# ..../.!!..
# .-.-/..|..
# .|....-|.!
# ..//.|...."""

inputArray = inputString.splitlines()

def moveBeam(beam: list):
    direction = beam[1]
    position = beam[0]
    match direction:
        case 'r':
            return (position[0] + 1, position[1])
        case 'l':
            return (position[0] - 1, position[1])
        case 'u':
            return (position[0], position[1] - 1)
        case 'd':
            return (position[0], position[1] + 1)
        
def moveBeamNew(beam: tuple):
    direction = beam[2]
    y = beam[1]
    x = beam[0]
    match direction:
        case 'r':
            x += 1
        case 'l':
            x -= 1
        case 'u':
            y -= 1
        case 'd':
            y += 1
    return (x, y, direction)

alreadyWalked = set()

        
@cache
def walkBeam(energized: frozenset[tuple], beam: tuple, fieldSize: int):
    newBeam = moveBeamNew(beam)
    if newBeam[0] < 0 or newBeam[0] == fieldSize or newBeam[1] < 0 or newBeam[1] == fieldSize or newBeam in alreadyWalked:
        return energized
    energized = energized.union({(newBeam[0],newBeam[1])})
    alreadyWalked.add(newBeam)
    match inputArray[newBeam[1]][newBeam[0]]:
        case '.':
            return walkBeam(energized, newBeam, fieldSize)
        case '|':
            if newBeam[2] in 'ud':
                return walkBeam(energized, newBeam, fieldSize)
            else:
                return energized.union(walkBeam(energized, (newBeam[0],newBeam[1],'u'), fieldSize), walkBeam(energized, (newBeam[0],newBeam[1],'d'), fieldSize))
        case '-':
            if newBeam[2] in 'lr':
                return walkBeam(energized, newBeam, fieldSize)
            else:
                return energized.union(walkBeam(energized, (newBeam[0],newBeam[1],'l'), fieldSize), walkBeam(energized, (newBeam[0],newBeam[1],'r'), fieldSize))
        case '/':
            match newBeam[2]:
                case 'r':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'u'), fieldSize)
                case 'l':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'d'), fieldSize)
                case 'u':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'r'), fieldSize)
                case 'd':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'l'), fieldSize)
        case '!':
            match newBeam[2]:
                case 'r':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'d'), fieldSize)
                case 'l':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'u'), fieldSize)
                case 'u':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'l'), fieldSize)
                case 'd':
                    return walkBeam(energized, (newBeam[0],newBeam[1],'r'), fieldSize)
    
    

def partOne(i):
    global alreadyWalked
    alreadyWalked = set()
    energized = frozenset()
    energized = walkBeam(energized, (-1, 0, 'r'), len(i))
    return len(energized)
                

def partTwo(i):
    pass


print(partOne(inputArray))

print(partTwo(inputArray))
