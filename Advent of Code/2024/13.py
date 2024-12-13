
# Started
# Finished

import re


f = open('2024/13.txt', 'r')
inputString = f.read()

# inputString = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

inputArray = inputString.split("\n\n")

regbutton = re.compile(r'Button [AB]: X\+(\d+), Y\+(\d+)')
regprize = re.compile(r'Prize: X=(\d+), Y=(\d+)')

machines = []
for machine in inputArray:
    machine = machine.splitlines()
    buttona = regbutton.match(machine[0])
    buttonb = regbutton.match(machine[1])
    prize = regprize.match(machine[2])
    machines.append({'a': (int(buttona.group(1)), int(buttona.group(2))), 'b': (int(buttonb.group(1)), int(buttonb.group(2))), 'prize': (int(prize.group(1)), int(prize.group(2)))})


def partOne():
    # runningsum = 0
    # for m in machines:
    #     xa = m['a'][0]
    #     ya = m['a'][1]
    #     xb = m['b'][0]
    #     yb = m['b'][1]
    #     x = m['prize'][0]
    #     y = m['prize'][1]
    #     if yb * xa - xb == 0:
    #         runningsum += 1
    # return runningsum
    # there are no parallel lines
    runningsum = 0
    for m in machines:
        xa = m['a'][0]
        ya = m['a'][1]
        xb = m['b'][0]
        yb = m['b'][1]
        x = m['prize'][0]
        y = m['prize'][1]
        if (y * xa - x * ya) % (yb * xa - xb * ya) != 0: continue
        b = (y * xa - x * ya) / (yb * xa - xb * ya)
        if (x - b * xb) % xa != 0: continue
        a = (x - b * xb) / xa
        runningsum += (3 * a) + b
    return int(runningsum)
        

def partTwo():
    runningsum = 0
    for m in machines:
        xa = m['a'][0]
        ya = m['a'][1]
        xb = m['b'][0]
        yb = m['b'][1]
        x = m['prize'][0] + 10000000000000
        y = m['prize'][1] + 10000000000000
        if (y * xa - x * ya) % (yb * xa - xb * ya) != 0: continue
        b = (y * xa - x * ya) / (yb * xa - xb * ya)
        if (x - b * xb) % xa != 0: continue
        a = (x - b * xb) / xa
        runningsum += (3 * a) + b
    return int(runningsum)

print(partOne())

print(partTwo())
