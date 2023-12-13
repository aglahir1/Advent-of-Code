
# Started
# Finished

import copy
from math import sqrt


f = open('2017/21.txt', 'r')
inputString = f.read()

# inputString = """../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#"""

inputArray = inputString.splitlines()

instructions = {}


def rotateAndFlip(square: str) -> set[str]:
    result = set()
    result.add(square)
    a = square[0]
    b = square[1]
    c = square[2]
    d = square[3]
    if len(square) == 4:
        result.add(a+c+b+d)
        result.add(b+d+a+c)
        result.add(b+a+d+c)
        result.add(c+d+a+b)
        result.add(c+a+d+b)
        result.add(d+c+b+a)
        result.add(d+b+c+a)
    else:
        e = square[4]
        f = square[5]
        g = square[6]
        h = square[7]
        i = square[8]
        result.add(a+d+g+b+e+h+c+f+i)
        result.add(c+b+a+f+e+d+i+h+g)
        result.add(c+f+i+b+e+h+a+d+g)
        result.add(g+d+a+h+e+b+i+f+c)
        result.add(g+h+i+d+e+f+a+b+c)
        result.add(i+f+c+h+e+b+g+d+a)
        result.add(i+h+g+f+e+d+c+b+a)
    return result

for i in inputArray:
    i = i.replace('/', '')
    for p in rotateAndFlip(i.split(' => ')[0]):
        instructions[p] = i.split(' => ')[1]

startPattern = ['.#.', '..#', '###']


def divideImage(image: list[str]):
    dividedImage = []
    if len(image) % 2 == 0:
        for y in range(len(image) // 2):
            for x in range(len(image) // 2):
                dividedImage.append(image[0 + 2 * y][0 + 2 * x:2 + 2 * x] + image[1 + 2 * y][0 + 2 * x:2 + 2 * x])
    else:
        for y in range(len(image) // 3):
            for x in range(len(image) // 3):
                dividedImage.append(image[0 + 3 * y][0 + 3 * x:3 + 3 * x] + image[1 + 3 * y][0 + 3 * x:3 + 3 * x] + image[2 + 3 * y][0 + 3 * x:3 + 3 * x])
    return dividedImage

def reconstituteImage(dividedImage: list[str]):
    image: list[str] = []
    bigSize = int(sqrt(len(dividedImage)))
    if len(dividedImage[0]) == 9:
        d = 3
    else:
        d = 4
        
    for y in range(bigSize):
        for subY in range(d):
            line = ''
            for x in range(bigSize):
                line += dividedImage[y * bigSize + x][0 + d * subY:d + d * subY]
            image.append(line)
    return image
        
    
    
def countOnPixels(image: list[str]):
    return sum([x.count('#') for x in image])

def partOne():
    image = copy.copy(startPattern)
    for _ in range(18):
        div = divideImage(image)
        newSquares = [instructions[x] for x in div]
        image = reconstituteImage(newSquares)
    return countOnPixels(image)

def partTwo():
    pass


print(partOne())

print(partTwo())
