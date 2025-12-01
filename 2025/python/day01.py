example = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def part1():
    with open("../data/day01.txt") as f:
        lines = f.readlines()

    pos = 50
    n_zeros = 0
    for l in lines:
        d, n = l[0], int(l[1:])
        if d == "L":
            pos = (pos - n) % 100
        else:
            pos = (pos + n) % 100
        if pos == 0:
            n_zeros += 1
    print(n_zeros)


def next_pos_and_passes(dir: str, pos: int, n: int, size=10):
    passes = 0
    if dir == "L":
        pn = pos - n
        npos = pn % size
        if pn <= 0:
            passes = abs(pn) // size + 1
        if pos == 0:
            passes -= 1
    else:
        npos = (pos + n) % size
        passes = (pos + n) // size

    # print(dir, pos, n, "->", (npos, passes))
    return npos, passes


def tests_2():
    assert next_pos_and_passes("L", 0, 0) == (0, 0)
    assert next_pos_and_passes("L", 0, 9) == (1, 0)
    assert next_pos_and_passes("R", 0, 9) == (9, 0)
    assert next_pos_and_passes("L", 1, 2) == (9, 1)
    assert next_pos_and_passes("L", 1, 20) == (1, 2)
    assert next_pos_and_passes("R", 9, 1) == (0, 1)
    assert next_pos_and_passes("R", 9, 2) == (1, 1)
    assert next_pos_and_passes("R", 9, 20) == (9, 2)
    assert next_pos_and_passes("R", 9, 21) == (0, 3)


def part2():
    with open("../data/day01.txt") as f:
        lines = f.readlines()

    pos = 50
    n_zeros = 0
    for l in lines:
        d, n = l[0], int(l[1:])
        npos, passes = next_pos_and_passes(d, pos, n, 100)
        pos = npos
        n_zeros += passes
    print(pos, n_zeros)


def part2_while():
    with open("../data/day01.txt") as f:
        lines = f.readlines()

    pos = 50
    n_zeros = 0
    for l in lines:
        d, n = l[0], int(l[1:])
        if d == "L":
            while n > 0:
                if pos == 0:
                    n_zeros += 1
                pos -= 1
                n -= 1
                if pos < 0:
                    pos = 99
        elif d == "R":
            while n > 0:
                if pos == 0:
                    n_zeros += 1
                pos += 1
                n -= 1
                if pos > 99:
                    pos = 0
        # if pos == 0:
        #     n_zeros += 1
    print(pos, n_zeros)


part2()
