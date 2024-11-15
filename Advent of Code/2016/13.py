
# Started
# Finished


from copy import deepcopy


favouritenumber = 1352
endGoal = (31, 39)

# favouritenumber = 10
# endGoal = (7, 4)

def manhattanDistance(pointOne: tuple[int, int], pointTwo: tuple[int, int]) -> int:
    return abs(pointOne[0] - pointTwo[0]) + abs(pointOne[1] - pointTwo[1])

def checkForWall(position: tuple[int, int]) -> bool:
    (x, y) = position
    calculation = x * x + 3 * x + 2 * x * y + y + y * y + favouritenumber
    return bool(bin(calculation).count('1') % 2)

def takeStep(path: list[tuple[int, int]], goal: tuple[int, int], checked: dict[str, int], walls: set[tuple[int, int]]) -> tuple[list[tuple[tuple[int,int],tuple[int,int]]],dict[str,int],set[tuple[int,int]]]:
    currentPosition = path[-1]
    if manhattanDistance(currentPosition, goal) == 1:
        return 'GOAL FOUND'
    newPaths = []
    left = (currentPosition[0] - 1, currentPosition[1])
    right = (currentPosition[0] + 1, currentPosition[1])
    up = (currentPosition[0], currentPosition[1] + 1)
    down = (currentPosition[0], currentPosition[1] - 1)
    if currentPosition[0] != 0:
        if ','.join([str(x) for x in left]) not in checked.keys():
            checked[','.join([str(x) for x in left])] = len(path)
            if checkForWall(left):
                walls.add(left)
        if checked[','.join([str(x) for x in left])] >= len(path): 
            checked[','.join([str(x) for x in left])] = len(path)
            newPaths.append(path + [left])
    if currentPosition[1] != 0:
        if ','.join([str(x) for x in down]) not in checked.keys():
            checked[','.join([str(x) for x in down])] = len(path)
            if checkForWall(down):
                walls.add(down)
        if checked[','.join([str(x) for x in down])] >= len(path): 
            checked[','.join([str(x) for x in down])] = len(path)
            newPaths.append(path + [down])
    if ','.join([str(x) for x in right]) not in checked.keys():
        checked[','.join([str(x) for x in right])] = len(path)
        if checkForWall(right):
            walls.add(right)
    if checked[','.join([str(x) for x in right])] >= len(path): 
        checked[','.join([str(x) for x in right])] = len(path)
        newPaths.append(path + [right])
    if ','.join([str(x) for x in up]) not in checked.keys():
        checked[','.join([str(x) for x in up])] = len(path)
        if checkForWall(up):
            walls.add(up)
    if checked[','.join([str(x) for x in up])] >= len(path): 
        checked[','.join([str(x) for x in up])] = len(path)
        newPaths.append(path + [up])
            
    return (newPaths, checked, walls)


def mazeFind(goal: tuple[int, int]) -> int:
    visited = [{(1,1)}]
    walls = set()
    while True:
        newVisits = set()
        for c in visited[-1]:
            left = (c[0] - 1, c[1])
            right = (c[0] + 1, c[1])
            up = (c[0], c[1] + 1)
            down = (c[0], c[1] - 1)
            if c[0] != 0:
                if not (any([left in x for x in visited]) or left in walls or left in newVisits):
                    if checkForWall(left): walls.add(left)
                    else: newVisits.add(left)
            if c[1] != 0:
                if not (any([down in x for x in visited]) or down in walls or down in newVisits):
                    if checkForWall(down): walls.add(down)
                    else: newVisits.add(down)
            if not (any([right in x for x in visited]) or right in walls or right in newVisits):
                if checkForWall(right): walls.add(right)
                else: newVisits.add(right)
            if not (any([up in x for x in visited]) or up in walls or up in newVisits):
                if checkForWall(up): walls.add(up)
                else: newVisits.add(up)
        visited.append(deepcopy(newVisits))
        if goal in visited[-1]:
            return visited
    # paths = [[(1,1)]]
    # checked = {'1,1': 1}
    # walls = set()
    # while True:
    #     newPaths = []
    #     for p in paths:
    #         result = takeStep(p, goal, checked, walls)
    #         if result == 'GOAL FOUND':
    #             return len(p) + 2
    #         for x in result[0]:
    #             if x not in newPaths:
    #                 newPaths.append(x)
    #         checked = result[1]
    #         walls = result [2]
    #     paths = deepcopy(newPaths)
    #     if len(paths) % 10 == 0: print('path length:', len(paths[0]), '\npaths:', len(paths))

answer = mazeFind(endGoal)

def partOne():
    return len(answer) - 1

def partTwo():
    return sum([len(x) for x in answer[0:51]])


print(partOne())

print(partTwo())