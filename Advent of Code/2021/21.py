
# Started 2:17
# Finished 3:28

f = open('2021/21.txt', 'r')
inputString = f.read()
p1 = 1
p2 = 6
#p1 = 4
#p2 = 8
pr = [3,4,5,6,7,8,9]

def advancePos(pos, amount):
    pos += amount
    pos %= 10
    if pos == 0: pos = 10
    return pos

def advanceRound(gamestate):
    #gamestate = [p1, p2, s1, s2, (True, False)] True is p1 turn False is p2 turn
    p1 = gamestate[0]
    p2 = gamestate[1]
    s1 = gamestate[2]
    s2 = gamestate[3]
    turn = gamestate[4]
    if s1 >= 21: return {'1': 1, '2': 0}
    if s2 >= 21: return {'1': 0, '2': 1}
    universes = []
    if turn:
        p1 += 2
        for x in pr:
            p1 = advancePos(p1, 1)
            s1 += p1
            universes.append([p1, p2, s1, s2, False])
            s1 -= p1
    else:
        p2 += 2
        for x in pr:
            p2 = advancePos(p2, 1)
            s2 += p2
            universes.append([p1, p2, s1, s2, True])
            s2 -= p2
    un3 = advanceRound(universes[0])
    un4 = advanceRound(universes[1])
    un5 = advanceRound(universes[2])
    un6 = advanceRound(universes[3])
    un7 = advanceRound(universes[4])
    un8 = advanceRound(universes[5])
    un9 = advanceRound(universes[6])
    return {'1': un3['1'] + un4['1'] * 3 + un5['1'] * 6 + un6['1'] * 7 + un7['1'] * 6 + un8['1'] * 3 + un9['1'], '2': un3['2'] + un4['2'] * 3 + un5['2'] * 6 + un6['2'] * 7 + un7['2'] * 6 + un8['2'] * 3 + un9['2']}
    
def partOne(p1, p2):
    s1 = 0
    s2 = 0
    currentPlayer = True
    rollcount = 0
    currentroll = -1
    while s1 < 1000 and s2 < 1000:
        currentroll += 3
        roll = currentroll *3
        rollcount += 3
        if currentPlayer:
            p1 += roll
            p1 %= 10
            if p1 == 0: p1 = 10
            s1 += p1
            currentPlayer = False
        else:
            p2 += roll
            p2 %= 10
            if p2 == 0: p2 = 10
            s2 += p2
            currentPlayer = True
    if currentPlayer:
        result = s1 * rollcount
    else:
        result = s2 * rollcount
    return [s1, s2, rollcount, result]

def partTwo(p1, p2):
    multiverse = advanceRound([p1, p2, 0, 0, True])
    return [multiverse, max(multiverse)]

inputArray = inputString.splitlines()

print(partOne(p1, p2))

print(partTwo(p1, p2))
