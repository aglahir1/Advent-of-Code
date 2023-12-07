
# Started
# Finished

f = open('2017/11.txt', 'r')
inputString = f.read()

def sign(x: int):
    if x < 0:
        return '-'
    return '+'

def manhattanOnHex(posx, posy):
    if sign(posx) == sign(posy):
        return abs(posx) + abs(posy)
    return max(abs(posx), abs(posy))
    

def partOne(i):
    position = [0, 0]
    for step in i:
        match step:
            case 'n':
                position[1] += 1
            case 's':
                position[1] -= 1
            case 'ne':
                position[0] += 1
            case 'sw':
                position[0] -= 1
            case 'nw':
                position[0] -= 1
                position[1] += 1
            case 'se':
                position[0] += 1
                position[1] -= 1
    return manhattanOnHex(*position)

def partTwo(i):
    position = [0, 0]
    maxdist = 0
    for step in i:
        match step:
            case 'n':
                position[1] += 1
            case 's':
                position[1] -= 1
            case 'ne':
                position[0] += 1
            case 'sw':
                position[0] -= 1
            case 'nw':
                position[0] -= 1
                position[1] += 1
            case 'se':
                position[0] += 1
                position[1] -= 1
        dist = manhattanOnHex(*position)
        if dist > maxdist: maxdist = dist
    return maxdist

inputArray = inputString.split(',')

print(partOne(inputArray))

print(partTwo(inputArray))
