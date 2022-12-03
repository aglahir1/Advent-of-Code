
# Started 13:48
# Finished 13:59

f = open('2022/01.txt', 'r')
inputString = f.read()

#inputString = """1000
#2000
#3000

#4000

#5000
#6000

#7000
#8000
#9000

#10000"""

def partOne(i):
    totalcals = [sum(x) for x in i]
    result = max(totalcals)
    return result

def partTwo(i):
    totalcals = [sum(x) for x in i]
    totalcals.sort(reverse = True)
    return sum(totalcals[0:3])

inputArray = inputString.split('\n\n')
inputArray = [list(map(int, x.split('\n'))) for x in inputArray]

print(partOne(inputArray))

print(partTwo(inputArray))
