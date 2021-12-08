
#Started 16:39
#Ended 17:16

#see 9

import itertools

inputString = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George."""

inputArray = inputString.splitlines()
attendees = ["You"]
attendeesOpinions = []
for entry in inputArray:
    entry = entry.split()
    if entry[0] not in attendees: attendees.append(entry[0])
    x = int(entry[3])
    if entry[2] == 'lose': x *= -1
    a = [entry[0], entry[-1][:-1]]
    a.sort()
    attendeesOpinions.append([a,x])

attendeesOpinions.sort()
newArray = []
for index, opinion in enumerate(attendeesOpinions[::2]):
    index *= 2
    newArray.append([opinion[0], opinion[1] + attendeesOpinions[index + 1][1]])
attendeesOpinions = newArray
for x in attendees:
    attendeesOpinions.append([[x,"You"],0])
possibleSeatings = itertools.permutations(attendees)
newArray = []
for x in list(possibleSeatings):
    x = list(x)
    x.append(x[0])
    newArray.append(x)
possibleSeatings = newArray

seatingHappiness = []

for x in possibleSeatings:
    happiness = 0
    for i in range(len(x)-1):
        pair = [x[i],x[i+1]]
        pair.sort()
        happiness += attendeesOpinions[[x[0] for x in attendeesOpinions].index(pair)][1]
    seatingHappiness.append([x,happiness])

print(seatingHappiness[[x[1] for x in seatingHappiness].index(max([x[1] for x in seatingHappiness]))])