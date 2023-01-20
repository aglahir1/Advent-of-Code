
# Started
# Finished

from typing import Dict, List


f = open('2020/14.txt', 'r')
inputString = f.read()

testString = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

def masked(mask: str, num: int) -> int:
    bitstring: str = str(bin(num))[2:]
    bitstring = '0' * (36 - len(bitstring)) + bitstring
    resultString = ''
    for b, m in zip(bitstring, mask):
        if m == 'X': resultString += b
        else: resultString += m
    return int(resultString, 2)

def maskedv2(mask: str, num: int) -> List:
    bitstring: str = str(bin(num))[2:]
    bitstring = '0' * (36 - len(bitstring)) + bitstring
    resultArray = ['']
    for b, m in zip(bitstring, mask):
        if m == 'X': 
            branched = []
            for prior in resultArray:
                branched.append(prior + '0')
                branched.append(prior + '1')
            resultArray = branched
        elif m == '0':
            for i, prior in enumerate(resultArray):
                resultArray[i] += b
        else: 
            for i, prior in enumerate(resultArray):
                resultArray[i] += '1'
    return resultArray

def partOne(i: List):
    memory: Dict = {}
    mask: str = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for instruction in i:
        instruction = instruction.split(' = ')
        if instruction[0] == 'mask':
            mask = instruction[1]
            continue
        memory[instruction[0][4:-1]] = masked(mask, int(instruction[1]))
    return sum(memory.values())

def partTwo(i):
    memory: Dict = {}
    mask: str = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for instruction in i:
        instruction = instruction.split(' = ')
        if instruction[0] == 'mask':
            mask = instruction[1]
            continue
        memoryAdresses: List = maskedv2(mask, int(instruction[0][4:-1]))
        for adress in memoryAdresses:
            memory[int(adress, 2)] = int(instruction[1])
    return sum(memory.values())

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))