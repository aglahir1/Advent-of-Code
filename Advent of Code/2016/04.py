
# Started 17:18
# Finished 17:47

f = open('2016/04.txt', 'r')
inputString = f.read()

#inputString = """aaaaa-bbb-z-y-x-123[abxyz]
#a-b-c-d-e-f-g-h-987[abcde]
#not-a-real-room-404[oarel]
#totally-real-room-200[decoy]"""

def partOne(i):
    rooms = []
    for entry in i:
        entry = entry.split('-')
        rooms.append([''.join(entry[:-1]), entry[-1].split('[')[0], entry[-1][:-1].split('[')[1]])
    realRooms = []
    for room in rooms:
        letters = []
        for c in room[0]:
            if c in [x[0] for x in letters]:
                letters[[x[0] for x in letters].index(c)][1] += 1
            else: letters.append([c, 1])
        letters.sort(key = lambda x: (-x[1], x[0]))
        if ''.join([x[0] for x in letters[:5]]) == room[2]:
            realRooms.append(room[:])
    return sum([int(x[1]) for x in realRooms])


def partTwo(i):
    rooms = []
    for entry in i:
        entry = entry.split('-')
        rooms.append([''.join(entry[:-1]), entry[-1].split('[')[0], entry[-1][:-1].split('[')[1]])
    realRooms = []
    for room in rooms:
        letters = []
        for c in room[0]:
            if c in [x[0] for x in letters]:
                letters[[x[0] for x in letters].index(c)][1] += 1
            else: letters.append([c, 1])
        letters.sort(key = lambda x: (-x[1], x[0]))
        if ''.join([x[0] for x in letters[:5]]) == room[2]:
            realRooms.append(room[:])
    northRooms = []
    for i, room in enumerate(realRooms):
        shift = int(room[1])
        roomname = ''
        for x in room[0]:
            c = chr((ord(x) + shift - 97) % 26 + 97)
            roomname += c
        if 'north' in roomname:
            northRooms.append([roomname, room[1]])
    return northRooms

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
