
# Started
# Finished

from functools import cache


inputString = '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^'
# inputString = '.^^.^.^^^^'
# inputString = '..^^.'

@cache
def generateNextRow(i: str) -> str:
    newRow = '.'
    for x in zip(i[:-2], i[2:]):
        if x in {('.', '^'), ('^', '.')}:
            newRow += '^'
        else:
            newRow += '.'
    return newRow + '.'

def partOne(i):
    # prime row
    i = '.' + i + '.'
    result = i[1:-1] + '\n'
    for _ in range(39):
        i = generateNextRow(i)
        result += i[1:-1] + '\n'
    return result.count('.')

def partTwo(i):
    # prime row
    i = '.' + i + '.'
    result = i[1:-1] + '\n'
    for _ in range(399999):
        i = generateNextRow(i)
        result += i[1:-1] + '\n'
    return result.count('.')


print(partOne(inputString))

print(partTwo(inputString))
