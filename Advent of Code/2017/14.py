
# Started
# Finished

from functools import reduce


f = open('2017/14.txt', 'r')
inputString = f.read()

# inputString = 'flqrgnkx'

def knot(nums, lengths, skipsize, pos):
    for command in lengths:
        sublist = []
        for i in range(command):
            sublist.append(nums[(pos + i) % len(nums)])
        for x, n in enumerate(sublist[::-1]):
            nums[(pos + x) % len(nums)] = n
        pos += command + skipsize
        skipsize += 1
    return [nums, skipsize, pos]

def knothash(i):
    hashlength = 256
    nums = list(range(hashlength))
    skipsize = 0
    pos = 0
    insts = []
    for c in i:
        insts.append(ord(c))
    insts += [int(x) for x in '17 31 73 47 23'.split()]
    for _ in range(64):
        nums, skipsize, pos = knot(nums, insts, skipsize, pos)
    xored = []
    for a in range(16):
        xored.append(reduce(lambda x, y: x ^ y, nums[0 + a*16: 16 + a*16]))
    return ''.join([x.to_bytes(1, "big").hex() for x in xored])

def arrayprint(a):
    for l in a:
        print(''.join(l))
        
def groupExplore(x, y, grid: list[list[str]], groupSoFar: list[str]):
    if x != 127 and f'{x + 1},{y}' not in groupSoFar and grid[y][x + 1] == '1':
        groupSoFar.append(f'{x + 1},{y}')
        groupSoFar = groupExplore(x + 1, y, grid, groupSoFar)
    if x != 0 and f'{x - 1},{y}' not in groupSoFar and grid[y][x - 1] == '1':
        groupSoFar.append(f'{x - 1},{y}')
        groupSoFar = groupExplore(x - 1, y, grid, groupSoFar)
    if y != 127 and f'{x},{y + 1}' not in groupSoFar and grid[y + 1][x] == '1':
        groupSoFar.append(f'{x},{y + 1}')
        groupSoFar = groupExplore(x, y + 1, grid, groupSoFar)
    if y != 0 and f'{x},{y - 1}' not in groupSoFar and grid[y - 1][x] == '1':
        groupSoFar.append(f'{x},{y - 1}')
        groupSoFar = groupExplore(x, y - 1, grid, groupSoFar)
    return groupSoFar
        
def countgroups(a):
    groups = []
    for y, l in enumerate(a):
        for x, f in enumerate(l):
            if f == '1':
                if any([f'{x},{y}' in g for g in groups]):
                    continue
                groups.append(groupExplore(x, y, a, [f'{x},{y}']))
    return len(groups)

def partOne(i):
    grid = []
    count = 0
    for r in range(128):
        string = i + '-' + str(r)
        kh = knothash(string)
        grid.append(list(bin(int(kh, 16))[2:].zfill(128)))
    print(sum([x.count('1') for x in grid]))
    return countgroups(grid)

print(partOne(inputString))
