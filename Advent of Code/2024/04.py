
# Started
# Finished

from asyncio.windows_events import NULL


f = open('2024/04.txt', 'r')
inputString = f.read()

#inputString = """MMMSXXMASM
#MSAMXMSMSA
#AMXSXMAAMM
#MSAMASMSMX
#XMASAMXAMM
#XXAMMXXAMA
#SMSMSASXSS
#SAXAMASAAA
#MAMMMXMMMM
#MXMXAXMASX"""

inputArray = inputString.splitlines()

gridH = len(inputArray)
gridW = len(inputArray[0])

goal = 'XMAS'

def lookaround(needle: str, grid: list[str], position: tuple[int], direction: tuple[int]) -> list[dict[str, tuple[int]]]:
    x = position[0] + direction[0]
    y = position[1] + direction[1]
    if direction != (0,0):
        if 0 <= x < gridW and 0 <= y < gridH and grid[y][x] == needle:
            return [{'position': (x, y), 'direction': direction}]
        else:
            return []
    founds = []
    for xdiff in [-1, 0, 1]:
        for ydiff in [-1, 0, 1]:
            if 0 <= x + xdiff < gridW and 0 <= y + ydiff < gridH:
                if grid[y + ydiff][x + xdiff] == needle:
                    founds.append({'position': (x + xdiff, y + ydiff), 'direction': (xdiff, ydiff)})
    return founds

def lookaroundD(needle: str, grid: list[str], position: tuple[int], direction: tuple[int]) -> list[dict[str, tuple[int]]]:
    x = position[0] + direction[0]
    y = position[1] + direction[1]
    if direction != (0,0):
        if 0 <= x < gridW and 0 <= y < gridH and grid[y][x] == needle:
            return [{'position': (x, y), 'direction': direction}]
        else:
            return []
    founds = []
    for xdiff in [-1, 1]:
        for ydiff in [-1, 1]:
            if 0 <= x + xdiff < gridW and 0 <= y + ydiff < gridH:
                if grid[y + ydiff][x + xdiff] == needle:
                    founds.append({'position': (x + xdiff, y + ydiff), 'direction': (xdiff, ydiff)})
    return founds
    

def partOne(i: list[str]):
    runningsum = 0
    for l in range(gridH):
        for c in range(gridW):
            if i[l][c] == 'X':
                Ms = lookaround('M', i, (c, l), (0, 0))
                for M in Ms:
                    As = lookaround('A', i, M['position'], M['direction'])
                    for A in As:
                        if len(lookaround('S', i, A['position'], A['direction'])) > 0:
                            runningsum += 1
    return runningsum

def partTwo(i):
    runningsum = 0
    for l in range(gridH):
        for c in range(gridW):
            if i[l][c] == 'M':
                As = lookaroundD('A', i, (c, l), (0, 0))
                for A in As:
                    if len(lookaround('S', i, A['position'], A['direction'])) == 0:
                        continue
                    crossdiagonal = [(A['direction'][0] * -1, A['direction'][1]), (A['direction'][0], A['direction'][1] * -1)]
                    M = [len(lookaround('M', i, A['position'], x)) for x in crossdiagonal]
                    S = [len(lookaround('S', i, A['position'], x)) for x in crossdiagonal]
                    if M == [0, 1] and S == [1, 0] or M == [1, 0] and S == [0, 1]:
                        runningsum += 1
    return runningsum / 2


print(partOne(inputArray))

print(partTwo(inputArray))
