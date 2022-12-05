
# Started
# Finished

f = open('2020/07.txt', 'r')
inputString = f.read()

#inputString = """light red bags contain 1 bright white bag, 2 muted yellow bags.
#dark orange bags contain 3 bright white bags, 4 muted yellow bags.
#bright white bags contain 1 shiny gold bag.
#muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
#shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
#dark olive bags contain 3 faded blue bags, 4 dotted black bags.
#vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
#faded blue bags contain no other bags.
#dotted black bags contain no other bags."""

#inputString = """shiny gold bags contain 2 dark red bags.
#dark red bags contain 2 dark orange bags.
#dark orange bags contain 2 dark yellow bags.
#dark yellow bags contain 2 dark green bags.
#dark green bags contain 2 dark blue bags.
#dark blue bags contain 2 dark violet bags.
#dark violet bags contain no other bags."""

def parseRule(r):
    rule = r.split(' contain ')
    bag = ' '.join(rule[0].split()[0:2])
    if rule[1] == 'no other bags.': 
        rule = {bag: 0}
    else:
        contains = rule[1].split(', ')
        contains[-1] = contains[-1][:-1]
        containsforreal = {}
        for x in contains:
            x = x.split()
            containsforreal[' '.join(x[1:3])] = int(x[0])
        rule = {bag: containsforreal}
    return rule

def findContainingBag(r, b):
    listOfBags = []
    for key in r.keys():
        if r[key] != 0:
            if b in r[key]:
                listOfBags.append(key)
                listOfBags += findContainingBag(r, key)
    return listOfBags

def howManyBags(r, b):
    total = 1
    if r[b] == 0: return 1
    for x in r[b]:
        total += r[b][x] * howManyBags(r, x)
    return total


def partOne(i):
    mybag = 'shiny gold'
    rules = {}
    for x in i: rules.update(parseRule(x))
    listOfColours = findContainingBag(rules, mybag)
    return len(set(listOfColours))

def partTwo(i):
    mybag = 'shiny gold'
    rules = {}
    for x in i: rules.update(parseRule(x))
    return howManyBags(rules, mybag) - 1


inputArray = inputString.splitlines()


print(partOne(inputArray))

print(partTwo(inputArray))
