from collections import Counter
from functools import cmp_to_key, reduce

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cardsr = reversed(cards)
card_points = {k: v for k, v in zip(cards, reversed(range(len(cards))))}

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    hands, bids = [], []
    for l in lines:
        ll = l.split(" ")
        hands.append(ll[0])
        bids.append(ll[1])

    return hands, bids

def hand_strength(hand):
    c = tuple(reversed(sorted(Counter(hand).values())))
    points = [card_points[c] for c in hand]
    if c == (5, ):
        return (6, points, )
    if c == (4, 1):
        return (5, points, )
    if c == (3, 2):
        return (4, points, )
    if c == (3, 1, 1):
        return (3, points, )
    if c == (2, 2, 1):
        return (2, points, )
    if c == (2, 1, 1, 1):
        return (1, points, )
    
    return (0, points)

def hand_strength2(hand):
    strength = hand_strength(hand=hand)
    jpos = []
    for i in range(len(hand)):
        if hand[i] == "J":
            jpos.append(i)
    if jpos:
        new_hand = list(hand)
        for j in jpos:
            for card in cards:
                new_hand[j] = card
                new_strength = hand_strength("".join(new_hand))
                if new_strength > strength:
                    strength = new_strength
        for card in cards:
            new_hand = hand.replace("J", card)
            new_strength = hand_strength(new_hand)
            if new_strength > strength:
                strength = new_strength

    return strength

def solve_1(hands, bids):
    hands = [(h, int(b),) for h, b in zip(hands, bids,)]
    hands.sort(key=lambda play: hand_strength(play[0]))

    total = 0
    for i in range(len(hands)):
        hand, bid = hands[i]
        rank = i + 1
        winning = rank * bid
        print(hand, rank, bid, winning)
        total += winning
    print(total)

def solve_2(hands, bids):
    hands = [(h, int(b),) for h, b in zip(hands, bids,)]
    hands.sort(key=lambda play: hand_strength2(play[0]))

    total = 0
    for i in range(len(hands)):
        hand, bid = hands[i]
        rank = i + 1
        winning = rank * bid
        print(hand, rank, bid, winning)
        total += winning
    print(total)

DAY = 7
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

hands, bids = read_file(filename)

# solve_1(hands, bids)
solve_2(hands, bids)



