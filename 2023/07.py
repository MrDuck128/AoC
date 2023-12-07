from collections import Counter

with open('07.txt') as f:
    data = f.read().splitlines()

m = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def sortDicts(hand):
    return sorted(list(Counter(hand).values()), reverse=True), [m[x] for x in hand]

hands = [(hand, int(bid)) for hand, bid in [line.split() for line in data]]
hands = sorted(hands, key=lambda x: sortDicts(x[0]))

winnings = 0
for i, (_, bid) in enumerate(hands):
    winnings += (i+1) * bid
print('Part 1:', winnings)

m['J'] = 1

def sortDicts2(hand):
    mostCommon = 'J'
    for (c, _) in Counter(hand).most_common():
        if c != 'J':
            mostCommon = c
            break
        
    hand2 = hand.replace('J', mostCommon)
    return sorted(list(Counter(hand2).values()), reverse=True), [m[x] for x in hand]

hands = sorted(hands, key=lambda x: sortDicts2(x[0]))

winnings = 0
for i, (_, bid) in enumerate(hands):
    winnings += (i+1) * bid
print('Part 2:', winnings)