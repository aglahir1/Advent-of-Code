
# Started
# Finished

f = open('2023/01.txt', 'r')
inputString = f.read()

#inputString = """two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen"""

def partOne(i):
    calibrationDigits = []
    for line in i:
        lineDigits = []
        for char in line:
            if char.isdigit():
                lineDigits.append(char)
        calibrationDigit = lineDigits[0] + lineDigits[-1]
        calibrationDigits.append(int(calibrationDigit))
    return sum(calibrationDigits)

def partTwo(i):
    calibrationDigits = []
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for line in i:
        earliest = [9999, '']
        latest = [-1, '']
        for n in numbers.keys():
            eindex = line.find(n)
            lindex = line.rfind(n)
            if eindex != -1 and eindex < earliest[0]: earliest = [eindex, n]

            if lindex != -1 and lindex > latest[0]: latest = [lindex, n]
        calibrationDigits.append(numbers[earliest[1]] * 10 + numbers[latest[1]])
    return sum(calibrationDigits)



def parseInput(inputString: str):
    inputArray = inputString.splitlines()
    return inputArray



print(partOne(parseInput(inputString)))

print(partTwo(parseInput(inputString)))
