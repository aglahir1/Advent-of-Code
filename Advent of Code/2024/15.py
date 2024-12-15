
# Started
# Finished

f = open('2024/15.txt', 'r')
inputString = f.read()

# inputString = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# inputString = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

inputArray = inputString.split('\n\n')

field = dict()
field2 = dict()

for y, l in enumerate(inputArray[0].splitlines()):
    for x, c in enumerate(l):
        field2[f'{x * 2},{y}'] = {'#': '#', '.': '.', '@': '@', 'O': '['}[c]
        field2[f'{(x * 2) + 1},{y}'] = {'#': '#', '.': '.', '@': '.', 'O': ']'}[c]
        field[f'{x},{y}'] = c
        if c == '@':
            startx = x
            starty = y
        
def isMovable(x: int, y: int, dir: str, grid: dict[str,str]) -> bool:
    (dx, dy) = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[dir]
    x += dx
    y += dy
    target = grid[f'{x},{y}']
    if target == '#':
        return False
    if target == '.':
        return True
    if target in 'O[]':
        return isMovable(x, y, dir, grid)
    print(f'PANIC tried to move {target} at {x},{y} {dir}')
        
def isMovable2(x: int, y: int, dir: str, grid: dict[str,str]) -> bool:
    (dx, dy) = {'^': (0, -1), 'v': (0, 1)}[dir]
    x += dx
    y += dy
    target = grid[f'{x},{y}']
    if target == '#':
        return False
    if target == '.':
        return True
    if target in '[]':
        return all([isMovable2(x, y, dir, grid), isMovable2(x + [-1, 1][target == '['], y, dir, grid)])
    print(f'PANIC2 tried to move {target} at {x},{y} {dir}')
    
def move(x: int, y: int, dir: str, grid: dict[str,str]) -> dict[str,str]:
    (dx, dy) = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[dir]
    nx = x + dx
    ny = y + dy
    old = grid[f'{x},{y}']
    target = grid[f'{nx},{ny}']
    if target in 'O[]':
        grid = move(nx, ny, dir, grid)
    grid[f'{nx},{ny}'] = old
    grid[f'{x},{y}'] = '.'
    return grid
    
def move2(x: int, y: int, dir: str, grid: dict[str,str]) -> dict[str,str]:
    (dx, dy) = {'^': (0, -1), 'v': (0, 1)}[dir]
    nx = x + dx
    ny = y + dy
    old = grid[f'{x},{y}']
    target = grid[f'{nx},{ny}']
    if target in '[]':
        grid = move2(nx, ny, dir, grid)
        grid = move2(nx + [-1, 1][target == '['], ny, dir, grid)
    grid[f'{nx},{ny}'] = old
    grid[f'{x},{y}'] = '.'
    return grid

def printGrid(grid, h, w):
    for y in range(h):
        for x in range(w):
            print(grid[f'{x},{y}'], end='')
        print()
        
def calcScore(grid):
    runningScore = 0
    for k, v in grid.items():
        if v in 'O[':
            runningScore += int(k.split(',')[0]) + int(k.split(',')[1]) * 100
    return runningScore
    

def partOne(grid, instructions):
    x = startx
    y = starty
    for i in instructions:
        if isMovable(x, y, i, grid):
            grid = move(x, y, i, grid)
            (dx, dy) = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[i]
            x += dx
            y += dy
    printGrid(grid, len(inputArray[0].splitlines()), len(inputArray[0].splitlines()[0]))
    return calcScore(grid)
            
def partTwo(grid, instructions):
    x = startx * 2
    y = starty
    for i in instructions:
        if i in '<>':
            if isMovable(x, y, i, grid):
                grid = move(x, y, i, grid)
                (dx, dy) = {'<': (-1, 0), '>': (1, 0)}[i]
                x += dx
                y += dy
        else:
            if isMovable2(x, y, i, grid):
                grid = move2(x, y, i, grid)
                (dx, dy) = {'^': (0, -1), 'v': (0, 1)}[i]
                x += dx
                y += dy
    printGrid(grid, len(inputArray[0].splitlines()), len(inputArray[0].splitlines()[0]) * 2)
    return calcScore(grid)

instructions = inputArray[1].replace('\n', '')

grid = field.copy()
print(partOne(grid, instructions))

grid = field2.copy()
print(partTwo(grid, instructions))
