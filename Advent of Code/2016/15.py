
# Started
# Finished

inputArray = [
    (1, 13, 11),
    (2, 5, 0),
    (3, 17, 11),
    (4, 3, 0),
    (5, 7, 2),
    (6, 19, 17)
    ]

# inputArray = [
#     (1, 5, 4),
#     (2, 2, 1),
#     ]

def partOne(i):
    positions = []
    for x in i:
        positions.append(((x[2] + x[0]) % x[1], x[1]))
    check = 0
    while True:
        launched = False
        for p in positions:
            if (p[0] + check) % p[1] != 0:
                launched = True
                break
        if not launched:
            return check
        check += 1

def partTwo(i):
    pass



print(partOne(inputArray))

print(partOne(inputArray + [(7, 11, 0)]))
