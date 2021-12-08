
# Started 05:21
# Finished 06:32

import math

f = open('2015/24.txt', 'r')
inputString = f.read()

#inputString = """1
#2
#3
#4
#5
#7
#8
#9
#10
#11"""

divisor = 4

def remainingPackagesTurnaround(group, remainingPackages, target, minim):
    answer = []
    for i in range(len(remainingPackages)):
        if answer:
            minim = min([len(x) for x in answer])
        check = group[:]
        extra = remainingPackages[i+1:]
        check.append(remainingPackages[i])
        if sum(check) == target:
            answer.append(check)
        elif sum(check) > target or len(check) > minim:
            continue
        else:
            answer += remainingPackagesTurnaround(check, extra, target, minim)
    return answer

inputArray = inputString.splitlines()

packages = []

for entry in inputArray:
    packages.append(int(entry))

packages.sort(reverse=True)

target = int(sum(packages) / divisor)

group1s = []
currentMin = len(packages) / divisor

for i in range(int(len(packages) / 2)):
    remainingPackages = packages[i+1:] + packages[:i]
    group = [packages[i]]
    group1s += remainingPackagesTurnaround(group, remainingPackages, target, currentMin)
    if group1s:
       currentMin = min([len(x) for x in group1s])
    

group1s.sort(key= lambda x: len(x))
group1s = [x for x in group1s if len(x) == len(group1s[0])]

if len(group1s) > 1:
    answer = min([math.prod(x) for x in group1s])
else: 
    answer = math.prod(group1s[0])

print(group1s)
print(answer)