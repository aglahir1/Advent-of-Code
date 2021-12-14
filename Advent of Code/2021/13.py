
# Started 18:25
# Finished

f = open('2021/13.txt', 'r')
inputString = f.read()

#inputString = """6,10
#0,14
#9,10
#0,3
#10,4
#4,11
#6,0
#6,12
#4,1
#0,13
#10,12
#3,4
#3,0
#8,4
#1,10
#2,14
#8,10
#9,0

#fold along y=7
#fold along x=5"""

def addLists(list1, list2):
    returnlist = []
    for i in range(len(list1)):
        if list1[i] == '#' or list2[i] == '#':
            returnlist.append('#')
        else: 
            returnlist.append('.')
    return returnlist

def printMatrix(matrix):
    for x in matrix:
        string = ''
        for z in x:
            if z == '.':
                string += ' '
            else: string += '?'
        print(string)

def countMatrix(matrix):
    count = 0
    for x in matrix:
        count += x.count('#')
    return count

def partOne(dots, instructions):
    matrix = [['.'] * (max([int(x.split(',')[0]) for x in dots]) + 1) for _ in range(max([int(x.split(',')[1]) for x in dots]) + 1)]
    for x in dots:
        x = x.split(',')
        matrix[int(x[1])][int(x[0])] = '#'
    for x in instructions[0:1]:
        swapmatrix = []
        x = x.split()[-1].split('=')
        print(x)
        k = int(x[1])
        if x[0] == 'y':
            amountAbove = k
            amountBelow = len(matrix) - k - 1
            if amountAbove > amountBelow:
                for j in range(amountAbove - amountBelow):
                    swapmatrix.append(matrix.pop(0))
                    k -= 1
            for i in range(k):
                swapmatrix.append(addLists(matrix[i], matrix[-(i+1)]))
            matrix = swapmatrix[:]
        else: 
            amountLeft = k
            amountRight = len(matrix[0]) - k - 1
            if amountLeft > amountRight:
                for j in range(amountLeft - amountRight):
                    swapmatrix.append([x.pop(0) for x in matrix])
                    k -= 1
            for i in range(k):
                swapmatrix.append(addLists([z[i] for z in matrix], [y[-(i+1)] for y in matrix]))
            matrix = []
            for i in range(len(swapmatrix[0])):
                matrix.append([z[i] for z in swapmatrix])
    return countMatrix(matrix)

def partTwo(dots, instructions):
    matrix = [['.'] * (max([int(x.split(',')[0]) for x in dots]) + 1) for _ in range(max([int(x.split(',')[1]) for x in dots]) + 1)]
    for x in dots:
        x = x.split(',')
        matrix[int(x[1])][int(x[0])] = '#'
    for x in instructions:
        swapmatrix = []
        x = x.split()[-1].split('=')
        print(x)
        k = int(x[1])
        if x[0] == 'y':
            amountAbove = k
            amountBelow = len(matrix) - k - 1
            if amountAbove > amountBelow:
                for j in range(amountAbove - amountBelow):
                    swapmatrix.append(matrix.pop(0))
                    k -= 1
            for i in range(k):
                swapmatrix.append(addLists(matrix[i], matrix[-(i+1)]))
            matrix = swapmatrix[:]
        else: 
            amountLeft = k
            amountRight = len(matrix[0]) - k - 1
            if amountLeft > amountRight:
                for j in range(amountLeft - amountRight):
                    swapmatrix.append([x.pop(0) for x in matrix])
                    k -= 1
            for i in range(k):
                swapmatrix.append(addLists([z[i] for z in matrix], [y[-(i+1)] for y in matrix]))
            matrix = []
            for i in range(len(swapmatrix[0])):
                matrix.append([z[i] for z in swapmatrix])
    printMatrix(matrix)
    return countMatrix(matrix)

i = inputString.split('\n\n')
dots = i[0].splitlines()
instructions = i[1].splitlines()

print(partOne(dots, instructions))

print(partTwo(dots, instructions))