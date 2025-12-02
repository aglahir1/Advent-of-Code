
# Started
# Finished

f = open('2026/02.txt', 'r')
inputString = f.read()

# inputString = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def partOne(i):
    invalids = []
    for r in i:
        r = r.split('-')
        for idx in range(int(r[0]), int(r[1]) + 1):
            idx = str(idx)
            l = len(idx)
            if l % 2 == 1: continue
            if idx[:l//2] == idx[l//2:]: invalids.append(int(idx))
    return sum(invalids)
            

def partTwo(i):
    invalids = set()
    for r in i:
        r = r.split('-')
        for idx in range(int(r[0]), int(r[1]) + 1):
            idx = str(idx)
            l = len(idx)
            for j in range(1, l//2 + 1):
                if l % j != 0: continue
                cut = [idx[n:n+j] for n in range(0, l, j)]
                if all(cut[m] == cut[0] for m in range(len(cut))): 
                    invalids.add(int(idx))
                    break
    return sum(invalids)

inputArray = inputString.split(',')

print(partOne(inputArray))

print(partTwo(inputArray))
