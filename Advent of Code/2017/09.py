
# Started
# Finished

f = open('2017/09.txt', 'r')
inputString = f.read()

#inputString = '{{{},{},{{}}}}'

def cleanoutgarbage(i):
    cleaned = ''
    garbaged = 0
    gFlag = False
    throw = False
    for c in i:
        if throw:
            throw = False
            continue
        if gFlag:
            if c not in '!>':
                garbaged += 1
                continue
            if c == '!':
                throw = True
                continue
            gFlag = False
            continue
        if c == '<':
            gFlag = True
            continue
        cleaned += c
    return (cleaned, garbaged)

def partOne(i):
    i = cleanoutgarbage(i)
    level = 0
    runningSum = 0
    for c in i[0]:
        if c == '{':
            level += 1
        if c == '}':
            runningSum += level
            level -= 1
    return (runningSum,i[1])

print(partOne(inputString))