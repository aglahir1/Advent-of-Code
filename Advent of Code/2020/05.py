
# Started
# Finished

f = open('2020/05.txt', 'r')
inputString = f.read()

def parseSeatnum(seat):
    seatval = 0
    rows = list(range(128))
    cols = list(range(8))
    for b in seat[:7]:
        halfpoint = len(rows) // 2
        if b == 'F': rows = rows[:halfpoint]
        else: rows = rows[halfpoint:]
    row = rows[0]
    for b in seat[7:]:
        halfpoint = len(cols) // 2
        if b == 'L': cols = cols[:halfpoint]
        else: cols = cols[halfpoint:]
    col = cols[0]
    seatval = row  * 8 + col 
    return seatval

def partOne(i):
    highest = 0
    for s in i:
        snum = parseSeatnum(s)
        if snum > highest: highest = snum
    return highest


def partTwo(i):
    seats = []
    for s in i:
        seats.append(parseSeatnum(s))
    for x in range(partOne(i)+1):
        if x not in seats and x - 1 in seats and x + 1 in seats: return x

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
