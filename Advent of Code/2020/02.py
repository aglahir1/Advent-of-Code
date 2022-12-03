
# Started
# Finished

f = open('2020/02.txt', 'r')
inputString = f.read()

#inputString = """1-3 a: abcde
#1-3 b: cdefg
#2-9 c: ccccccccc"""

def partOne(i):
    valid = 0
    for pw in i:
        if pw['min'] <= pw['password'].count(pw['letter']) <= pw['max']: valid += 1
    return valid

def partTwo(i):
    valid = 0
    for pw in i:
        word = pw['password'][pw['min']]+ pw['password'][pw['max']]
        if word.count(pw['letter']) == 1: valid += 1
    return valid
        

inputArray = inputString.splitlines()

i = [{'min': int(x[0].split('-')[0]), 'max': int(x[0].split('-')[1]), 'letter': x[1][0], 'password': x[2]} for x in [i.split(' ') for i in inputArray]]

print(partOne(i))

inputArray = [{'min': int(x[0].split('-')[0]) - 1, 'max': int(x[0].split('-')[1]) - 1, 'letter': x[1][0], 'password': x[2]} for x in [i.split(' ') for i in inputArray]]


print(partTwo(inputArray))
