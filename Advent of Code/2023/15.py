
# Started
# Finished

f = open('2023/15.txt', 'r')
inputString = f.read()

#inputString = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def aSHA(i: str):
    currVal = 0
    for c in i:
        currVal += ord(c)
        currVal *= 17
        currVal %= 256
    return currVal

def partOne(i: list[str]):
    count = 0
    for l in i:
        count += aSHA(l)
    return count

def partTwo(i: list[str]):
    boxes: dict[int, dict[str, int]] = {x: {} for x in range(256)}
    for l in i:
        if l.find('-') != -1:
            box = aSHA(l[:-1])
            boxes[box].pop(l[:-1], 0)
            continue
        l = l.split('=')
        box = aSHA(l[0])
        boxes[box][l[0]] = int(l[1])
    power = 0
    for b in boxes:
        for x, l in enumerate(boxes[b]):
            power += (1 + b) * (1 + x) * boxes[b][l]
    return power


inputArray = inputString.split(',')

print(partOne(inputArray))

print(partTwo(inputArray))
