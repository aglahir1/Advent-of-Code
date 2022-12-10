
# Started
# Finished

f = open('2022/10.txt', 'r')
inputString = f.read()

#inputString = """addx 15
#addx -11
#addx 6
#addx -3
#addx 5
#addx -1
#addx -8
#addx 13
#addx 4
#noop
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx -35
#addx 1
#addx 24
#addx -19
#addx 1
#addx 16
#addx -11
#noop
#noop
#addx 21
#addx -15
#noop
#noop
#addx -3
#addx 9
#addx 1
#addx -3
#addx 8
#addx 1
#addx 5
#noop
#noop
#noop
#noop
#noop
#addx -36
#noop
#addx 1
#addx 7
#noop
#noop
#noop
#addx 2
#addx 6
#noop
#noop
#noop
#noop
#noop
#addx 1
#noop
#noop
#addx 7
#addx 1
#noop
#addx -13
#addx 13
#addx 7
#noop
#addx 1
#addx -33
#noop
#noop
#noop
#addx 2
#noop
#noop
#noop
#addx 8
#noop
#addx -1
#addx 2
#addx 1
#noop
#addx 17
#addx -9
#addx 1
#addx 1
#addx -3
#addx 11
#noop
#noop
#addx 1
#noop
#addx 1
#noop
#noop
#addx -13
#addx -19
#addx 1
#addx 3
#addx 26
#addx -30
#addx 12
#addx -1
#addx 3
#addx 1
#noop
#noop
#noop
#addx -9
#addx 18
#addx 1
#addx 2
#noop
#noop
#addx 9
#noop
#noop
#noop
#addx -1
#addx 2
#addx -37
#addx 1
#addx 3
#noop
#addx 15
#addx -21
#addx 22
#addx -6
#addx 1
#noop
#addx 2
#addx 1
#noop
#addx -10
#noop
#noop
#addx 20
#addx 1
#addx 2
#addx 2
#addx -6
#addx -11
#noop
#noop
#noop"""

def checkClock(sigStrengths: list, clock: int, x: int):
    if (clock + 20) % 40 == 0: 
        sigStrengths.append(clock * x)
    return sigStrengths

def run(i: list):
    clock: int
    x: int
    position: int
    sigStrengths: list
    clock = 0
    x = 1
    position = 0
    sigStrengths = []
    while True:
        if position == len(i): break
        if i[position][0] == 'n':
            print(('.', '#')[abs((clock % 40) - x) < 2], end=('', '\n')[(clock+1) % 40 == 0])
            clock += 1
            sigStrengths = checkClock(sigStrengths, clock, x)
            position += 1
            continue
        
        print(('.', '#')[abs((clock % 40)  - x) < 2], end=('', '\n')[(clock+1) % 40 == 0])
        clock += 1
        sigStrengths = checkClock(sigStrengths, clock, x)
        print(('.', '#')[abs((clock % 40)  - x) < 2], end=('', '\n')[(clock+1) % 40 == 0])
        clock += 1
        sigStrengths = checkClock(sigStrengths, clock, x)
        x += int(i[position].split()[1])
        position += 1
    return sum(sigStrengths)

inputArray = inputString.splitlines()

print(run(inputArray))
