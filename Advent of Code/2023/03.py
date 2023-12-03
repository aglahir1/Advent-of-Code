
# Started
# Finished

import re


f = open('2023/03.txt', 'r')
inputString = f.read()

#inputString = """467..114..
#...*......
#..35..633.
#......#...
#617*......
#.....+.58.
#..592.....
#......755.
#...$.*....
#.664.598.."""

def findSurroundingNums(r, c, n):
    numbers = set()
    numbers.add(n[r - 1].get(c, 0))
    numbers.add(n[r - 1].get(c + 1, 0))
    numbers.add(n[r - 1].get(c - 1, 0))
    numbers.add(n[r + 1].get(c, 0))
    numbers.add(n[r + 1].get(c + 1, 0))
    numbers.add(n[r + 1].get(c - 1, 0))
    numbers.add(n[r].get(c + 1, 0))
    numbers.add(n[r].get(c - 1, 0))
    if numbers.__contains__(0): numbers.remove(0)
    return numbers


def partOne(i):
    runningSum = 0
    numbers = []
    for r in range(len(i)):
        nums = re.finditer('\d+', i[r])
        numbers.append({})
        for match in nums:
            for x in range(*match.span()):
                numbers[r][x] = int(match.group())
    for r in range(len(i)):
        specialChars = re.finditer('[^\d.]', i[r])
        for char in specialChars:
            runningSum += sum(findSurroundingNums(r, char.span()[0], numbers))
    return runningSum


def partTwo(i):
    runningSum = 0
    numbers = []
    for r in range(len(i)):
        nums = re.finditer('\d+', i[r])
        numbers.append({})
        for match in nums:
            for x in range(*match.span()):
                numbers[r][x] = int(match.group())
    for r in range(len(i)):
        specialChars = re.finditer('[^\d.]', i[r])
        for char in specialChars:
            if char.group() != '*': continue
            gearSet = list(findSurroundingNums(r, char.span()[0], numbers))
            if len(gearSet) != 2: continue
            runningSum += gearSet[0] * gearSet[1]
    return runningSum

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
