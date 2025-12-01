
# Started
# Finished

f = open('2026/01.txt', 'r')
inputString = f.read()

# inputString = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

def partOne(i):
    pos = 50
    count = 0
    for instruction in i:
        if instruction[0] == 'L':
            m = -1
        else:
            m = 1
        pos += m * int(instruction[1:])
        if pos % 100 == 0: count += 1
    return count

def partTwo(i):
    pos = 50
    count = 0
    for instruction in i:
        if instruction[0] == 'L':
            m = -1
            if pos == 0: pos = 100
        else:
            m = 1
        pos += m * int(instruction[1:])
        if 0 < pos < 100:
            continue
        if pos < 1:
            count += -(pos - 100) // 100
        elif pos > 99:
            count += pos // 100
        pos %= 100
    return count


inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
