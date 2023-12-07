
# Started
# Finished

f = open('2017/12.txt', 'r')
inputString = f.read()

# # inputString = """0 <-> 2
# # 1 <-> 1
# # 2 <-> 0, 3, 4
# # 3 <-> 2, 4
# # 4 <-> 2, 3, 6
# # 5 <-> 6
# # 6 <-> 4, 5"""

def findConnections(groupSoFar: set[int], connections: list[list[int]], house: int): 
    furtherHouses = connections[house]
    for h in furtherHouses:
        if h in groupSoFar:
            continue
        groupSoFar.add(h)
        housesToAdd = findConnections(groupSoFar, connections, h)
        for x in housesToAdd:
            groupSoFar.add(x)
    return groupSoFar

def partOne(i: list[list[int]]):
    connectsTo = set()
    connectsTo = findConnections(connectsTo, i, 0)
    return len(connectsTo)
    

def partTwo(i):
    groups: list[set[int]] = []
    for h in range(len(i)):
        if all([h not in x for x in groups]):
            groups.append(findConnections(set([h]), i, h))
    return len(groups)

inputArray = [[int(j) for j in x.split('<->')[1].split(',')] for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
