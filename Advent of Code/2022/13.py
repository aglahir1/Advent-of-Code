
# Started
# Finished

from pprint import pprint
from typing import List
import functools

f = open('2022/13.txt', 'r')
inputString = f.read()

#inputString: str = """[1,1,3,1,1]
#[1,1,5,1,1]

#[[1],[2,3,4]]
#[[1],4]

#[9]
#[[8,7,6]]

#[[4,4],4,4]
#[[4,4],4,4,4]

#[7,7,7,7]
#[7,7,7]

#[]
#[3]

#[[[]]]
#[[]]

#[1,[2,[3,[4,[5,6,7]]]],8,9]
#[1,[2,[3,[4,[5,6,0]]]],8,9]"""

class Packet:
    val: List

class Packet:
    def __init__(self, packetString: str):
        self.val = eval(packetString)

    def __lt__(self, otherPacket: Packet):
        for i in zip(self.val, otherPacket.val):
            if type(i[0]) == list or type(i[1]) == list:
                check = Packet(str(makeList(i[0]))) < Packet(str(makeList(i[1])))
                if check == 'same': continue
                return check
            if i[0] == i[1]: continue
            if i[0] < i[1]: return True
            return False
        if len(self.val) == len(otherPacket.val): return 'same'
        if len(self.val) < len(otherPacket.val): return True
        return False


def makeList(i):
    if type(i) == list: return i
    return [i]

def partOne(i):
    correctPairs = []
    for x, pair in enumerate(i):
        if pair[0] < pair[1] : correctPairs.append(x + 1)
    return sum(correctPairs)

def partTwo(i: List[Packet]):
    i.append(Packet('[[2]]'))
    i.append(Packet('[[6]]'))
    i.sort()
    indices = 1
    for x, p in enumerate(i):
        if p.val == [[2]] or p.val == [[6]]: indices *= x + 1
    return indices

inputFirstPart = inputString.split('\n\n')

inputFirstPart = [[Packet(j[0]), Packet(j[1])] for j in [x.splitlines() for x in inputFirstPart]]

print(partOne(inputFirstPart))

inputSecondPart = inputString.replace('\n\n', '\n')

inputSecondPart = [Packet(j) for j in inputSecondPart.splitlines()]

print(partTwo(inputSecondPart))

