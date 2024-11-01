
# Started 15:45
# Finished

from copy import deepcopy


startingSitu = [
    [('Elerium', True), ('Elerium', False), ('Dilithium', True), ('Dilithium', False), ('Thulium', True), ('Thulium', False), ('Plutonium', True), ('Strontium', True)],
    [('Plutonium', False), ('Strontium', False)],
    [('Promethium', True), ('Promethium', False), ('Ruthenium', True), ('Ruthenium', False)],
    []
    ]

goalState = '3,,,PPPPPPP,'

testSitu = [
    [('Hydrogen', False), ('Lithium', False)],
    [('Hydrogen', True)],
    [('Lithium', True)],
    []
    ]

global passes 
passes = 0

# goalState = '3,,,PP,'

def statify(situ: list[list[tuple[str,bool]]], currentStep: int, currentElevator: int) -> tuple[str, int]:
    state = str(currentElevator)
    for floor in situ:
        flstr = []
        onlyElems = [x[0] for x in floor]
        counted = []
        for item in floor:
            if item[0] in counted:
                continue
            if onlyElems.count(item[0]) == 2:
                flstr += 'P'
            elif item[1]:
                flstr += 'G'
            else:
                flstr += 'M'
            counted.append(item[0])
        state += ''.join(sorted(flstr)) + ','
    return (state, currentStep, currentElevator)

def isValidState(state: str) -> bool:
    isValid = True
    for floor in state.split(','):
        if 'M' in floor:
            if 'P' in floor or 'G' in floor:
                isValid = False
    return isValid

def moveElevator(oldSitu: list[list[tuple[str,bool]]], currentElevator: int, movingUp: bool, takingItems: list[tuple[str,bool]]) -> list[list[tuple[str,bool]]]:
    newSitu = deepcopy(oldSitu)
    for i in takingItems:
        newSitu[currentElevator].remove(i)
        newSitu[currentElevator + [-1, 1][movingUp]].append(i)
    return newSitu

def makeAllCombos(availableItems: list[tuple[str,bool]]) -> list[list[tuple[str,bool]]]:
    combos = []
    for i in range(len(availableItems)):
        combos.append([availableItems[i]])
        for a in range(i + 1, len(availableItems)):
            combos.append([availableItems[i], availableItems[a]])
    return combos

def movingDecisions(visitedStates: dict[str, int], situ: list[list[tuple[str,bool]]], currentElevator: int, currentStep: int, currentLowest: int) -> tuple[int, list[str]]:
    currentStep += 1
    global passes
    passes += 1
    if passes % 1000 == 0: print([passes, currentLowest])
    if currentStep == currentLowest: return (currentLowest, visitedStates)
    combos = makeAllCombos(situ[currentElevator])
    toSearch = []
    for itemset in combos:
        if currentElevator != 3:
            newSitu = deepcopy(moveElevator(situ, currentElevator, True, itemset))
            newState = statify(newSitu, currentStep, currentElevator + 1)
            if newState[0] == goalState: 
                visitedStates[goalState] = currentStep
                return (currentStep, visitedStates)
            toSearch.append((newState, newSitu, True))
        if currentElevator != 0:
            newSitu = deepcopy(moveElevator(situ, currentElevator, False, itemset))
            newState = statify(newSitu, currentStep, currentElevator - 1)
            if newState[0] == goalState: 
                visitedStates[goalState] = currentStep
                return (currentStep, visitedStates)
            toSearch.append((newState, newSitu, False))
    for x in toSearch:
        if not isValidState(x[0][0]): continue
        if x[0][0] in visitedStates.keys():
            if visitedStates[x[0][0]] <= x[0][1]: continue
        visitedStates[x[0][0]] = x[0][1]
        newTree = movingDecisions(visitedStates, x[1], currentElevator + [-1, 1][x[2]], currentStep, currentLowest)
        if newTree[0] < currentLowest: currentLowest = newTree[0]
        visitedStates = newTree[1]
    return (currentLowest, visitedStates)
            

def partOne():
    result = movingDecisions({statify(startingSitu, 0, 0)[0]: 0}, startingSitu, 0, 0, 60)
    if goalState in result[1]:
        return 'success! step count: ' + str(result[0])
    else: return 'failed'

def partTwo():
    pass

print(partOne())

print(partTwo())
