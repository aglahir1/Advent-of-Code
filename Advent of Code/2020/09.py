
# Started
# Finished

f = open('2020/09.txt', 'r')
inputString = f.read()
global windowLength
windowLength = 25

#inputString = """35
#20
#15
#25
#47
#40
#62
#55
#65
#95
#102
#117
#150
#182
#127
#219
#299
#277
#309
#576"""
#windowLength = 5

def checkifsummable(window, num):
    for v in window:
        if v * 2 != num and num - v in window: return True
    return False

def partOne(i):
    pos = 0
    while pos < len(i) - windowLength:
        window = i[pos:pos+windowLength]
        num = i[pos+windowLength]
        pos += 1
        if not checkifsummable(window, num): return num

def partTwo(i):
    target = partOne(i)
    goal = []
    for j, x in enumerate(i):
        for x in i[j:]:
            if sum(goal) < target: goal.append(x)
            elif sum(goal) > target: 
                goal = []
                break
            elif sum(goal) == target:
                goal.sort()
                return goal[0] + goal[-1]
    

inputArray = inputString.splitlines()
actualarray = []
for x in inputArray:
    actualarray.append(int(x))

print(partOne(actualarray))

print(partTwo(actualarray))
