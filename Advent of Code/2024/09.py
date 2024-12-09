
# Started
# Finished

f = open('2024/09.txt', 'r')
inputString = f.read()

# inputString = "2333133121414131402"

def partOne(i):
    drive = list(i)
    files = [{'number': n, 'size': x} for n, x in enumerate(drive[::2])]
    filled = sum(drive[::2])
    runningchecksum = 0
    driveidx = 0
    driveidxprog = 0
    emptySpace = False
    leftFile = 0
    emptyslots = []
    filledslots = 0
    for idx in range(filled):
        if driveidxprog == drive[driveidx]:
            driveidx += 1
            driveidxprog = 0
            emptySpace = not emptySpace
            if not emptySpace:
                leftFile += 1
        if drive[driveidx] == 0:
            driveidx += 1
            emptySpace = not emptySpace
            if not emptySpace:
                leftFile += 1
        if not emptySpace:
            runningchecksum += idx * files[leftFile]['number']
            filledslots += 1
        else:
            emptyslots.append(idx)
        driveidxprog += 1
    for f in files[::-1]:
        for _ in range(f['size']):
            if len(emptyslots) > 0:
                runningchecksum += emptyslots.pop(0) * f['number']
        if len(emptyslots) == 0:
            break
    return runningchecksum

def partTwo(i):
    drive = list(i)
    driveSize = sum(drive)
    fileness = True
    blocks = []
    driveidx = 0
    for idx, block in enumerate(drive):
        if block != 0: blocks.append({'file': fileness, 'fileNum': [0, idx // 2][fileness], 'start': driveidx, 'end': driveidx + block - 1})
        driveidx += block
        fileness = not fileness
    for x in range(len(drive[::2]))[::-1]:
        [file] = [f for f in blocks if f['fileNum'] == x and f['file'] == True]
        size = file['end'] - file['start'] + 1
        for b in blocks:
            if b['start'] > file['end']: continue
            if b['file']: continue
            space = b['end'] - b['start'] + 1
            if space < size: continue
            prestart = file['start']
            preend = file['end']
            file['start'] = b['start']
            if space == size:
                blocks.remove(b)
                file['end'] = b['end']
            else:
                b['start'] += size
                file['end'] = b['start'] - 1
            break
    runningchecksum = 0
    for b in blocks:
        if b['file']:
            runningchecksum += b['fileNum'] * sum(range(b['start'], b['end'] + 1))
    return runningchecksum
        
                
drive = map(int, list(inputString))

print(partOne(drive))

drive = map(int, list(inputString))

print(partTwo(drive))
