
# Started
# Finished

f = open('2017/15.txt', 'r')
inputString = f.read()

# inputString = """Generator A starts with 65
# Generator B starts with 8921"""

global amultiplier
global bmultiplier
global divisor
amultiplier = 16807
bmultiplier = 48271
divisor = 2147483647


def partOne(i: list[int]):
    genA = i[0]
    genB = i[1]
    count = 0
    for _ in range(40000000):
        genA *= amultiplier
        genA %= divisor
        genB *= bmultiplier
        genB %= divisor
        if bin(genA)[2:].zfill(16)[-16:] == bin(genB)[2:].zfill(16)[-16:]: count += 1
    return count
    

def partTwo(i: list[int]):
    genA = i[0]
    genB = i[1]
    count = 0
    for _ in range(5000000):
        genA *= amultiplier
        genA %= divisor
        genB *= bmultiplier
        genB %= divisor
        while genA % 4 != 0:
            genA *= amultiplier
            genA %= divisor
        while genB % 8 != 0:
            genB *= bmultiplier
            genB %= divisor
        if bin(genA)[2:].zfill(16)[-16:] == bin(genB)[2:].zfill(16)[-16:]: count += 1
    return count

inputArray = [int(x.split()[-1]) for x in inputString.splitlines()]

# print(partOne(inputArray))

print(partTwo(inputArray))
