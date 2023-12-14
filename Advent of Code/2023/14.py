
# Started
# Finished

f = open('2023/14.txt', 'r')
inputString = f.read()

#inputString = """O....#....
#O.OO#....#
#.....##...
#OO.#O....O
#.O.....O#.
#O.#..O.#.#
#..O..#O..O
#.......O..
##....###..
##OO..#...."""

class Table:
    def __init__(self, g):
        rocks = {}
        blocks = set()
        for y, l in enumerate(g):
            for x, c in enumerate(l):
                match c:
                    case '#':
                        blocks.add((x, y))
                    case 'O':
                        rocks[(x, y)] = (Rock(x, y))
        self.rocks = rocks
        self.blocks = blocks
        self.topLoad = len(g)

    def load(self):
        count = 0
        for r in self.rocks.values():
            count += r.load(self.topLoad)
        return count

    def tipN(self):
        newRocks = {}
        for r in sorted(list(self.rocks), key=lambda x: x[1]):
            if r[1] == 0:
                newRocks[r] = Rock(*r)
                continue
            for x in range(1, r[1] + 1):
                newPos = (r[0], r[1] - x)
                if newPos in self.blocks or newPos in newRocks.keys():
                    newRocks[(r[0], r[1] - x + 1)] = Rock(r[0], r[1] - x + 1)
                    break
                elif newPos[1] == 0:
                    newRocks[newPos] = Rock(*newPos)
        self.rocks = newRocks

    def printTable(self):
        for y in range(self.topLoad):
            l = ''
            for x in range(self.topLoad):
                if (x, y) in self.blocks:
                    l += '#'
                elif (x, y) in self.rocks:
                    l += 'O'
                else:
                    l += '.'
            print(l)

class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def load(self, topLoad):
        return topLoad - self.y

def partOne(i):
    table = Table(i)
    table.printTable()
    print()
    table.tipN()
    table.printTable()
    return table.load()


def partTwo(i):
    pass

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
