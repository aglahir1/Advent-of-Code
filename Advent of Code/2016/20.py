
# Started
# Finished

f = open('2016/20.txt', 'r')
inputString = f.read()

# inputString = """5-8
# 0-2
# 4-7"""


def parseBlacklist(blacklist: str, whitelist: list[list[int]]) -> list[list[int]]:
    blocked = [int(x) for x in blacklist.split('-')]
    newWhitelist = []
    for i in range(len(whitelist)):
        if whitelist[i][1] < blocked[0]:
            newWhitelist.append(whitelist[i])
            continue
        if blocked[1] < whitelist[i][0]:
            newWhitelist.append(whitelist[i])
            continue
        if blocked[0] <= whitelist[i][0] and whitelist[i][1] <= blocked[1]:
            continue
        if whitelist[i][0] <= blocked[0] and blocked[1] <= whitelist[i][1]:
            if whitelist[i][0] != blocked[0]:
                newWhitelist.append([whitelist[i][0], blocked[0] - 1])
            if blocked[1] != whitelist[i][1]:
                newWhitelist.append([blocked[1] + 1, whitelist[i][1]])
            continue
        if blocked[0] < whitelist[i][0] and blocked[1] < whitelist[i][1]:
            newWhitelist.append([blocked[1] + 1, whitelist[i][1]])
            continue
        if whitelist[i][0] < blocked[0] and whitelist[i][1] < blocked[1]:
            newWhitelist.append([whitelist[i][0], blocked[0] - 1])
            continue
    return newWhitelist
            
            
            
        

def partOne(i):
    allowed = [[0, 4294967295]]
    for line in i:
        allowed = parseBlacklist(line, allowed)
    print(allowed[0][0])
    return sum([x[1] - x[0] + 1 for x in allowed])


inputArray = inputString.splitlines()

print(partOne(inputArray))