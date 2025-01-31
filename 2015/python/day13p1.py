from itertools import permutations

with open("../input/day13.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

connections = {}
people = set()
for line in lines:
    split = line.split(' ')
    gainLoos = split[2]
    amount = int(split[3])
    left, right = split[0], split[-1][:-1]
    if split[2] == 'lose':
        amount = -amount
    people.add(left)
    people.add(right)
    people.add('me')
    connections[(left, right)] = amount
    connections[(left, 'me')] = 0
    connections[('me', right)] = 0

people = list(people)
maxHappines = float('-Inf')
for per in permutations(people):
    happiness = 0
    for i in range(len(per) - 1):
        happiness += connections[(per[i], per[i + 1])]
        happiness += connections[(per[i + 1], per[i])]
    happiness += connections[(per[0], per[-1])]
    happiness += connections[(per[-1], per[0])]
    maxHappines = max(maxHappines, happiness)
print(maxHappines)