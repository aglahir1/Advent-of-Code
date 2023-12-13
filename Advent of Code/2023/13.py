
# Started
# Finished

f = open('2023/13.txt', 'r')
inputString = f.read()

#inputString = """#.##..##.
#..#.##.#.
###......#
###......#
#..#.##.#.
#..##..##.
##.#.##.#.

##...##..#
##....#..#
#..##..###
######.##.
######.##.
#..##..###
##....#..#"""

def findVerticalReflection(g: list[str]):
    for x in range(len(g) - 1):
        notDisproven = True
        for d in range(min(len(g) - 1 - x, x + 1)):
            if g[x - d] != g[x + 1 + d]:
                notDisproven = False
                break
        if notDisproven:
            return x
    return -1

def countDifferences(a: str, b: str) -> bool:
    count = 0
    for ca, cb in zip(a, b):
        if ca != cb: count += 1
    return count

def findVerticalReflectionWhileFixing(g: list[str]):
    for x in range(len(g) - 1):
        noFixesYet = True
        notDisproven = True
        for d in range(min(len(g) - 1 - x, x + 1)):
            if g[x - d] != g[x + 1 + d]:
                if noFixesYet and (countDifferences(g[x - d], g[x + 1 + d]) == 1):
                    noFixesYet = False
                else:
                    notDisproven = False
                    break
        if notDisproven and not noFixesYet:
            return x
    return -1

def partOne(i):
    count = 0
    for g in i:
        res = findVerticalReflection(g) + 1
        if res == 0:
            res = findVerticalReflection([''.join(x) for x in zip(*g)]) + 1
        else:
            res *= 100
        count += res
    return count

def partTwo(i):
    count = 0
    for g in i:
        res = findVerticalReflectionWhileFixing(g) + 1
        if res == 0:
            res = findVerticalReflectionWhileFixing([''.join(x) for x in zip(*g)]) + 1
            print()
        else:
            res *= 100
        count += res
    return count

inputArray = [x.splitlines() for x in inputString.split('\n\n')]

print(partOne(inputArray))

print(partTwo(inputArray))
