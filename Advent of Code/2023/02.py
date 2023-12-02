
# Started
# Finished

f = open('2023/02.txt', 'r')
inputString = f.read()
testString = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

class Game:
    def __init__(self, id: int):
        self.id = id
        self.minRed = 0
        self.minBlue = 0
        self.minGreen = 0

    def draw(self, r, g, b):
        if r > self.minRed: self.minRed = r
        if g > self.minGreen: self.minGreen = g
        if b > self.minBlue: self.minBlue = b

    def getMin(self):
        return self.minRed + self.minBlue + self.minGreen

    def getPower(self):
        return self.minRed * self.minBlue * self.minGreen

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Game {self.id} has at least {self.minRed} red cubes, {self.minGreen} green cubes, and {self.minBlue} blue cubes.'

def partOne(i: list[Game]):
    runningSum = 0
    for game in i:
        if game.minRed <= 12 and game.minGreen <= 13 and game.minBlue <= 14:
            runningSum += game.id
    return runningSum

def partTwo(i):
    runningSum = 0
    for game in i:
        runningSum += game.getPower()
    return runningSum


def parseInput(inputString: str):
    inputArray: list[str] = inputString.splitlines()
    games: list[Game] = []
    for line in inputArray:
        line = line.split(': ')
        game = Game(int(line[0].split()[1]))
        for draw in line[1].split('; '):
            cubes = draw.split(', ')
            cubes = {y: int(x) for [x, y] in [z.split() for z in cubes]}
            game.draw(cubes.get('red', 0), cubes.get('green', 0), cubes.get('blue', 0))
        games.append(game)
    return games


print(partOne(parseInput(inputString)))

print(partTwo(parseInput(inputString)))
