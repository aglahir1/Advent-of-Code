
# Started
# Finished



f = open('2017/01.txt', 'r')
inputString: str = f.read()

#inputString = '1122'

def partOne(i):
    numbers: list = []
    for pointer in range(len(i)):
        num1: int = int(i[pointer])
        num2: int = int(i[(pointer + 1) % len(i)])
        if num1 == num2: numbers.append(num1)
    return sum(numbers)

def partTwo(i):
    numbers: list = []
    for pointer in range(len(i)):
        num1: int = int(i[pointer])
        num2: int = int(i[(pointer + int(len(i)/2)) % len(i)])
        if num1 == num2: numbers.append(num1)
    return sum(numbers)

inputArray: list = list(inputString)

print(partOne(inputArray))

print(partTwo(inputArray))
