
# Started
# Finished

from typing import Dict

inputString = '1,0,18,10,19,6'
#inputString = '0,3,6'

class Number:
    name: int
    last_spoken: int
    before_last_spoken: int

    def __init__(self, name, turn):
        self.name = name
        self.last_spoken = turn

    def __repr__(self):
        returnString = 'number ' + str(self.name) + ' was last spoken on turn ' + str(self.last_spoken)
        return returnString

    def speak(self, turn):
        self.before_last_spoken = self.last_spoken
        self.last_spoken = turn


numbers: Dict[int, Number] = dict()

def partOne(i):
    turn = 1
    spoken_nums = []
    last_spoken: int
    for n in i:
        numbers[n] = Number(n, turn)
        last_spoken = n
        turn += 1
    while turn < 30000001:
        subject = last_spoken
        if hasattr(numbers[subject], 'before_last_spoken'):
            speak = turn - numbers[subject].before_last_spoken - 1
        else: 
            speak = 0
        if speak in numbers.keys(): numbers[speak].speak(turn)
        else: numbers[speak] = Number(speak, turn)
        last_spoken = speak
        turn += 1
    return last_spoken

def partTwo(i):
    pass

inputArray = [int(x) for x in inputString.split(',')]

print(partOne(inputArray))

print(partTwo(inputArray))
