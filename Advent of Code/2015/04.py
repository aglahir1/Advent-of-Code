import hashlib

i = "bgvyzdsv"
x = 0
while True:
    hashable = i + str(x)
    hashed = hashlib.md5(hashable.encode())
    hexhash = hashed.hexdigest()
    if(hexhash[:6] == '000000'):
        break
    x += 1
print(x)