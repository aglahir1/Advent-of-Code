
import itertools

inputString = """Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127"""

#inputString = """London to Dublin = 464
#London to Belfast = 518
#Dublin to Belfast = 141"""

inputArray = inputString.splitlines()

cityArray = []

for entry in inputString.split():
    if not (entry == 'to' or entry == '=' or entry.isdecimal()):
        if entry not in cityArray: cityArray.append(entry)

cityConnections = []

for entry in inputArray:
    entry = entry.split()
    connection = [entry[0], entry[2]]
    connection.sort()
    cityConnections.append([connection, int(entry[4])])

print(cityConnections)

cityroutes = list(itertools.permutations(cityArray))
cityRoutesWithDistances = []

for route in cityroutes:
    route = list(route)
    routepairs = []
    for index in range(len(route)-1):
        pair = [route[index],route[index+1]]
        pair.sort()
        routepairs.append(pair)
    distance = 0
    for pair in routepairs:
        distance += cityConnections[[x[0] for x in cityConnections].index(pair)][1]
    cityRoutesWithDistances.append([route, distance])

for x in cityRoutesWithDistances:
    print(x)

print(max([x[1] for x in cityRoutesWithDistances]))