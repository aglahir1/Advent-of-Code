
#S 05:03
#F 05:45



f = open('2015/15.txt', 'r')
inputString = f.read()

#inputString = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

inputArray = inputString.splitlines()

ingredients = []

for entry in inputArray:
    entry = entry.split()
    ingredients.append([entry[0][:-1], int(entry[2][:-1]), int(entry[4][:-1]), int(entry[6][:-1]), int(entry[8][:-1]), int(entry[10])])

results = []

def calculateMixture(mixture):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingredient in mixture:
        x = ingredient[1]
        capacity += x * ingredient[0][1]
        durability += x * ingredient[0][2]
        flavor += x * ingredient[0][3]
        texture += x * ingredient[0][4]
        calories += x * ingredient[0][5]
    if capacity < 0: capacity = 0
    if durability < 0: durability = 0
    if flavor < 0: flavor = 0
    if texture < 0: texture = 0
    results.append([mixture, capacity * durability * flavor * texture, calories])

def forIngredient(precedingIngredients, remainingIngredients, amountLeft):
    if len(remainingIngredients) == 1: 
        precedingIngredients.append([remainingIngredients[0], amountLeft])
        calculateMixture(precedingIngredients)
    else:
        precedingIngredients.append([remainingIngredients[0], 0])
        for n in range(amountLeft + 1):
            precedingIngredients[-1][1] = n
            forIngredient(precedingIngredients[:], remainingIngredients[1:], amountLeft - n)

forIngredient([], ingredients, 100)
actualResults = []
for result in results:
    if result[2] == 500: actualResults.append(result[:])

print(max(actualResults, key = lambda x: x[1]))

