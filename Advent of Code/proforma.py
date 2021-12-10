
# Started
# Finished

f = open('Year/Day.txt', 'r')
inputString = f.read()

def partOne(i):
    pass

def partTwo(i):
    pass

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))


p = open('proforma.py', 'r')
proforma = p.read()

for y in range(2016,2021):
    for d in range(1, 26):
        if y == 2016 and d in (2, 1): continue
        f = open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.py', 'w')
        open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.txt', 'x')

        f.write(proforma.replace('Year', str(y)).replace('Day', ('', '0')[d < 10] + str(d)))