
# Started 02:16
# Finished 02:31

f = open('2016/02.txt', 'r')
inputString = f.read()

#inputString = """ULL
#RRDDD
#LURDL
#UUUUD"""

def partOne(i):
    pos = 5
    code = []
    for entry in i:
        for x in entry:
            if x == 'U':
                if pos < 4:
                    continue
                pos -= 3
            if x == 'D':
                if pos > 6:
                    continue
                pos += 3
            if x == 'L':
                if pos in (1, 4, 7):
                    continue
                pos -= 1
            if x == 'R':
                if pos in (3, 6, 9):
                    continue
                pos += 1
        code.append(pos)
    return code

def partTwo(i):
    y = 2
    x = 0
    keypad = [['', '', 1, '', ''], ['', 2, 3, 4, ''], [5, 6, 7, 8, 9], ['', 'A', 'B', 'C', ''], ['', '', 'D', '', '']]
    code = []
    for entry in i:
        for c in entry:
            if c == 'U':
                if y:
                    if keypad[y - 1][x]:
                        y -= 1
            if c == 'D':
                if y < 4:
                    if keypad[y + 1][x]:
                        y += 1
            if c == 'L':
                if x:
                    if keypad[y][x - 1]:
                        x -= 1
            if c == 'R':
                if x < 4:
                    if keypad[y][x + 1]:
                        x += 1
        code.append(keypad[y][x])
    return code

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))