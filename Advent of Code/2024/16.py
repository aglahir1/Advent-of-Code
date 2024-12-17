
# Started
# Finished

f = open('2024/16.txt', 'r')
inputString = f.read()

inputString = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

inputString = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

inputArray = inputString.splitlines()

MAX = 99999999999999999999999999
gridH = len(inputArray)
gridW = len(inputArray[0])
deltas = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
dirloop = {'E': 'SN', 'S': 'WE', 'W': 'NS', 'N': 'EW'}

field = dict()

for y in range(gridH):
    for x in range(gridW):
        c = inputArray[y][x]
        if c == '#':
            continue
        if c == 'E':
            goalPos = (y,x)
        if c == 'S':
            startPos = (y,x)
            field[(y,x)] = {'p': 0, 'd': 'E'}
        else:
            field[(y,x)] = {'p': MAX, 'd': ''}

def partOne(i):
    paths = {startPos}
    while len(paths) > 0:
        newPaths = set()
        for p in paths:
            points = i[p]['p']
            d = i[p]['d']
            dp = (p[0] + deltas[d][0], p[1] + deltas[d][1])
            if dp in i:
                if points + 1 < i[dp]['p'] or (points + 1 == i[dp]['p'] and d != i[dp]['d']):
                    i[dp]['p'] = points + 1
                    i[dp]['d'] = d
                    newPaths.add((dp[0], dp[1] ))
            for t in dirloop[d]:
                tp = (p[0] + deltas[t][0], p[1] + deltas[t][1])
                if tp in i:
                    if points + 1001 < i[tp]['p'] or (points + 1001 == i[tp]['p'] and t != i[tp]['d']):
                        i[tp]['p'] = points + 1001
                        i[tp]['d'] = t
                        newPaths.add((tp[0], tp[1]))
        paths = newPaths.copy()
    return i[goalPos]
        
def partTwo(i):
    visited = {startPos, goalPos}
    paths = {goalPos}
    while len(paths) > 0:
        newPaths = set()
        for p in paths:
            points = i[p]['p']
            for d in deltas.values():
                np = (p[0] + d[0], p[1] + d[1])
                if np in visited: continue
                if np in i:
                    if i[np]['p'] in (points - 1, points - 1001):
                        newPaths.add(np)
                        visited.add(np)
        paths = newPaths.copy()
    return len(visited)

print(partOne(field))

print(partTwo(field))
