
# Started 15:33
# Finished 15:51

import itertools

f = open('2015/17.txt', 'r')
inputString = f.read()

eggnog = 150

#inputString = """20
#15
#10
#5
#5"""

#eggnog = 25

inputArray = inputString.splitlines()
containers = []
for entry in inputArray:
    containers.append(int(entry))

permutations = []

for x in range(len(containers)):
    permutations += list(itertools.combinations(containers, x+1))

possibilities = []

for x in permutations:
    if sum(list(x)) == eggnog: possibilities.append([x, len(x)])

minimum = min([x[1] for x in possibilities])

result = []

for x in possibilities:
    if x[1] == minimum: result.append(x[:])

print(result)