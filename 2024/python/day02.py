from collections import Counter


def sign(x):
    if x >= 0:
        return 1
    return -1


def is_safe(levels):
    max_diff = -1
    dir = 0
    for i in range(len(levels) - 1):
        dif = levels[i+1] - levels[i]
        max_diff = max(max_diff, abs(dif))
        if max_diff > 3 or abs(dif) < 1:
            return False
        if i > 0:
            if dir != sign(dif):
                return False
        dir = sign(dif)
    return True


def solve_1():
    with open("part1.txt", "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        levels = [int(e) for e in line.split(' ')]
        if is_safe(levels):
            result += 1
    print(result)


def solve_2():
    with open("part1.txt", "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        levels = [int(e) for e in line.split(' ')]
        if is_safe(levels):
            result += 1
        else:
            now_safe = False
            for i in range(len(levels)):
                less = [levels[ii] for ii in range(len(levels)) if ii != i]
                if is_safe(less):
                    now_safe = True
            if now_safe:
                result += 1

    print(result)


# solve_1()
solve_2()
