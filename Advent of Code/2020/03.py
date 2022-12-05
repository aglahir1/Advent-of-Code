
# Started
# Finished


from math import prod


f = open('2020/03.txt', 'r')
inputString = f.read()

#inputString = """..##.......
##...#...#..
#.#....#..#.
#..#.#...#.#
#.#...##..#.
#..#.##.....
#.#.#.#....#
#.#........#
##.##...#...
##...##....#
#.#..#...#.#"""

def partOne(i, slope):
    y = len(i)
    x = len(i[0])
    pos = {'x': 0, 'y': 0}
    trees = 0
    while pos['y'] < y:
        if i[pos['y']][pos['x']] == '#': trees += 1
        pos['x'] += slope['x']
        pos['y'] += slope['y']
        if pos['x'] >= x: pos['x'] -= x
    return trees


def partTwo(i):
    slopes = [{'x': 1, 'y': 1}, {'x': 3, 'y': 1}, {'x': 5, 'y': 1}, {'x': 7, 'y': 1}, {'x': 1, 'y': 2}]
    trees = []
    for m in slopes:
        trees.append(partOne(i, m))
    return prod(trees)

inputArray = inputString.splitlines()

print(partOne(inputArray, {'x': 3, 'y': 1}))

print(partTwo(inputArray))
