
# Started
# Finished

from collections import Counter


f = open('2017/07.txt', 'r')
inputString = f.read()

#inputString = """pbga (66)
#xhth (57)
#ebii (61)
#havc (66)
#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
#qoyq (66)
#padx (45) -> pbga, havc, qoyq
#tknk (41) -> ugml, padx, fwft
#jptl (61)
#ugml (68) -> gyxo, ebii, jptl
#gyxo (61)
#cntj (57)"""

class Program:
    def __init__(self, name, weight):
        self.name = name
        self.load = []
        self.parent = None
        self.weight = weight

    def __repr__(self):
        return f'Programme {self.name} has parent {self.parent} and has weight {self.weight}'

    def getFullWeight(self):
        runningSum = self.weight
        for x in self.load:
            runningSum += x.getFullWeight()
        return runningSum

    def checkBalance(self):
        weights = []
        for x in self.load:
            weights.append(x.getFullWeight())
        if len(set(weights)) == 1:
            return 'balanced'
        else:
            counter = Counter(weights)
            return self.load[weights.index(min(counter, key=counter.get))].name
        
    def correctWeight(self):
        weights = []
        for x in self.load:
            weights.append(x.getFullWeight())
        counter = Counter(weights)
        correctWeight = max(counter, key=counter.get)
        culprit = self.load[weights.index(min(counter, key=counter.get))]
        return correctWeight - culprit.getFullWeight() + culprit.weight
    

def partOne(i):
    listOfProgrammes = {}
    for line in i:
        parsed = line.split()
        listOfProgrammes[parsed[0]] = Program(parsed[0], int(parsed[1][1:-1]))
    for line in i:
        parsed = line.split()
        if len(parsed) > 2:
            load = ''.join(parsed[3:]).split(',')
            for p in load:
                listOfProgrammes[parsed[0]].load.append(listOfProgrammes[p])
                listOfProgrammes[p].parent = listOfProgrammes[parsed[0]]
    runningSum = 0
    for p in listOfProgrammes.values():
        if p.parent == None: bottom = p.name
    print(bottom)
    #part two starts here
    search = [bottom]
    while True:
        check = listOfProgrammes[search[-1]].checkBalance()
        if check == 'balanced':
            return listOfProgrammes[search[-2]].correctWeight()
        search.append(check)
    

inputArray = inputString.splitlines()

print(partOne(inputArray))

