
# Started 23:26
# Finished 01:35
#P2 correct commands ['P', 'R', 'S', 'P', 'R', 'D', 'P', 'D', 'M']
#P2 correct commands ['P', 'R', 'S', 'P', 'D', 'R', 'P', 'D', 'M']

import math

bossHealth = 55
bossDamage = 8

playerHealth = 50
playerArmour = 0
mana = 500
manaSpent = 0

mmCost = 53
mmDamage = 4

sCost = 113
sArmour = 7
sDuration = 6
sRemaining = 0

pCost = 173
pDamage = 3
pDuration = 6
pRemaining = 0

rCost = 229
rDuration = 5
rAmount = 101
rRemaining = 0

def timeToLive(armour, health, damage):
    damage = damage - armour
    if damage < 1: damage = 1
    return math.ceil(health / damage)

commands = []

while bossHealth > 0:
    print('-- Player turn --')
    playerHealth -= 1
    if playerHealth < 1:
        print('DEATH')
        break
    print('- Player has ' + str(playerHealth) + ' hit points, ' + str(playerArmour) + ' armour, ' + str(mana) + ' mana')
    print('- Boss has ' + str(bossHealth) + ' hit points')
    if sRemaining > 0:
        sRemaining -= 1
        print('Shield\'s timer is now ' + str(sRemaining) + '.')
        if sRemaining == 0:
            print('Shield wears off, decreasing armour by 7')
            playerArmour -= sArmour
    if pRemaining > 0:
        pRemaining -= 1
        bossHealth -= pDamage
        if bossHealth < 1:
            print('Poison deals ' + str(pDamage) + ' damage. This kills the boss, and the player wins.')
            break
        print('Poison deals ' + str(pDamage) + ' damage; its timer is now ' + str(pRemaining) + '.')
        if pRemaining == 0:
            print('Poison wears off.')
    if rRemaining > 0:
        rRemaining -= 1
        mana += rAmount
        print('Recharge provides ' + str(rAmount) + ' mana; its timer is now ' + str(rRemaining) + '.')
        if rRemaining == 0:
            print('Recharge wears off.')
    print('turnsRemaining: ' + str(((bossHealth - (pRemaining * pDamage)) / mmDamage) + pRemaining))


    print('1:R, 2:S, 3:P, 4:D, 5:M')
    x = int(input())
    

    if x == 1: #rRemaining < 1 and mana >= rCost and timeToLive(0, bossHealth, 4) > mana / mmCost:
        manaSpent += rCost
        mana -= rCost
        rRemaining = rDuration
        print('Player casts Recharge.')
        commands.append('R')
    elif x == 2: #sRemaining < 1 and mana >= sCost and timeToLive(0, playerHealth, bossDamage + 1) < timeToLive(0, bossHealth, 7):
        manaSpent += sCost
        mana -= sCost
        sRemaining = sDuration
        playerArmour += sArmour
        commands.append('S')
        print('Player casts Shield, increasing armour by ' + str(sArmour) + '.')
    elif x == 3: #pRemaining < 1 and mana >= pCost and timeToLive(0, bossHealth, 4) > 4:
        manaSpent += pCost
        mana -= pCost
        pRemaining = pDuration
        print('Player casts Poison')
        commands.append('P')
    elif x == 4: #playerHealth <= bossDamage + 1 - playerArmour and mana >= 73 and bossHealth > 4 + pDamage * (0, 1)[bool(pRemaining)]:
        bossHealth -= 2
        manaSpent += 73
        playerHealth += 2
        mana -= 73
        commands.append('D')
        if bossHealth < 1:
            print('drain. This kills the boss, and the player wins.')
            break
        print('drain')
    elif x == 5: #mana > mmCost:
        manaSpent += mmCost
        mana -= mmCost
        bossHealth -= mmDamage
        commands.append('M')
        if bossHealth < 1:
            print('Player casts Magic Missile, dealing ' + str(mmDamage) + ' damage. This kills the boss, and the player wins.')
            break
        print('Player casts Magic Missile, dealing ' + str(mmDamage) + ' damage.')
    elif pDuration < 1:
        print('Player has run out of mana')
        break
    print()

    print('-- Boss turn --')
    print('- Player has ' + str(playerHealth) + ' hit points, ' + str(playerArmour) + ' armour, ' + str(mana) + ' mana')
    print('- Boss has ' + str(bossHealth) + ' hit points')
    if sRemaining > 0:
        sRemaining -= 1
        print('Shield\'s timer is now ' + str(sRemaining) + '.')
        if sRemaining == 0:
            print('Shield wears off, decreasing armour by 7')
            playerArmour -= sArmour
    if pRemaining > 0:
        pRemaining -= 1
        bossHealth -= pDamage
        if bossHealth < 1:
            print('Poison deals ' + str(pDamage) + ' damage. This kills the boss, and the player wins.')
            break
        print('Poison deals ' + str(pDamage) + ' damage; its timer is now ' + str(pRemaining) + '.')
        if pRemaining == 0:
            print('Poison wears off.')
    if rRemaining > 0:
        rRemaining -= 1
        mana += rAmount
        print('Recharge provides ' + str(rAmount) + ' mana; its timer is now ' + str(rRemaining) + '.')
        if rRemaining == 0:
            print('Recharge wears off.')

    if playerArmour > 0:
        playerHealth -= (bossDamage - playerArmour)
        print('Boss attacks for ' + str(bossDamage) + ' - ' + str(playerArmour) + ' = ' + str(bossDamage - playerArmour) + ' damage!')
    else:
        playerHealth -= bossDamage
        print('Boss attacks for ' + str(bossDamage) + ' damage!')

    if playerHealth < 1:
        print('DEATH')
        break
    print()

print('spent mana: ' + str(manaSpent))
print('commands: ', end= '')
print(commands)