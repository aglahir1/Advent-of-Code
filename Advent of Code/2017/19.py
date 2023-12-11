
# Started
# Finished

f = open('2017/19.txt', 'r')
inputString = f.read()

def partOne(i: list[str]):
    pY = 1
    pX = i[1].index('|')
    heading = 'd'
    letters = []
    count = 0
    while 0 <= pY < len(i) and 0 <= pX < len(i[0]):
        count += 1
        match heading:
            case 'd':
                pY += 1
            case 'u':
                pY -= 1
            case 'l':
                pX -= 1
            case 'r':
                pX += 1
        if i[pY][pX] not in '|-+ ':
            letters.append(i[pY][pX])
            print(letters)
            continue
        if i[pY][pX] == ' ':
            break
        if i[pY][pX] == '+':
            if i[pY + 1][pX] == '|' and heading not in 'ud':
                heading = 'd'
            elif i[pY - 1][pX] == '|' and heading not in 'ud':
                heading = 'u'
            elif i[pY][pX + 1] == '-' and heading not in 'lr':
                heading = 'r'
            elif i[pY][pX - 1] == '-' and heading not in 'lr':
                heading = 'l'
    return [''.join(letters), count]

inputArray = [' ' + x + ' ' for x in inputString.splitlines()]
inputArray = [' '*len(inputArray)] + inputArray + [' '*len(inputArray)]

print(partOne(inputArray))
