def solve_1(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    points = 0
    for line in lines:
        _, numbers = line.split(": ")
        winning, nums = numbers.split(" | ")
        winning, nums = winning.split(" "), nums.split(" ")
        winning = set([int(w.strip()) for w in winning if w])
        nums = set([int(n.strip()) for n in nums if n])
        nwins = len(winning.intersection(nums))
        if nwins:
            points += 2**(nwins - 1)
    return points

def solve_2(filename):
    from collections import defaultdict
    with open(filename, "r") as f:
        lines = f.readlines()

    instances = defaultdict(lambda : 0)

    for i, line in enumerate(lines):
        _, numbers = line.split(": ")
        winning, nums = numbers.split(" | ")
        winning, nums = winning.split(" "), nums.split(" ")
        winning = set([int(w.strip()) for w in winning if w])
        nums = set([int(n.strip()) for n in nums if n])
        nwins = len(winning.intersection(nums))
        instances[i] += 1
        if nwins:
            for n in range(i + 1, i + nwins + 1):
                instances[n] += 1 * instances[i]

    return sum(instances.values())


test = False
if test:
    filename = "../data/sample-04-01.txt"
else:
    filename = "../data/day-04.txt"

result1 = solve_1(filename)
print("Result 1: ", result1)

result2 = solve_2(filename)
print("Result 2: ", result2)
