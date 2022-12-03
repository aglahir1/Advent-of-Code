
# Started 11:13
# Finished 11:24

f = open('2022/02.txt', 'r')
inputString = f.read()

#inputString = """A Y
#B X
#C Z"""

global points
global winning
global losing

points = {'X': 1, 'Y': 2, 'Z': 3}
winning = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
losing = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}

def calculateTotalscore(rs):
    totalscore = 0
    for r in rs:
        score = points[r[1]]
        if r[0] == r[1]: score += 3
        if winning[r[0]] == r[1]: score += 6
        totalscore += score
    return totalscore



def partOne(i):
    return calculateTotalscore(i)
        

def partTwo(i):
    games = []
    for r in i:
        if r[1] == 'X': r[1] = losing[r[0]]
        elif r[1] == 'Y': r[1] = r[0]
        else: r[1] = winning[r[0]]
        games.append(r)
    return calculateTotalscore(games)

inputArray = inputString.splitlines()

rounds = []
equiv = {'A': 'X', 'B': 'Y', 'C': 'Z'}

for round in inputArray:
    round = round.split(' ')
    round[0] = equiv[round[0]]
    rounds.append(round)

print(partOne(rounds))

print(partTwo(rounds))
