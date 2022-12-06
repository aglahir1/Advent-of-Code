
# Started
# Finished

f = open('2022/06.txt', 'r')
inputString = f.read()

#inputString = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
#inputString = "bvwbjplbgvbhsrlpgdmjqwftvncz"
#inputString = "nppdvjthqldpwncqszvftbrmjlhg"
#inputString = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
#inputString = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def partOne(i):
    for x, c in enumerate(i):
        if x < 4: continue
        if len(set(i[x-4:x])) == 4: return x

def partTwo(i):
    for x, c in enumerate(i):
        if x < 14: continue
        if len(set(i[x-14:x])) == 14: return x

print(partOne(inputString))

print(partTwo(inputString))
