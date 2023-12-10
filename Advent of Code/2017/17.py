
# Started
# Finished

inputString = 335

def partOne(i):
    spinlock = [0]
    position = 0
    for x in range(1, 2018):
        position += i
        position %= len(spinlock)
        spinlock.insert(position + 1, x)
        position += 1
    return spinlock[(position + 1) % len(spinlock)]

def partTwo(i):
    spinlock = [0]
    position = 0
    for x in range(1, 50000000):
        position += i
        position %= x
        if position == 0:
            spinlock.insert(1, x)
        position += 1
    return spinlock[1]

print(partOne(inputString))

print(partTwo(inputString))
