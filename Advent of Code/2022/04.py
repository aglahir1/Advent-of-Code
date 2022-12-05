
# Started
# Finished

f = open('2022/04.txt', 'r')
inputString = f.read()

#inputString = """2-4,6-8
#2-3,4-5
#5-7,7-9
#2-8,3-7
#6-6,4-6
#2-6,4-8"""

def partOne(i):
    contained = 0
    for pair in i:
        pair = pair.split(',')
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')
        if (int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1])) or (int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1])): 
            contained += 1
    return contained

def partTwo(i):
    overlap = 0
    for pair in i:
        pair = pair.split(',')
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')
        if int(pair[1][0]) <= int(pair[0][0]) <= int(pair[1][1]) or int(pair[1][0]) <= int(pair[0][1]) <= int(pair[1][1]) or int(pair[0][0]) <= int(pair[1][0]) <= int(pair[0][1]) or int(pair[0][0]) <= int(pair[1][1]) <= int(pair[0][1]): overlap += 1
    return overlap

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
