
# Started
# Finished

f = open('2016/09.txt', 'r')
inputString = f.read()

def deflatedLength(string):
    if string.find('(') == -1: return len(string)
    count = 0
    while string.find('(') != -1:
        pre, post = string.split('(', 1)
        count += len(pre)
        markerString, post = post.split(')', 1)
        marker = list(map(int,markerString.split('x')))
        count += marker[1] * deflatedLength(post[:marker[0]])
        string = post[marker[0]:]
    return count


def partOne(inputString):
    deflatedSize = 0
    while inputString.find('(') != -1:
        pre, post = inputString.split('(', 1)
        deflatedSize += len(pre)
        markerString, post = post.split(')', 1)
        marker = list(map(int,markerString.split('x')))
        #deflatedSize += deflatedLength(marker, post[:marker[0]], False)
        inputString = post[marker[0]:]
    return deflatedSize

def partTwo(inputString):
    return deflatedLength(inputString)


#print(partOne(inputString))

print(partTwo(inputString))
