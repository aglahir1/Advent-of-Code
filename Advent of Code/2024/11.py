
# Started
# Finished

from functools import cache


f = open('2024/11.txt', 'r')
inputString = f.read()

# inputString = "125 17"

@cache
def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    strsto = str(stone)
    if len(strsto) % 2 == 0:
        return [int(strsto[:len(strsto) // 2]), int(strsto[len(strsto) // 2:])]
    return[stone * 2024]

def partOne(i):
    stones = i.copy()
    for idx in range(25):
        newstones = []
        for s in stones:
            newstones += blink(s)
        stones = newstones.copy()
    return len(stones)

def partTwo(i):
    stones = dict()
    for x in i:
        if x in stones:
            stones[x] += 1
        else:
            stones[x] = 1
    for idx in range(75):
        newstones = dict()
        for s in stones:
            n = blink(s)
            for ns in n:
                if ns in newstones:
                    newstones[ns] += stones[s]
                else:
                    newstones[ns] = stones[s]
        stones = newstones
        print(f"{idx + 1} / 75")
    return sum(stones.values())

inputArray = [int(x) for x in inputString.split()]

print(partOne(inputArray))

print(partTwo(inputArray))
