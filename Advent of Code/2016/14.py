
# Started
# Finished

from hashlib import md5

inputString = 'zpqevtbw'

# inputString = 'abc'

def checkquins(hash: str) -> set[str]:
    runningc: str = ''
    tally: int = 0
    quins: set[str] = set()
    for c in hash:
        if c == runningc:
            tally += 1
            if tally == 5:
                quins.add(c)
        else:
            tally = 1
            runningc = c
    return quins

def checktrips(hash: str) -> str:
    runningc: str = ''
    tally: int = 0
    for c in hash:
        if c == runningc:
            tally += 1
            if tally == 3:
                return c
        else:
            tally = 1
            runningc = c
    return ''
            
def fullhash(input: str, part: int) -> str:
    input = md5(str.encode(input)).hexdigest()
    if part == 2:
        for _ in range(2016):
            input = md5(str.encode(input)).hexdigest()
    return input

def parts(i, part: int):
    hashes = {}
    index = 0
    keys = []
    end = 'not found'
    while True:
        hash = fullhash(str(i) + str(index), part)
        quins = checkquins(hash)
        trips = checktrips(hash)
        if len(quins) > 0 or len(trips) > 0:
            hashes[index] = (hash, trips, quins)
        if len(quins) > 0:
            for x in range(index - 1000, index):
                if x in hashes and x not  in keys:
                    if hashes[x][1] in quins:
                        keys.append(x)
                        if len(keys) == 64 and end == 'not found': end = x + 1000
        index += 1
        if index == end:
            keys.sort()
            return keys[63]



print(parts(inputString, 1))

print(parts(inputString, 2))