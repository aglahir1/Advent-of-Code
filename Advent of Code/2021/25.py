
# Started
# Finished

import copy

f = open('2021/25.txt', 'r')
inputString = f.read()

def print2DArray(arr):
    for r in arr:
        for t in r:
            print(end=str(t)+' ')
        print()
    print()

def takeTurn(oceanFloor):
    movement=False
    oceanFloor2 = copy.deepcopy(oceanFloor)
    for y,r in enumerate(oceanFloor):
        for x,t in enumerate(r):
            if t == '>':
                if x==len(r)-1:
                    if oceanFloor[y][0] == '.':
                        oceanFloor2[y][x] = '.'
                        oceanFloor2[y][0] = '>'
                        movement=True
                else:
                    if oceanFloor[y][x+1] == '.':
                        oceanFloor2[y][x] = '.'
                        oceanFloor2[y][x+1] = '>'
                        movement=True
    oceanFloor3 = copy.deepcopy(oceanFloor2)
    for y,r in enumerate(oceanFloor2):
        for x,t in enumerate(r):
            if t == 'v':
                if y==len(oceanFloor2)-1:
                    if oceanFloor2[0][x] == '.':
                        oceanFloor3[y][x] = '.'
                        oceanFloor3[0][x] = 'v'
                        movement=True
                else:
                    if oceanFloor2[y+1][x] == '.':
                        oceanFloor3[y][x] = '.'
                        oceanFloor3[y+1][x] = 'v'
                        movement=True
    return (oceanFloor3[:],movement)

def partOne(oceanFloor):
    turnCount = 0
    movement = True
    while movement:
        turnCount += 1
        oceanFloor, movement = takeTurn(oceanFloor)
    return turnCount


#inputString = """v...>>.vv>
#.vv>>.vv..
#>>.>v>...v
#>>v>>.>.v.
#v>v.vv.v..
#>.>>..v...
#.vv..>.>v.
#v.v..>>v.v
#....v..v.>"""

inputArray = inputString.splitlines()
oceanFloor = []
for entry in inputArray:
    oceanFloor.append(list(entry))

print(partOne(oceanFloor))

#print(partTwo(inputArray))
