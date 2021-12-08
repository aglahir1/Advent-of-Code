
# Started 15:52
# Finished P1 16:12
# Started P2 17:05
# Finished 17:10


f = open('2015/18.txt', 'r')
inputString = f.read()

size = 100

steps = 100


#inputString = """.#.#.#
#...##.
##....#
#..#...
##.#..#
#####.."""

#size = 6

#steps = 5

def printLights(grid):
    for row in grid:
        rowString = ''
        for col in row:
            rowString += str(col)
        print(rowString)

def calculateGrid(grid):
    count = 0
    for row in grid:
        count += sum(row)
    return count


inputArray = inputString.splitlines()

lights = [[0]*size for _ in range(size)]

for y, row in enumerate(inputArray):
    for x, col in enumerate(row):
        if col == '#': lights[y][x] = 1

lights[0][0] = lights[0][-1] = lights[-1][0] = lights[-1][-1] = 1

while(steps):
    nextLightGrid = [[]]
    for y in range(size):
        for x in range(size):
            count = 0
            result = lights[y][x]
            if y > 0 and x > 0: count += lights[y - 1][x - 1]
            if y > 0 and x < size - 1: count += lights[y - 1][x + 1]
            if y < size - 1 and x > 0: count += lights[y + 1][x - 1]
            if y < size - 1 and x < size - 1: count += lights[y + 1][x + 1]
            if y > 0: count += lights[y - 1][x]
            if y < size - 1: count += lights[y + 1][x]
            if x > 0: count += lights[y][x - 1]
            if x < size - 1: count += lights[y][x + 1]
            if lights[y][x] and count not in (2, 3): result = 0
            if not lights[y][x] and count == 3: result = 1
            nextLightGrid[y].append(result)
        nextLightGrid.append([])
    lights = nextLightGrid[:-1]
    lights[0][0] = lights[0][-1] = lights[-1][0] = lights[-1][-1] = 1
    steps -= 1

print(calculateGrid(lights))