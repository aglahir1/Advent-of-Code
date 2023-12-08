
# Started
# Finished

import re

f = open('2023/08.txt', 'r')
inputString = f.read()

#inputString = """RL

#AAA = (BBB, CCC)
#BBB = (DDD, EEE)
#CCC = (ZZZ, GGG)
#DDD = (DDD, DDD)
#EEE = (EEE, EEE)
#GGG = (GGG, GGG)
#ZZZ = (ZZZ, ZZZ)"""

class Node:
    def __init__(self, name: str):
        self.name = name

    def directions(self, left: 'Node', right: 'Node'):
        self.left = left
        self.right = right

def partOne(i):
    pointer = nodes['AAA']
    count = 0
    while True:
        for c in i:
            count += 1
            if c == 'R':
                pointer = pointer.right
            elif c == 'L':
                pointer = pointer.left
            if pointer.name == 'ZZZ':
                return count

def partTwo(i):
    pass

inputArray = inputString.split('\n\n')


nodes = {x.split()[0]: Node(x.split()[0]) for x in inputArray[1].splitlines()}

for n in inputArray[1].splitlines():
    result = re.search(r'\((.{3}), (.{3})\)', n)
    nodes[n.split()[0]].directions(nodes[result.group(1)], nodes[result.group(2)])


print(partOne(inputArray[0]))

print(partTwo(inputArray[0]))
