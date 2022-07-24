
# Started 14:20
# Finished 15:03

f = open('2016/10.txt', 'r')
inputString = f.read()

bots = {}
outputs = {}

class Bot:
    def __init__(self, id, lowInstruction, highInstruction):
        self.id = id
        self.lowInstruction = lowInstruction # [bot(T) or output(F), id]
        self.highInstruction = highInstruction
        self.chips = []

    def gainChip(self, val):
        self.chips += [val]
        if len(self.chips) == 2:
            self.chips.sort()
            #partOne
            if self.chips == [17,61]: print('bot that compares 17 and 61: ' + str(self))
            if self.lowInstruction[0]:
                bots[self.lowInstruction[1]].gainChip(self.chips[0])
            else:
                outputs[self.lowInstruction[1]]+=[self.chips[0]]
            if self.highInstruction[0]:
                bots[self.highInstruction[1]].gainChip(self.chips[1])
            else:
                outputs[self.highInstruction[1]]+=[self.chips[1]]
            self.chips = []

    def __str__(self):
        return 'bot #' + self.id

inputArray = inputString.splitlines()
inputs = []
for x in inputArray:
    x = x.split()
    if x[0] == 'value':
        inputs += [[x[1],x[-1]]] #[val, bot]
        continue
    bots[x[1]] = Bot(x[1], [x[5]=='bot', x[6]], [x[10]=='bot', x[11]])
    if x[5] == 'output':
        if x[6] not in outputs: outputs[x[6]] = []
    if x[10] == 'output':
        if x[11] not in outputs: outputs[x[11]] = []

for j in inputs:
    bots[j[1]].gainChip(int(j[0]))

#partTwo
print(outputs['0'][0]*outputs['1'][0]*outputs['2'][0])
