

# Started 11:20
# P 11:50 - 12:10
# Finished 12:12

f = open('2021/10.txt', 'r')
inputString = f.read()

#inputString = """[({(<(())[]>[[{[]{<()<>>
#[(()[<>])]({[<{<<[]>>(
#{([(<{}[<>[]}>{[]{[(<()>
#(((({<>}<{<{<>}{[]{[]{}
#[[<[([]))<([[{}[[()]]]
#[{[{({}]{}}([{[{{{}}([]
#{<[[]]>}<{[{[{[]{()[[[]
#[<(<(<(<{}))><([]([]()
#<{([([[(<>()){}]>(<<{{
#<{([{{}}[<[[[<>{}]]]>[]]"""

def partOne(i):
    illegalchs = []
    for entry in i:
        chs = []
        for ch in entry:
            if ch in ('{', '[', '(', '<'):
                chs.append(ch)
            else:
                if ch == '}':
                    if chs[-1] == '{':
                        chs.pop(-1)
                        continue
                    illegalchs.append(ch)
                    break
                if ch == ']':
                    if chs[-1] == '[':
                        chs.pop(-1)
                        continue
                    illegalchs.append(ch)
                    break
                if ch == ')':
                    if chs[-1] == '(':
                        chs.pop(-1)
                        continue
                    illegalchs.append(ch)
                    break
                if ch == '>':
                    if chs[-1] == '<':
                        chs.pop(-1)
                        continue
                    illegalchs.append(ch)
                    break
    syntaxScore = illegalchs.count('}') * 1197
    syntaxScore += illegalchs.count(')') * 3
    syntaxScore += illegalchs.count(']') * 57
    syntaxScore += illegalchs.count('>') * 25137
    return syntaxScore


def partTwo(i):
    correctStrings = []
    for entry in i:
        chs = []
        valid = True
        for ch in entry:
            if ch in ('{', '[', '(', '<'):
                chs.append(ch)
            else:
                if ch == '}':
                    if chs[-1] == '{':
                        chs.pop(-1)
                        continue
                    valid = False
                    break
                if ch == ']':
                    if chs[-1] == '[':
                        chs.pop(-1)
                        continue
                    valid = False
                    break
                if ch == ')':
                    if chs[-1] == '(':
                        chs.pop(-1)
                        continue
                    valid = False
                    break
                if ch == '>':
                    if chs[-1] == '<':
                        chs.pop(-1)
                        continue
                    valid = False
                    break
        if valid: correctStrings.append(chs[::-1])

    syntaxScore = []
    for x in correctStrings:
        score = 0
        for z in x:
            score *= 5
            if z == '(': score += 1
            if z == '[': score += 2
            if z == '{': score += 3
            if z == '<': score += 4
        syntaxScore.append(score)
    print(syntaxScore)
    syntaxScore.sort()

    return syntaxScore[int(len(syntaxScore) / 2)]

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))