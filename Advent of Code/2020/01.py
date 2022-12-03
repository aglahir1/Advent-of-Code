
# Started
# Finished

f = open('2020/01.txt', 'r')
inputString = f.read()

#inputString = """1721
#979
#366
#299
#675
#1456"""

def partOne(i):
    s = i[1:]
    for x in i:
        for y in s:
            if x + y == 2020:
                return x * y
        s = s[1:]


def partTwo(i):
    s = i[1:]
    for x in i:
        t = s[1:]
        for y in s:
            for z in t:
                if x + y + z == 2020:
                    return x * y * z
            t = t[1:]
        s = s[1:]

inputArray = [int(x) for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
