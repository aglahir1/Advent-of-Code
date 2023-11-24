
# Started
# Finished


f = open('2017/02.txt', 'r')
inputString = f.read()
#inputString = """5 9 2 8
#9 4 7 3
#3 8 6 5"""

def partOne(i):
    differences: list = []
    for row in i:
        differences.append(max(row) - min(row))
    return sum(differences)

def partTwo(i):
    divisions: list = []
    for row in i:
        row = sorted(row, reverse = True)
        divisions.append(findMultiple(row))
    return sum(divisions)


def findMultiple(row:list):
        for j in range(len(row)):
            for y in range(j + 1,len(row)):
                if row[j] % row[y] == 0:
                    return int(row[j] / row[y])


inputArray = [[int(y) for y in x.split()] for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
