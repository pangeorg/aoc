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

def hand_to_counts(hand):
    from collections import defaultdict

    assert len(hand) == 5

    counts = defaultdict(lambda : 0)
    for card in hand:
        counts[card] += 1
    return counts

def five_of_a_kind(counts):
    return len(counts.keys()) == 1

def four_of_a_kind(counts):
    return len(counts.keys()) == 2

def full_house(counts):
    return list(sorted(counts.values())) == [2, 3]

def three_of_a_kind(counts):
    return list(sorted(counts.values())) == [1, 1, 3]

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

def two_pair(counts):
    pairs = 0
    for v in counts.values():
        if v == 2:
            pairs += 1
    return pairs == 2
    
def one_pair(counts):
    for v in counts.values():
        if v == 2:
            return True
    return False

def high_card(counts):
    return len(counts.keys()) == 5


fs = {"five": five_of_a_kind, 
      "four": four_of_a_kind, 
      "full house": full_house, 
      "three": three_of_a_kind,
      "two_pair": two_pair, 
      "one_pair": one_pair, 
      "high_card": high_card}

def check_hand(hand):
    counts = hand_to_counts(hand)
    for k, v in fs.items():
        if v(counts):
            print(hand, k)
            break


def compare(hand1, hand2):
    counts1, counts2 = hand_to_counts(hand1), hand_to_counts(hand2)
    for _, v in fs.items():
        has_hand1 = v(counts1)
        has_hand2 = v(counts2)
        if has_hand1 and not has_hand2:
            return 1
        if has_hand2 and not has_hand1:
            return -1

    for h1, h2 in zip(hand1, hand2):
        if card_points[h1] == card_points[h2]:
            continue
        if card_points[h1] > card_points[h2]:
            return 1
        if card_points[h1] < card_points[h2]:
            return -1
    return 0


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

def solve_2():
    pass

DAY = 7
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

hands, bids = read_file(filename)

solve_1(hands, bids)



