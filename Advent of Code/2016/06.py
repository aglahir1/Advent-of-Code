
# Started 01:40
# Finished 01:55

import itertools

f = open('2016/06.txt', 'r')
inputString = f.read()

#inputString = """eedadn
#drvtee
#eandsr
#raavrd
#atevrs
#tsrnev
#sdttsa
#rasrtv
#nssdts
#ntnada
#svetve
#tesnvt
#vntsnd
#vrdear
#dvrsen
#enarar"""

def partOne(i):
    correct = ''
    for z in range(len(i[0])):
        col = [x[z] for x in i]
        col.sort()
        unduped = [x[0] for x in list(itertools.groupby(col))]
        counted = [[x, col.count(x)] for x in unduped]
        counted.sort(key = lambda x: x[1], reverse = True)
        correct += counted[0][0]
    return correct

def partTwo(i):
    correct = ''
    for z in range(len(i[0])):
        col = [x[z] for x in i]
        col.sort()
        unduped = [x[0] for x in list(itertools.groupby(col))]
        counted = [[x, col.count(x)] for x in unduped]
        counted.sort(key = lambda x: x[1], reverse = True)
        correct += counted[-1][0]
    return correct

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
