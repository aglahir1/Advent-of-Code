
# Started
# Finished


input = '10111011111001111'
disksize = 272


def step(a: str) -> str:
    length = len(a)
    b = a[::-1]
    b = (1 << length) - 1 - int(b, 2)
    return a + '0' + str(bin(b))[2:].zfill(length)

def checksum(data: str) -> str:
    result = ''
    for x in zip(data[0::2], data[1::2]):
        if x[0] == x[1]:
            result += '1'
        else: 
            result += '0'
    return result


def partOne(i,d):
    data = i
    while len(data) < d:
        data = step(data)
    result = checksum(data[:d])
    while len(result) % 2 == 0:
        result = checksum(result)
    return result




print(partOne(input, 272))

print(partOne(input, 35651584))
