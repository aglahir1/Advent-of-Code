
# Started
# Finished

f = open('2024/10.txt', 'r')
inputString = f.read()

# inputString = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

def nextStep(grid: list[str], currentHeight: int, position: tuple[int]) -> set[tuple[int]]:
    if currentHeight == 9: return {position}
    up = (position[0], position[1] - 1)
    down = (position[0], position[1] + 1)
    left = (position[0] - 1, position[1])
    right = (position[0] + 1, position[1])
    nines = set()
    if 0 <= up[0] < len(grid[0]) and 0 <= up[1] < len(grid) and grid[up[1]][up[0]] == currentHeight + 1:
        nines = nines.union(nextStep(grid, currentHeight + 1, up))
    if 0 <= down[0] < len(grid[0]) and 0 <= down[1] < len(grid) and grid[down[1]][down[0]] == currentHeight + 1:
        nines = nines.union(nextStep(grid, currentHeight + 1, down))
    if 0 <= left[0] < len(grid[0]) and 0 <= left[1] < len(grid) and grid[left[1]][left[0]] == currentHeight + 1:
        nines = nines.union(nextStep(grid, currentHeight + 1, left))
    if 0 <= right[0] < len(grid[0]) and 0 <= right[1] < len(grid) and grid[right[1]][right[0]] == currentHeight + 1:
        nines = nines.union(nextStep(grid, currentHeight + 1, right))
    return nines

def nextStepRating(grid: list[str], currentHeight: int, position: tuple[int]) -> set[tuple[int]]:
    if currentHeight == 9: return 1
    up = (position[0], position[1] - 1)
    down = (position[0], position[1] + 1)
    left = (position[0] - 1, position[1])
    right = (position[0] + 1, position[1])
    nines = 0
    if 0 <= up[0] < len(grid[0]) and 0 <= up[1] < len(grid) and grid[up[1]][up[0]] == currentHeight + 1:
        nines += nextStepRating(grid, currentHeight + 1, up)
    if 0 <= down[0] < len(grid[0]) and 0 <= down[1] < len(grid) and grid[down[1]][down[0]] == currentHeight + 1:
        nines += nextStepRating(grid, currentHeight + 1, down)
    if 0 <= left[0] < len(grid[0]) and 0 <= left[1] < len(grid) and grid[left[1]][left[0]] == currentHeight + 1:
        nines += nextStepRating(grid, currentHeight + 1, left)
    if 0 <= right[0] < len(grid[0]) and 0 <= right[1] < len(grid) and grid[right[1]][right[0]] == currentHeight + 1:
        nines += nextStepRating(grid, currentHeight + 1, right)
    return nines

def partOne(i):
    score = 0
    for y, l in enumerate(i):
        for x, h in enumerate(l):
            if h == 0:
                score += len(nextStep(i, h, (x, y)))
    return score

def partTwo(i):
    rating = 0
    for y, l in enumerate(i):
        for x, h in enumerate(l):
            if h == 0:
                rating += nextStepRating(i, h, (x, y))
    return rating

inputArray = [list(map(int, list(x))) for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
