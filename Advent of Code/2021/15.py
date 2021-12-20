
# Started
# Finished

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

def partOne(i):
    pass

def partTwo(i):
    pass

inputArray = inputString.splitlines()

grid = [[int(j) for j in x] for x in inputArray]

for g in grid:
    for c in g:
        print(f"{c} ", end = "")
    print()

csv = open('')

print(partOne(grid))

print(partTwo(grid))
