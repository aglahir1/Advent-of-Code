
# Started 03:04
# Finished 03:25

import hashlib

f = open('2016/05.txt', 'r')
inputString = f.read()

inputString = 'ffykfhsq'

#inputString = 'abc'

def partOne(i):
    x = 0
    password = ''
    while len(password) < 8:
        hashable = i + str(x)
        hashed = hashlib.md5(hashable.encode())
        hexhash = hashed.hexdigest()
        if(hexhash[:5] == '00000'):
            password += str(hexhash[5])
        x += 1
    return password

def partTwo(i):
    x = 0
    password = 'xxxxxxxx'
    while 'x' in password:
        hashable = i + str(x)
        hashed = hashlib.md5(hashable.encode())
        hexhash = hashed.hexdigest()
        if hexhash[:5] == '00000' and hexhash[5] in ('0', '1', '2', '3', '4', '5', '6', '7') and password[int(hexhash[5])] == 'x':
            password = password[:int(hexhash[5])] + hexhash[6] + password[int(hexhash[5]) + 1:]
        x += 1
    return password

print(partOne(inputString))

print(partTwo(inputString))
