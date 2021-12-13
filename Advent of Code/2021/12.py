
# Started 22:20
# Finished 23:08

import itertools

f = open('2021/12.txt', 'r')
inputString = f.read()

#inputString = """fs-end
#he-DX
#fs-he
#start-DX
#pj-DX
#end-zg
#zg-sl
#zg-pj
#pj-he
#RW-he
#fs-DX
#pj-RW
#zg-RW
#start-pj
#he-WI
#zg-he
#pj-fs
#start-RW"""

#inputString = """dc-end
#HN-start
#start-kj
#dc-start
#dc-HN
#LN-dc
#HN-end
#kj-sa
#kj-HN
#kj-dc"""

#inputString = """start-A
#start-b
#A-c
#A-b
#b-d
#A-end
#b-end"""

class cave:
    def __init__(self, name):
        self.name = name
        self.passes = 0
        self.connections = []
        self.small = name.islower()

    def __str__(self):
        string = self.name + " is a " + ("large", "small")[self.small] + " cave with connections to "
        for x in self.connections:
            string += x.name + " "
        return string

def explore(currentRoute, caves):
    routes = []
    connections = caves[[x.name for x in caves].index(currentRoute[-1])].connections
    for x in connections:
        route = currentRoute[:]
        if x.name in route and x.small:
            continue
        route.append(x.name)
        if route[-1] == 'end':
            routes.append(route)
            continue
        routes += explore(route, caves)
    routes.sort()
    endresult = list(k for k,_ in itertools.groupby(routes))
    return endresult

def exploreMore(currentRoute, caves):
    routes = []
    connections = caves[[x.name for x in caves].index(currentRoute[-1])].connections
    for x in connections:
        route = currentRoute[:]
        if x.name == 'start':
            continue
        if route.count(x.name) > 0 and x.small:
            if route[0]:
                continue
            route[0] = True
        route.append(x.name)
        if route[-1] == 'end':
            routes.append(route)
            continue
        routes += exploreMore(route, caves)
    routes.sort()
    endresult = list(k for k,_ in itertools.groupby(routes))
    return endresult


def partOne(i):
    caves = []
    for entry in i:
        entry = entry.split('-')
        if entry[0] not in [x.name for x in caves]:
            caves.append(cave(entry[0]))
        if entry[1] not in [x.name for x in caves]:
            caves.append(cave(entry[1]))
        caves[[x.name for x in caves].index(entry[0])].connections.append(caves[[x.name for x in caves].index(entry[1])])
        caves[[x.name for x in caves].index(entry[1])].connections.append(caves[[x.name for x in caves].index(entry[0])])

    possibleRoutes = []
    pos = 'start'

    possibleRoutes += explore([pos], caves)
    
    return len(possibleRoutes)

    

def partTwo(i):
    caves = []
    for entry in i:
        entry = entry.split('-')
        if entry[0] not in [x.name for x in caves]:
            caves.append(cave(entry[0]))
        if entry[1] not in [x.name for x in caves]:
            caves.append(cave(entry[1]))
        caves[[x.name for x in caves].index(entry[0])].connections.append(caves[[x.name for x in caves].index(entry[1])])
        caves[[x.name for x in caves].index(entry[1])].connections.append(caves[[x.name for x in caves].index(entry[0])])

    possibleRoutes = []
    pos = 'start'

    possibleRoutes += exploreMore([False, pos], caves)
    
    return len(possibleRoutes)

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))