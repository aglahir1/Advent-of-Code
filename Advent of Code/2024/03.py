
# Started
# Finished

import re

f = open('2024/03.txt', 'r')
inputString = f.read()

# inputString = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5
# inputString = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()don't()?mul(8,5))"

mulregex = re.compile(r'mul\((\d+),(\d+)\)')
dontregex = re.compile(r"don't\(\).*?do\(\)")
finaldont = re.compile(r"don't\(\).*$")

def partOne(i):
    return sum([int(x[0]) * int(x[1]) for x in re.findall(mulregex, i)])

def partTwo(i):
    i = re.sub(dontregex, '', i)
    i = re.sub(finaldont, '', i)
    return sum([int(x[0]) * int(x[1]) for x in re.findall(mulregex, i)])


print(partOne(inputString))

print(partTwo(inputString))
