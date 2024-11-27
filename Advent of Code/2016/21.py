
# Started
# Finished

f = open('2016/21.txt', 'r')
inputString = f.read()


def parseInstr(line: str) -> list:
    inst = line.split()
    match(inst[0]):
        case 'reverse':
            result = [5, int(inst[2]), int(inst[4])]
        case 'move':
            result = [6, int(inst[2]), int(inst[5])]
        case 'swap':
            if inst[1] == 'position':
                result = [1, int(inst[2]), int(inst[5])]
            else:
                result = [2, inst[2], inst[5]]
        case 'rotate':
            if inst[1] == 'based':
                result = [4, inst[6]]
            else:
                result = [3, inst[1][0], int(inst[2])]
    return result

def runInstr(l: list, pw: str) -> str:
    match l[0]:
        case 1:
            a = [l[1], l[2]][l[2] < l[1]]
            b = [l[1], l[2]][l[2] > l[1]]
            result = pw[:a] + pw[b] + pw[a + 1:b] + pw[a] + pw[b + 1:]
        case 2:
            a = pw.find(l[1])
            b = pw.find(l[2])
            if b < a:
                c = a
                a = b
                b = c
            result = pw[:a] + pw[b] + pw[a + 1:b] + pw[a] + pw[b + 1:]
        case 3:
            a = l[2]
            if l[1] == 'l':
                result = pw[a:] + pw[:a]
            else:
                result = pw[-a:] + pw[:-a]
        case 4:
            a = pw.find(l[1]) + 1
            if a > 4:
                a += 1
                a %= len(pw)
            result = pw[-a:] + pw[:-a]
        case 5:
            a = [l[1], l[2]][l[2] < l[1]]
            b = [l[1], l[2]][l[2] > l[1]]
            result = pw[0:a] + pw[a:b + 1][::-1] + pw[b + 1:]
        case 6:
            result = list(pw)
            a = result.pop(l[1])
            result.insert(l[2], a)
            result = ''.join(result)
    return result


def revInstr(l: list, pw: str) -> str:
    match l[0]:
        case 1:
            a = [l[1], l[2]][l[2] < l[1]]
            b = [l[1], l[2]][l[2] > l[1]]
            result = pw[:a] + pw[b] + pw[a + 1:b] + pw[a] + pw[b + 1:]
        case 2:
            a = pw.find(l[1])
            b = pw.find(l[2])
            if b < a:
                c = a
                a = b
                b = c
            result = pw[:a] + pw[b] + pw[a + 1:b] + pw[a] + pw[b + 1:]
        case 3:
            a = l[2]
            if l[1] == 'r':
                result = pw[a:] + pw[:a]
            else:
                result = pw[-a:] + pw[:-a]
        case 4:
            assoc = {0: 7, 1: 7, 2: 2, 3: 6, 4: 1, 5: 5, 6: 0, 7: 4}
            a = assoc[pw.find(l[1])]
            result = pw[-a:] + pw[:-a]
        case 5:
            a = [l[1], l[2]][l[2] < l[1]]
            b = [l[1], l[2]][l[2] > l[1]]
            result = pw[0:a] + pw[a:b + 1][::-1] + pw[b + 1:]
        case 6:
            result = list(pw)
            a = result.pop(l[2])
            result.insert(l[1], a)
            result = ''.join(result)
    return result


def partOne(i):
    p1 = 'abcdefgh'
    for l in i:
        p1 = runInstr(l, p1)
    return p1

def partTwo(i):
    p2 = 'fbgdceah'
    for l in i[::-1]:
        p2 = revInstr(l, p2)
    return p2

inputArray = []

for l in inputString.splitlines():
    inputArray.append(parseInstr(l))



print(partOne(inputArray))

print(partTwo(inputArray))
