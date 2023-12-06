
# Started
# Finished

from functools import reduce


f = open('2017/10.txt', 'r')
inputString = f.read()

#inputString = "3, 4, 1, 5"

def knot(nums, lengths, skipsize, firstinlist):
    for command in lengths:
        if command > 0:
            nums = nums[command:] + nums[command - 1::-1]
        nums = nums[skipsize:] + nums[0:skipsize]
        firstinlist -= (command + skipsize)
        skipsize += 1
    return [nums, skipsize, firstinlist]

def knot2(nums, lengths, skipsize, pos):
    for command in lengths:
        sublist = []
        for i in range(command):
            sublist.append(nums[(pos + i) % len(nums)])
        for x, n in enumerate(sublist[::-1]):
            nums[(pos + x) % len(nums)] = n
        pos += command + skipsize
        skipsize += 1
    return [nums, skipsize, pos]

def partOne(i):
    hashlength = 256
    nums = list(range(hashlength))
    skipsize = 0
    pos = 0
    nums, skipsize, pos = knot2(nums, [int(x) for x in i.split(',')], skipsize, pos)
    return nums[0] * nums[1]


def partTwo(i):
    hashlength = 256
    nums = list(range(hashlength))
    skipsize = 0
    pos = 0
    insts = []
    for c in i:
        insts.append(ord(c))
    insts += [int(x) for x in '17 31 73 47 23'.split()]
    for _ in range(64):
        nums, skipsize, pos = knot2(nums, insts, skipsize, pos)
    xored = []
    for a in range(16):
        xored.append(reduce(lambda x, y: x ^ y, nums[0 + a*16: 16 + a*16]))
    print(xored)
    return ''.join([x.to_bytes(1, "big").hex() for x in xored])

print(partOne(inputString))

print(partTwo(inputString))
