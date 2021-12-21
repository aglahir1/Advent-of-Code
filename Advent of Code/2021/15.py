
# Started
# Finished

from os import cpu_count


f = open('2021/15.txt', 'r')
inputString = f.read()

#inputString = """1163751742
#1381373672
#2136511328
#3694931569
#7463417111
#1319128137
#1359912421
#3125421639
#1293138521
#2311944581"""

def partOne(grid):

    wall = len(grid)

    visited = [[0] * wall for _ in range(wall)]
    tentativeDistance = [[9999999999] * wall for _ in range(wall)]

    tentativeDistance[0][0] = 0

    cN = {'x': 0, 'y': 0}

    while True:
        x = cN['x']
        y = cN['y']
        cV = tentativeDistance[y][x]
        if x > 0: #left
            td = grid[y][x - 1] + cV
            if td < tentativeDistance[y][x - 1]: tentativeDistance[y][x - 1] = td
        if x < wall - 1: #right
            td = grid[y][x + 1] + cV
            if td < tentativeDistance[y][x + 1]: tentativeDistance[y][x + 1] = td
        if y > 0: # up
            td = grid[y - 1][x] + cV
            if td < tentativeDistance[y - 1][x]: tentativeDistance[y - 1][x] = td
        if y < wall - 1: #down
            td = grid[y + 1][x] + cV
            if td < tentativeDistance[y + 1][x]: tentativeDistance[y + 1][x] = td
        visited[y][x] = 1
        #check EndNode visited
        if visited[-1][-1]: break
        #check PathNotFound:
        breaking = False
        for ir, r in enumerate(tentativeDistance):
            for ic, c in enumerate(r):
                if not visited[ir][ic] and c != 9999999999: breaking = True
                if breaking: break
            if breaking: break
        if not breaking: break
        #select new Node
        low = 9999999999
        nX = x
        nY = y
        for ir, r in enumerate(tentativeDistance):
            for ic, c in enumerate(r):
                if not visited[ir][ic] and c < low:
                    low = c
                    nX = ic
                    nY = ir
        cN = {'x': nX, 'y': nY}

    return (tentativeDistance[-1][-1])

def partTwo(i):
    pass

inputArray = inputString.splitlines()

grid = [[int(j) for j in x] for x in inputArray]
grid2 = [[int(j) % 9 + 1 for j in x] for x in grid]
grid3 = [[int(j) % 9 + 1 for j in x] for x in grid2]
grid4 = [[int(j) % 9 + 1 for j in x] for x in grid3]
grid5 = [[int(j) % 9 + 1 for j in x] for x in grid4]
grid6 = [[int(j) % 9 + 1 for j in x] for x in grid5]
grid7 = [[int(j) % 9 + 1 for j in x] for x in grid6]
grid8 = [[int(j) % 9 + 1 for j in x] for x in grid7]
grid9 = [[int(j) % 9 + 1 for j in x] for x in grid8]

gridCol1 = grid + grid2 + grid3 + grid4 + grid5
gridCol2 = grid2 + grid3 + grid4 + grid5 + grid6
gridCol3 = grid3 + grid4 + grid5 + grid6 + grid7
gridCol4 = grid4 + grid5 + grid6 + grid7 + grid8
gridCol5 = grid5 + grid6 + grid7 + grid8 + grid9

fullGrid = [a + b + c + d + e for a, b, c, d, e in zip(gridCol1, gridCol2, gridCol3, gridCol4, gridCol5)]



print('part ONE: ' + str(partOne(grid)))

print(partOne(fullGrid))
