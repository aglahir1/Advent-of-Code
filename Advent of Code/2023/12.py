
# Started
# Finished

f = open('2023/12.txt', 'r')
inputString = f.read()

#inputString = """???.### 1,1,3
#.??..??...?##. 1,1,3
#?#?#?#?#?#?#?#? 1,3,1,6
#????.#...#... 4,1,1
#????.######..#####. 1,6,5
#?###???????? 3,2,1"""

def generateSolutions(solutions: set[str], morphable: str, score: list[int]):
    if morphable.find('?') != -1:
        if isSuitable(morphable.replace('?', '.', 1), score):
            solutions = solutions.union(generateSolutions(solutions, morphable.replace('?', '.', 1)))
        if isSuitable(morphable.replace('?', '#', 1), score):
            solutions = solutions.union(generateSolutions(solutions, morphable.replace('?', '#', 1)))
    else:
        solutions.add(morphable)
    return solutions

def isSuitable(springs, score):
    pass

def generateScore(springs: str) -> list[int]:
    curr = 0
    result = []
    for c in springs:
        if c == '#':
            curr += 1
        if c == '.':
            result.append(curr)
            curr = 0
    while 0 in result:
        result.remove(0)
    return result


def partOne(i):
    count = 0
    for j, l in enumerate(i):
        possibles = generateSolutions(set(), l[0], l[1])
        count += len(possibles)
        print(f'{j+1}/{len(i)}')
    return count

def partTwo(i):
    pass

inputArray = [[x.split()[0], [int(i) for i in x.split()[1].split(',')]] for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
