
# Started
# Finished

from pprint import pprint

f = open('2020/16.txt', 'r')
inputString = f.read()

#inputString = """class: 1-3 or 5-7
#row: 6-11 or 33-44
#seat: 13-40 or 45-50

#your ticket:
#7,1,14

#nearby tickets:
#7,3,47
#40,4,50
#55,2,20
#38,6,12"""

#inputString = """class: 0-1 or 4-19
#row: 0-5 or 8-19
#seat: 0-13 or 16-19

#your ticket:
#11,12,13

#nearby tickets:
#3,9,18
#15,1,5
#5,14,9"""

def partOne(i):
    fields = [x.split(': ')[1] for x in i[0].splitlines()]
    myTicket = i[1].splitlines()[1]
    otherTickets = i[2].splitlines()[1:]
    otherTickets = [[int(y) for y in x.split(',')] for x in otherTickets]
    ranges = [x.split()[0] for x in fields] + [x.split()[2] for x in fields]
    allowedNums = set()
    for r in ranges:
        allowedNums.update(set(range(int(r.split('-')[0]),int(r.split('-')[1]) + 1)))
    count = 0
    for t in otherTickets:
        for x in t:
            if x in allowedNums: continue
            count += x
            break
    return count

def partTwo(i):
    fields = {x.split(': ')[0]: x.split(': ')[1] for x in i[0].splitlines()}
    myTicket = i[1].splitlines()[1]
    otherTickets = i[2].splitlines()[1:]
    otherTickets = [[int(y) for y in x.split(',')] for x in otherTickets]
    ranges = {k: set(range(int(fields[k].split()[0].split('-')[0]),int(fields[k].split()[0].split('-')[1]) + 1)).union(set(range(int(fields[k].split()[2].split('-')[0]),int(fields[k].split()[2].split('-')[1]) + 1))) for k in fields}
    allowedNums = set().union(*ranges.values())
    ticketsToGo = []
    for j, t in enumerate(otherTickets):
        for x in t:
            if x in allowedNums: continue
            ticketsToGo.append(j)
            break
    for x in ticketsToGo[::-1]:
        otherTickets.pop(x)
    availableFields = list(fields.keys())
    confirmedFields = [''] * len(otherTickets[0])
    while len(availableFields) > 0:
        for j in range(len(otherTickets[0])):
            if confirmedFields[j] != '': continue
            possibleFields = availableFields[:]
            field = [x[j] for x in otherTickets]
            for x in field:
                for k in possibleFields:
                    if x in ranges[k]: continue
                    possibleFields.remove(k)
                if len(possibleFields) == 1:
                    break
            if len(possibleFields) == 1:
                confirmedFields[j] = possibleFields[0]
                availableFields.remove(possibleFields[0])
    returnValue = 1
    for j, x in enumerate([int(l) for l in myTicket.split(',')]):
        if confirmedFields[j].split()[0] == 'departure':
            returnValue *= x
    return returnValue

inputArray = inputString.split('\n\n')

print(partOne(inputArray))

print(partTwo(inputArray))
