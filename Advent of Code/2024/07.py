
# Started
# Finished

f = open('2024/07.txt', 'r')
inputString = f.read()

# inputString = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

def partOne(i):
    runningSum = 0
    for calib in i:
        options = [{'ops': '', 'curr': calib['result']}]
        for j, op in enumerate(calib['operands'][::-1]):
            newOptions = []
            for o in options:
                if op > o['curr']: continue
                if o['curr'] - op == 0 and j == len(calib['operands']) - 1:
                    runningSum += calib['result']
                    break
                if o['curr'] % op == 0:
                    newOptions.append({'ops': o['ops'] + '*', 'curr': o['curr'] // op})
                newOptions.append({'ops': o['ops'] + '+', 'curr': o['curr'] - op})
            options = newOptions
    return runningSum
                

def partTwo(i):
    runningSum = 0
    for idx, calib in enumerate(i):
        options = [{'ops': '', 'curr': calib['operands'][0]}]
        for j, op in enumerate(calib['operands'][1:]):
            newOptions = []
            for o in options:
                if o['curr'] > calib['result']: continue
                newOptions.append({'ops': o['ops'] + '*', 'curr': o['curr'] * op})
                newOptions.append({'ops': o['ops'] + '+', 'curr': o['curr'] + op})
                newOptions.append({'ops': o['ops'] + '|', 'curr': int(str(o['curr']) + str(op))})
            options = newOptions
        for o in options:
            if o['curr'] == calib['result']:
                runningSum += calib['result']
                break
        print(f'{idx + 1} / {len(i)}')
    return runningSum

inputArray = [{'result': int(x.split(':')[0]), 'operands': list(map(int, x.split(': ')[1].split()))} for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
