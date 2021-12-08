
# Started 15:08
# Finished 15:33

f = open('2015/16.txt', 'r')
inputString = f.read()

inputArray = inputString.splitlines()

auntArray = []

correctAuntString = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

for entry in inputArray:
    entry = entry.split()
    auntArray.append({'number': entry[1][:-1], entry[2][:-1]: int(entry[3][:-1]), entry[4][:-1]: int(entry[5][:-1]), entry[6][:-1]: int(entry[7])})

correctAuntArray = correctAuntString.splitlines()
correctAunt = []

for a in correctAuntArray:
    a = a.split()
    correctAunt.append([a[0][:-1], int(a[1])])
    

for attribute in correctAunt:
    newAuntArray = []
    for aunt in auntArray:
        if attribute[0] in aunt:
            if attribute[0] in ('cats', 'trees'):
                if aunt[attribute[0]] > attribute[1]: newAuntArray.append(aunt)
            elif attribute[0] in ('pomeranians', 'goldfish'):
                if aunt[attribute[0]] < attribute[1]: newAuntArray.append(aunt)
            elif aunt[attribute[0]] == attribute[1]: newAuntArray.append(aunt)
        else:
            newAuntArray.append(aunt)
    auntArray = newAuntArray[:]

print(auntArray)