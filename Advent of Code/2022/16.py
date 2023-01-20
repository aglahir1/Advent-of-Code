
# Started
# Finished

from typing import Dict, List
from pprint import pprint
from itertools import permutations

f = open('2022/16.txt', 'r')
inputString = f.read()

#inputString = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
#Valve BB has flow rate=13; tunnels lead to valves CC, AA
#Valve CC has flow rate=2; tunnels lead to valves DD, BB
#Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
#Valve EE has flow rate=3; tunnels lead to valves FF, DD
#Valve FF has flow rate=0; tunnels lead to valves EE, GG
#Valve GG has flow rate=0; tunnels lead to valves FF, HH
#Valve HH has flow rate=22; tunnel leads to valve GG
#Valve II has flow rate=0; tunnels lead to valves AA, JJ
#Valve JJ has flow rate=21; tunnel leads to valve II"""

class Valve:
    pass

valves: Dict[str, Valve]
valves = dict()

class Valve:
    name: str
    pressure: int
    tunnels: List[Valve]
    state: bool
    distances: Dict[str, int]

    def __init__(self, name: str, pressure: int):
        self.name = name
        self.pressure = pressure
        self.tunnels = []
        self.state = False

    def __repr__(self):
        returnString = 'Valve ' + self.name + ' with flow rate: ' + str(self.pressure)
        if len(self.tunnels) > 0:
            returnString += ' with tunnels to: '
            for t in self.tunnels:
                returnString += t.name + ' '
        pprint(self.distances)
        return returnString

    def addTunnels(self, tunnels: List[str]):
        self.distances = dict().fromkeys(valves.keys())
        for name in tunnels:
            self.tunnels.append(valves[name])
            self.distances[name] = 1
        self.distances[self.name] = 0
        for x in self.distances:
            if self.distances[x] == None: self.distances[x] = 9999

    def findDistances(self):
        while True:
            change = False
            for x in self.distances:
                d = self.distances[x]
                if d == None: continue
                for e in valves[x].tunnels:
                    name = e.name
                    if self.distances[name] <= d + 1: continue
                    self.distances[name] = d + 1
                    valves[name].distances[self.name] = d + 1
                    change = True
            if not change: break

def followPath(path: List[str], time: int = 30) -> int:
    total = 0
    current = 0
    loc = 'AA'
    for n in path:
        if time == 0: break
        for _ in range(valves[loc].distances[n]):
            total += current
            time -= 1
            if time == 0: break
        if time == 0: break
        loc = n
        total += current
        current += valves[loc].pressure
        time -= 1
    if time > 0:
        for _ in range(time):
            total += current
    return total

def followPathPrinting(path: List[str], time: int = 30) -> int:
    total = 0
    current = 0
    loc = 'AA'
    for n in path:
        if time == 0: break
        for _ in range(valves[loc].distances[n]):
            total += current
            print('Minute: ' + str(30 - time) + ' moving to ' + n + ' flow rate is ' + str(current) + ' total is ' + str(total))
            time -= 1
            if time == 0: break
        if time == 0: break
        loc = n
        total += current
        print('Minute: ' + str(30 - time) + ' opening valve ' + n + ' flow rate is ' + str(current) + ' total is ' + str(total))
        current += valves[loc].pressure
        time -= 1
    if time > 0:
        for _ in range(time):
            total += current
            time -= 1
            print('Minute: ' + str(30 - time) + ' waiting at ' + n + ' flow rate is ' + str(current) + ' total is ' + str(total))
    return total


def partOne():
    turnableValves: List[str] = []
    for v in valves:
        if valves[v].pressure == 0: continue
        turnableValves.append(v)
    for _ in turnableValves:


def partTwo():
    pass

inputArray = inputString.splitlines()

for valve in inputArray:
    name = valve.split()[1]
    pressure = valve.split()[4][5:-1]
    valves[name] = Valve(name, int(pressure))
for valve in inputArray:
    name = valve.split()[1]
    tunnels = ''.join(valve.split()[9:]).split(',')
    valves[name].addTunnels(tunnels)

for v in valves:
    valves[v].findDistances()

print(partOne())

print(partTwo())
