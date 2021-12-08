
# Started 20:40
#

import math
import itertools

player = {'health': 100, 'damage': 0, 'armor': 0}
boss = {'health': 100, 'damage': 8, 'armor': 2}

def calculateWin(b, p):
    damageToPlayer = b['damage'] - p['armor']
    damageToBoss = p['damage'] - b['armor']
    if damageToPlayer < 1: damageToPlayer = 1
    if damageToBoss < 1: damageToBoss = 1
    turnsToKillPlayer = math.ceil(p['health'] / damageToPlayer)
    turnsToKillBoss = math.ceil(b['health'] / damageToBoss)
    if turnsToKillPlayer < turnsToKillBoss: return True
    return False

weapons = [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]]
armor = [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

possibleRingCombos = [[0, 0, 0]] + rings[:]
possibleTwoRingCombos = list(itertools.permutations(rings, 2))

for x in possibleTwoRingCombos:
    x = list(x)
    possibleRingCombos += [[x[0][0] + x[1][0], x[0][1] + x[1][1], x[0][2] + x[1][2]]]

possibleRingCombos.sort()
rings = list(k for k,_ in itertools.groupby(possibleRingCombos))

equipments = []

for x in weapons:
    for y in armor:
        for z in rings:
            cost = x[0] + y[0] + z[0]
            damage = x[1] + z[1]
            defense = y[1] + z[2]
            equipments.append([cost, damage, defense])
equipments.sort()
finalequipments = list(k for k,_ in itertools.groupby(equipments))
successes = []
for e in finalequipments:
    player['damage'] = e[1]
    player['armor'] = e[2]
    if calculateWin(boss, player): successes.append(e)

successes.sort(key = lambda x: x[0], reverse = True)
print(successes[0])