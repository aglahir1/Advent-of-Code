
# Started 02:32
# Finished 02:51

f = open('2016/03.txt', 'r')
inputString = f.read()

def partOne(i):
    i = i[:]
    possible = []
    impossible = []
    for triangle in i:
        triangle = triangle[:]
        triangle.sort(key = lambda x: int(x))
        if int(triangle[0]) + int(triangle[1]) <= int(triangle[2]): impossible.append(triangle[:])
        else: possible.append(triangle[:])
    return len(possible)

def partTwo(i):
    i = i[:]
    possible = []
    impossible = []
    for index in range(int(len(i) / 3)):
        index *= 3
        triangles = [[i[index][0], i[index + 1][0], i[index + 2][0]], [i[index][1], i[index + 1][1], i[index + 2][1]], [i[index][2], i[index + 1][2], i[index + 2][2]]]
        for triangle in triangles:
            triangle = triangle[:]
            triangle.sort(key = lambda x: int(x))
            if int(triangle[0]) + int(triangle[1]) <= int(triangle[2]): impossible.append(triangle[:])
            else: possible.append(triangle[:])
    return len(possible)

inputArray = inputString.splitlines()

inputs = []

for entry in inputArray:
    inputs.append(entry.split())

print(partOne(inputs))

print(partTwo(inputs))
