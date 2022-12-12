
# Started
# Finished

from typing import List

f = open('2022/11.txt', 'r')
inputString = f.read()

class Item:
    worryLevel: int

    def __init__(self, worryLevel):
        self.worryLevel = worryLevel

    def relief(self):
        self.worryLevel = int(self.worryLevel / 3)

class Monkey:
    items: List[Item]
    inspectionCount: int

    def __init__(self, startingItems, operation, test):
        self.items = [Item(x) for x in startingItems]
        self.operation = operation
        self.test = test
        self.inspectionCount = 0

    def inspectItems(self):
        for i, item in enumerate(self.items):
            item.worryLevel = self.operation(item.worryLevel)
            #item.relief()
            self.test(self, item, i)
            self.inspectionCount += 1
        self.items = []

    def throwItem(self, recipient, itemIndex):
        item = self.items[itemIndex]
        item.worryLevel = item.worryLevel % (11 * 7 * 3 * 5 * 17 * 13 * 19 * 2)
        monkeys[recipient].items.append(item)

    def __str__(self):
        return 'This Monkey inspected items ' + str(self.inspectionCount) + ' times.'
        return 'This Monkey has ' + str(len(self.items)) + ' items: ' + ', '.join([str(x.worryLevel) for x in self.items])


monkeys: List[Monkey]

# START TEST INPUT

def toperation0(old):
    return old * 19

def toperation1(old):
    return old + 6

def toperation2(old):
    return old * old

def toperation3(old):
    return old + 3

def ttest0(self, item, i):
    if item.worryLevel % 23 == 0: self.throwItem(2, i)
    else: self.throwItem(3, i)

def ttest1(self, item, i):
    if item.worryLevel % 19 == 0: self.throwItem(2, i)
    else: self.throwItem(0, i)

def ttest2(self, item, i):
    if item.worryLevel % 13 == 0: self.throwItem(1, i)
    else: self.throwItem(3, i)

def ttest3(self, item, i):
    if item.worryLevel % 17 == 0: self.throwItem(0, i)
    else: self.throwItem(1, i)

monkeys = [
    Monkey([79, 98], toperation0, ttest0),
    Monkey([54, 65, 75, 74], toperation1, ttest1),
    Monkey([79, 60, 97], toperation2, ttest2),
    Monkey([74], toperation3, ttest3)
    ]

# END TEST INPUT

def operation0(old):
    return old * 3

def operation1(old):
    return old * old

def operation2(old):
    return old + 1

def operation3(old):
    return old + 8

def operation4(old):
    return old + 3

def operation5(old):
    return old + 4

def operation6(old):
    return old * 17

def operation7(old):
    return old + 7

def test0(self, item, i):
    if item.worryLevel % 11 == 0: self.throwItem(2, i)
    else: self.throwItem(7, i)

def test1(self, item, i):
    if item.worryLevel % 7 == 0: self.throwItem(0, i)
    else: self.throwItem(2, i)

def test2(self, item, i):
    if item.worryLevel % 3 == 0: self.throwItem(7, i)
    else: self.throwItem(5, i)

def test3(self, item, i):
    if item.worryLevel % 5 == 0: self.throwItem(6, i)
    else: self.throwItem(4, i)

def test4(self, item, i):
    if item.worryLevel % 17 == 0: self.throwItem(1, i)
    else: self.throwItem(0, i)

def test5(self, item, i):
    if item.worryLevel % 13 == 0: self.throwItem(6, i)
    else: self.throwItem(3, i)

def test6(self, item, i):
    if item.worryLevel % 19 == 0: self.throwItem(4, i)
    else: self.throwItem(1, i)

def test7(self, item, i):
    if item.worryLevel % 2 == 0: self.throwItem(5, i)
    else: self.throwItem(3, i)
    
monkeys = [
    Monkey([50, 70, 54, 83, 52, 78], operation0, test0),
    Monkey([71, 52, 58, 60, 71], operation1, test1),
    Monkey([66, 56, 56, 94, 60, 86, 73], operation2, test2),
    Monkey([83, 99], operation3, test3),
    Monkey([98, 98, 79], operation4, test4),
    Monkey([76], operation5, test5),
    Monkey([52, 51, 84, 54], operation6, test6),
    Monkey([82, 86, 91, 79, 94, 92, 59, 94], operation7, test7),
    ]

for _ in range(10000):
    for x in monkeys:
        x.inspectItems()

inspectionCounts: List[int] = [x.inspectionCount for x in monkeys]
inspectionCounts.sort()
print(inspectionCounts[-2] * inspectionCounts[-1])