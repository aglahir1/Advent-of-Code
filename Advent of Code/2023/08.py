
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

# inputString = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

class Node:
    def __init__(self, name: str):
        self.name = name

    def directions(self, left: 'Node', right: 'Node'):
        self.left = left
        self.right = right
        
def primefactorise(n: int) -> dict[int: int]:
    i = 2
    factors: dict[int:int] = {}
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        else:
            i += 1
        if n == 1:
            break
    if n > 0: factors[n] = factors.get(n, 0) + 1
    return factors
    
            

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
    pointers = []
    for k in nodes.keys():
        if k[2] == 'A':
            pointers.append(nodes[k])
    histories: list[int] = []
    for p in pointers:
        count = 0
        found = False
        while not found:
            for c in i:
                count += 1
                if c == 'R': p = p.right
                elif c == 'L': p = p.left
                if p.name[2] == 'Z':
                    found = True
                    break
        histories.append(count)
    primes = {}
    for h in histories:
        smallPPrimes = primefactorise(h)
        for k in smallPPrimes:
            if primes.get(k, 0) < smallPPrimes[k]:
                primes[k] = smallPPrimes[k]
    result = 1
    for n in primes:
        result *= (n ** primes[n])
    return result
        
            
inputArray = inputString.split('\n\n')

nodes = {x.split()[0]: Node(x.split()[0]) for x in inputArray[1].splitlines()}

for n in inputArray[1].splitlines():
    result = re.search(r'\((.{3}), (.{3})\)', n)
    nodes[n.split()[0]].directions(nodes[result.group(1)], nodes[result.group(2)])


print(partOne(inputArray[0]))

print(partTwo(inputArray[0]))
