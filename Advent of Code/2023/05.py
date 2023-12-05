
# Started
# Finished

from copy import deepcopy
import copy


f = open('2023/05.txt', 'r')
inputString = f.read()

#inputString = """seeds: 79 14 55 13

#seed-to-soil map:
#50 98 2
#52 50 48

#soil-to-fertilizer map:
#0 15 37
#37 52 2
#39 0 15

#fertilizer-to-water map:
#49 53 8
#0 11 42
#42 0 7
#57 7 4

#water-to-light map:
#88 18 7
#18 25 70

#light-to-temperature map:
#45 77 23
#81 45 19
#68 64 13

#temperature-to-humidity map:
#0 69 1
#1 0 69

#humidity-to-location map:
#60 56 37
#56 93 4"""

def partOne(i):
    seeds = [int(x) for x in i[0][0].split(': ')[1].split()]
    for block in i[1:]:
        for x, seed in enumerate(seeds):
            for alloc in block[1:]:
                dest = int(alloc.split()[0])
                src = int(alloc.split()[1])
                offset = int(alloc.split()[2])
                if src <= seed <= src + offset:
                    seeds[x] = dest + seed - src
                    break
    return min(seeds)

def findAndApplyIntersections(untransformed, alloc):
    transformed = []
    remainder = []
    for seedrange in untransformed:
        diff = alloc['dest'][0] - alloc['src'][0]
        if seedrange[1] < alloc['src'][0] or seedrange[0] > alloc['src'][1]: 
            remainder.append(deepcopy(seedrange))
            continue
        if seedrange[0] <= alloc['src'][0] and seedrange[1] >= alloc['src'][1]:
            if seedrange[0] < alloc['src'][0]:
                remainder.append([seedrange[0], alloc['src'][0] - 1])
            if seedrange[1] > alloc['src'][1]:
                remainder.append([alloc['src'][1] + 1, seedrange[1]])
            transformed.append(alloc['dest'])
            continue
        if seedrange[0] >= alloc['src'][0] and seedrange[1] <= alloc['src'][1]:
            transformed.append([seedrange[0] + diff, seedrange[1] + diff])
            continue
        if seedrange[0] <= alloc['src'][0]:
            if seedrange[0] < alloc['src'][0]:
                remainder.append([seedrange[0], alloc['src'][0] - 1])
            transformed.append([alloc['dest'][0], seedrange[1] + diff])
            continue
        transformed.append([seedrange[0] + diff, alloc['dest'][1]])
        if seedrange[1] > alloc['src'][1]:
            remainder.append([alloc['src'][1] + 1, seedrange[1]])
    return [transformed,remainder]

def cleanup(a):
    a = sorted(a, key=lambda x: x[0])
    out = [a[0]]
    for r in a[1:]:
        if r[0] == out[-1][1] + 1:
            out[-1][1] = r[1]
        else:
            out.append(r)
    return out

def partTwo(i):
    seeds = list(map(int, i[0][0].split(': ')[1].split()))
    seeds = [[x[0], x[1] + x[0] - 1] for x in zip(seeds[::2], seeds[1::2])]
    for block in i[1:]:
        untransformed = deepcopy(seeds)
        transformed = []
        for alloc in block[1:]:
            dest = int(alloc.split()[0])
            src = int(alloc.split()[1])
            offset = int(alloc.split()[2])
            parsedAlloc = {
                'src': [src, src + offset - 1],
                'dest': [dest, dest + offset - 1]
                }
            result = findAndApplyIntersections(untransformed, parsedAlloc)
            if len(result[0]) > 0:
                transformed += result[0]
                untransformed = result[1]
        seeds = deepcopy(untransformed) + deepcopy(transformed)
        seeds = cleanup(seeds)
    return seeds[0][0]


inputArray = [x.splitlines() for x in inputString.split('\n\n')]

print(partOne(inputArray))

print(partTwo(inputArray))
