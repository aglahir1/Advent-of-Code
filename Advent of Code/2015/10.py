
inputString = "3113322113"

#inputString = "1"


amountOfIterations = 50

while(amountOfIterations > 0):
    counter = 0
    result = ''
    number = inputString[0]
    for digit in inputString:
        if digit == number:
            counter += 1
        else:
            result += str(counter) + number
            number = digit
            counter = 1
    result += str(counter) + number
    inputString = result
    amountOfIterations -= 1

print(len(inputString))