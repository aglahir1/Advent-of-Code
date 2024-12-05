
# Started
# Finished

f = open('2024/05.txt', 'r')
inputString = f.read()

#inputString = """47|53
#97|13
#97|61
#97|47
#75|29
#61|13
#75|53
#29|13
#97|29
#53|29
#61|53
#97|53
#61|29
#47|13
#75|47
#97|75
#47|61
#75|61
#47|29
#75|13
#53|13

#75,47,61,53,29
#97,61,53,29,13
#75,29,13
#75,97,47,61,53
#61,13,29
#97,13,75,29,47"""

def isRuleApplicable(rule: list[str], update: list[str]) -> bool:
    return rule[0] in update and rule[1] in update

def checkRule(rule: list[str], update: list[str]) -> bool:
    if not isRuleApplicable(rule, update): return True
    return update.index(rule[0]) < update.index(rule[1])

def reorder(update: list[str], rules: list[list[str]]) -> list[str]:
    i = 0
    temp = update.copy()
    while any([not checkRule(r, temp) for r in rules]):
        for j in range(i + 1, len(temp)):
            if all([checkRule(r, [temp[i], temp[j]]) for r in rules]):
                continue
            else:
                a = temp[i]
                temp[i] = temp[j]
                temp[j] = a
                i -= 1
                break
        i += 1
    return temp

def partOne(i):
    runningsum = 0
    wrongsum = 0
    index = 0
    max = len(i['updates'])
    for u in i['updates']:
        if all([checkRule(r, u) for r in i['rules']]):
            runningsum += int(u[len(u) // 2])
        else:
            wrongsum += int(reorder(u, i['rules'])[len(u) // 2])
        index += 1
        print(f'{index} / {max}')
    return {'part one': runningsum, 'part two': wrongsum}

inputArray = {'rules': [x.split('|') for x in inputString.split('\n\n')[0].splitlines()], 'updates': [x.split(',') for x in inputString.split('\n\n')[1].splitlines()]}

print(partOne(inputArray))
