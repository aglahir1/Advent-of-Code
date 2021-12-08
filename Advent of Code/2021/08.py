
# Started 06:37



f = open('2021/08.txt', 'r')
inputString = f.read()

#inputString = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
#edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
#fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
#fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
#aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
#fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
#dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
#bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
#egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
#gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

#inputString = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

inputArray = inputString.splitlines()

ins = []
outs = []

for i in inputArray:
    i = i.split(' | ')
    ins.append(i[0].split())
    outs.append(i[1].split())

count = 0
for o in outs:
    for x in o:
        if len(x) in (2, 4, 3, 7): count += 1


output = 0
for i in range(len(ins)):
    top = ''
    mid = ''
    bot = ''
    tr = ''
    tl = ''
    br = ''
    bl = ''
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixes = []
    sevens = []
    eights = ['a','b','c','d','e','f','g']
    nines = []
    zeros = []
    twoThreeFives = []
    zeroSixNines = []
    for x in ins[i]:
        if len(x) == 2:
            ones = list(x)
        elif len(x) == 3:
            sevens = list(x)
        elif len(x) == 4:
            fours = list(x)
        elif len(x) == 5:
            twoThreeFives.append(list(x))
        elif len(x) == 6:
            zeroSixNines.append(list(x))
    for x in zeroSixNines:
        if len(set(x) - set(sevens)) == 4:
            sixes = x
    tr = list(set(eights) - set(sixes))[0]
    br = list(set(ones) - set([tr]))[0]
    for x in twoThreeFives:
        if tr not in x:
            fives = x
        elif br not in x:
            twos = x
        else:
            threes = x
    tl = list(set(fours) - set(threes))[0]
    mid = list((set(fours) - set(ones))- set([tl]))[0]
    zeros = list(set(eights) - set([mid]))
    nines = fives + [tr]
    outputNumber = ''
    for x in outs[i]:
        if set(list(x)) == set(ones): outputNumber += '1'
        if set(list(x)) == set(twos): outputNumber += '2'
        if set(list(x)) == set(threes): outputNumber += '3'
        if set(list(x)) == set(fours): outputNumber += '4'
        if set(list(x)) == set(fives): outputNumber += '5'
        if set(list(x)) == set(sixes): outputNumber += '6'
        if set(list(x)) == set(sevens): outputNumber += '7'
        if set(list(x)) == set(eights): outputNumber += '8'
        if set(list(x)) == set(nines): outputNumber += '9'
        if set(list(x)) == set(zeros): outputNumber += '0'
    output += int(outputNumber)

print(output)