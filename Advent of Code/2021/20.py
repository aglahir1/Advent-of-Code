
# Started 18:40
# Finished 19:22

import copy

f = open('2021/20.txt', 'r')
inputString = f.read()

#inputString = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

##..#.
##....
###..#
#..#..
#..###"""

def printArray(array):
    for line in array:
        for pixel in line:
            print(pixel, end="")
        print()

def decodeImage(image, algorithm, swap):
    re = copy.deepcopy(image)
    curr = image[0][0]
    if curr == '.': switch = '#'
    else: switch = '.'
    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            if x == 0 or x == len(line) - 1 or y == 0 or y == len(image) - 1:
                if swap: re[y][x] = switch
                else: re[y][x] = curr
            else:
                pass #decodePixel
                pixels = [image[y-1][x-1], image[y-1][x], image[y-1][x+1], image[y][x-1], image[y][x], image[y][x+1], image[y+1][x-1], image[y+1][x], image[y+1][x+1]]
                bits = ''
                for pix in pixels:
                    if pix == '.': bits += '0'
                    else: bits += '1'
                num = int(bits, base=2)
                re[y][x] = algorithm[num]
    return re

def grow(image, amount):
    outImage = [['.']*(len(image[0]) + 2 * amount) for _ in range(amount)]
    for line in image:
        outImage.append(['.']*amount + line + ['.']*amount)
    outImage += [['.']*(len(image[0]) + 2 * amount) for _ in range(amount)]
    return outImage

def countLitPixels(image):
    count = 0
    for line in image:
        for pix in line:
            if pix == '#': count += 1
    return count


def partOne(algorithm, image, amount):
    image = grow(image, amount + 1)
    count = 0
    while count < amount:
        count += 1
        image = decodeImage(image, algorithm, True)
    printArray(image)
    return countLitPixels(image)

inputArray = inputString.splitlines()

algorithm = inputArray[0]
image = []
for line in inputArray[2:]:
    image.append(list(line))

print(partOne(algorithm, image, 2))

print(partOne(algorithm, image, 50))
