from collections import Counter


def solve_1():
    with open("part1.txt", "r") as f:
        lines = f.readlines()
    l1, l2 = [], []
    for line in lines:
        s = line.split(' ')
        l1.append(int(s[0]))
        l2.append(int(s[-1]))

    l1 = sorted(l1)
    l2 = sorted(l2)

    result = 0
    for i in range(len(l1)):
        result += abs(l1[i] - l2[i])
    print(result)


def solve_2():
    with open("part1.txt", "r") as f:
        lines = f.readlines()
    l1, l2 = [], []
    for line in lines:
        s = line.split(' ')
        l1.append(int(s[0]))
        l2.append(int(s[-1]))

    l1 = sorted(l1)
    c = Counter(l2)

    result = 0
    for i in range(len(l1)):
        result += (l1[i] * c[l1[i]])
    print(result)


# solve_1()
solve_2()
