
# Started
# Finished

f = open('2023/07.txt', 'r')
inputString = f.read()

# inputString = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

cardrankpartone = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
cardrank = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

class Hand:
    def __init__(self, cards, bid, joker):
        self.cards = cards
        self.joker = joker
        if joker:
            cards = ''.join(cards)
            if cards == 'JJJJJ': cards = 'KKKKK'
            mc = max(set(list(cards.replace('J', ''))), key = cards.count)
            cards = cards.replace('J', mc)
            cards = list(cards)
        cards = sorted(cards)
        self.bid = bid
        if len(set(cards)) == 1:
            self.rank = 6
        elif cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4:
            self.rank = 5
        elif (cards.count(cards[0]) == 3 and cards.count(cards[3]) == 2) or (cards.count(cards[0]) == 2 and cards.count(cards[2]) == 3):
            self.rank = 4
        elif cards.count(cards[0]) == 3 or cards.count(cards[1]) == 3 or cards.count(cards[2]) == 3:
            self.rank = 3
        elif (cards.count(cards[0]) == 2 and (cards.count(cards[2]) == 2 or cards.count(cards[3]) == 2)) or (cards.count(cards[1]) == 2 and cards.count(cards[3]) == 2):
            self.rank = 2
        elif cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2 or cards.count(cards[2]) == 2 or cards.count(cards[3]) == 2:
            self.rank = 1
        else:
            self.rank = 0
        
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        for c in range(5):
            if self.cards[c] == other.cards[c]: continue
            if self.joker:
                return cardrank[self.cards[c]] < cardrank[other.cards[c]]
            return cardrankpartone[self.cards[c]] < cardrankpartone[other.cards[c]]
        
    def __gt__(self, other):
        if self.rank != other.rank:
            return self.rank > other.rank
        for c in range(5):
            if self.cards[c] == other.cards[c]: continue
            if self.joker:
                return cardrank[self.cards[c]] > cardrank[other.cards[c]]
            return cardrankpartone[self.cards[c]] > cardrankpartone[other.cards[c]]
        
    def __repr__(self):
        return f'cards: {"".join(self.cards)}; bid: {self.bid}'
        
        

def partOne(i):
    hands = []
    runningSum = 0
    for hand in i:
        cards = list(hand[0])
        hands.append(Hand(cards, int(hand[1]), False))
    hands = sorted(hands)
    for x, h in enumerate(hands):
        runningSum += (h.bid * (x + 1))
    return runningSum
    
            

def partTwo(i):
    hands = []
    runningSum = 0
    for hand in i:
        cards = list(hand[0])
        hands.append(Hand(cards, int(hand[1]), True))
    hands = sorted(hands)
    for x, h in enumerate(hands):
        runningSum += (h.bid * (x + 1))
    return runningSum
    
inputArray = [x.split() for x in inputString.splitlines()]

print(partOne(inputArray))

print(partTwo(inputArray))
