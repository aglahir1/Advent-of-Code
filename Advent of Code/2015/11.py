
import re

inputString ="vzbxkghb"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def tripwise(s):
    result = []
    for a in range(len(s)-2):
        result.append(s[a] + s[a+1] + s[a+2])
    return result

def increment(s):
    result = ''
    s = s[::-1]
    for i, x in enumerate(s):
        if x != 'z':
            result += alphabet[alphabet.index(x)+1]
            break
        else: result += 'a'
    s = result + s[len(result):]
    s = s[::-1]
    return s

def test1(s):
    return any(i in tripwise(s) for i in tripwise(alphabet))

def test2(s):
    return not(any(i in s for i in 'iol'))

def test3(s):
    regex = re.compile(r'(.)\1.*?(.)\2')
    match = []
    matchGroups =[]
    for i in range(len(s)):
        match.append(regex.search(s[i:]))
    for x in match:
        if x:
            if x.group(1) != x.group(2):
                return True
    return False

def nextPassword(s):
    while (not(test1(s) and test2(s) and test3(s))):
        s = increment(s)
    return s

print(nextPassword(increment(nextPassword(inputString))))