
# Started
# Finished

from functools import cache


f = open('2023/12.txt', 'r')
inputString = f.read()

# inputString = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""


def generateSolutions(solutions: set[str], morphable: str, score: list[int]):
    if morphable.find('?') != -1:
        solutions = solutions.union(generateSolutions(solutions, morphable.replace('?', '.', 1), score))
        if isSuitable(morphable, score):
            solutions = solutions.union(generateSolutions(solutions, morphable.replace('?', '#', 1), score))
    else:
        if generateScore(morphable) == score:
            solutions.add(morphable)
    return solutions

def isSuitable(springs, score):
    i = springs.find('?')
    springs = springs[:i] + '#'
    pointer = 0
    curr = 0
    result = []
    for c in springs:
        if c == '#':
            curr += 1
        if c == '.':
            if pointer >= len(score) or curr > score[pointer]:
                return False
            else:
                if curr > 0:
                    pointer += 1
                    curr = 0
    return True

def generateScore(springs: str) -> list[int]:
    curr = 0
    result = []
    for c in springs:
        if c == '#':
            curr += 1
        if c == '.' and curr > 0:
            result.append(curr)
            curr = 0
    if curr > 0: result.append(curr)
    return result

@cache
def walkSprings(springs: str, score: tuple[int], currSpring: int, currScore: int, currScoreIndex: int) -> int:
    if currSpring == len(springs):
        if (currScoreIndex == len(score) - 1 and currScore == score[-1]) or (currScoreIndex == len(score) and currScore == 0):
            return 1
        else:
            return 0
    if currScoreIndex == len(score):
        if springs[currSpring:].find('#') != -1:
            return 0
        else:
            return 1
    if springs[currSpring] == '.':
        if currScore > 0:
            if currScore == score[currScoreIndex]:
                return walkSprings(springs, score, currSpring + 1, 0, currScoreIndex + 1)
            else:
                return 0
        else:
            return walkSprings(springs, score, currSpring + 1, 0, currScoreIndex)
    if springs[currSpring] == '#':
        return walkSprings(springs, score, currSpring + 1, currScore + 1, currScoreIndex)
    possibles = 0
    if currScore > 0 and currScore == score[currScoreIndex]:
        possibles += walkSprings(springs, score, currSpring + 1, 0, currScoreIndex + 1)
    if currScore == 0:
        possibles += walkSprings(springs, score, currSpring + 1, 0, currScoreIndex)
    possibles += walkSprings(springs, score, currSpring + 1, currScore + 1, currScoreIndex)
    return possibles
        


def partOne(i):
    count = 0
    for j, l in enumerate(i):
        amount = walkSprings(l[0], l[1], 0, 0, 0)
        count += amount
        print(f'{j+1:0{len(str(len(i)))}}/{len(i)}: {amount}')
    return count

def partTwo(i):
    pass

inputArray = [[((x.split()[0]+'?')*5)[:-1], tuple(int(i) for i in x.split()[1].split(','))*5] for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
