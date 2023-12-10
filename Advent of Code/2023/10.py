
# Started
# Finished

f = open('2023/10.txt', 'r')
inputString = f.read()

def partOne(i: list[list[str]]):
    pipes = []
    for y, line in enumerate(i):
        for x, c in enumerate(line):
            if c == 'S': 
                pipes.append(f'{x},{y}')
                currX = x + 1
                currY = y
                previous = 'l'
                break
        if len(pipes) == 1: break
    while True:
        if f'{currX},{currY}' in pipes:
            print(len(pipes) / 2)
            break
        pipes.append(f'{currX},{currY}')
        match i[currY][currX]:
            case '|':
                if previous == 'b':
                    currY -= 1
                else:
                    currY += 1
            case '-':
                if previous == 'l':
                    currX += 1
                else:
                    currX -= 1
            case 'L':
                if previous == 't':
                    currX += 1
                    previous = 'l'
                else:
                    currY -= 1
                    previous = 'b'
            case 'J':
                if previous == 'l':
                    currY -= 1
                    previous = 'b'
                else:
                    currX -= 1
                    previous = 'r'
            case '7':
                if previous == 'l':
                    currY += 1
                    previous = 't'
                else:
                    currX -= 1
                    previous = 'r'
            case 'F':
                if previous == 'r':
                    currY += 1
                    previous = 't'
                else:
                    currX += 1
                    previous = 'l'
    inside = False
    onPipe = False
    joinedPipe = ''
    joinHash = {'7': 'b', 'F': 'b', 'J': 't', 'L': 't', 'S': 'b'}
    count = 0
    for y in range(len(i)):
        for x in range(len(i[0])):
            if f'{x},{y}' in pipes:
                if i[y][x] == '|':
                    inside = not inside
                elif i[y][x] != '-':
                    if onPipe:
                        onPipe = False
                        if joinHash[i[y][x]] != joinedPipe:
                            inside = not inside
                    else:
                        onPipe = True
                        joinedPipe = joinHash[i[y][x]]
            elif inside:
                count += 1
        if inside:
            print(f'panic at line: {y}')
            break
    return count
    

inputArray = [[x for x in j] for j in inputString.splitlines()]

print(partOne(inputArray))
