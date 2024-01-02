from itertools import combinations

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]

    return lines

def str_insert(s: str, insert: str, index: int):
    return s[:index] + insert + s[index:]

def transpose(lines):
    xmax, ymax = len(lines[0]), len(lines)
    new_lines = []
    for x in range(xmax):
        new_lines.append("")
        for y in range(ymax):
            new_lines[x] += lines[y][x]
    return new_lines


def prepare(lines):
    xmax = len(lines[0])
    add_rows = []
    for i, l in enumerate(lines):
        if all([ch == "." for ch in l]):
            add_rows.append(i + len(add_rows))

    for r in add_rows:
        lines.insert(r, xmax * ".")
    
    lines = transpose(lines)

    xmax = len(lines[0])
    add_rows = []
    for i, l in enumerate(lines):
        if all([ch == "." for ch in l]):
            add_rows.append(i + len(add_rows))

    for r in add_rows:
        lines.insert(r + 1, xmax * ".")

    lines = transpose(lines)

    return lines

def prepare_weights(lines):
    xmax = len(lines[0])
    add_rows = []
    for i, l in enumerate(lines):
        if all([ch == "." for ch in l]):
            add_rows.append(i)

    add_cols = []
    for col in range(xmax):
        if all([l[col] == "." for l in lines]):
            add_cols.append(col)

    print(add_rows, add_cols)
    return add_rows, add_cols


def solve_1(lines):
    lines = prepare(lines)
    xmax, ymax = len(lines[0]), len(lines)
    galaxies = []
    for y in range(ymax):
        for x in range(xmax):
            if lines[y][x] == "#":
                galaxies.append((x, y,))
    comb = combinations(galaxies, 2)
    stps = 0
    for c in comb:
        dx = abs(c[0][0] - c[1][0])
        dy = abs(c[0][1] - c[1][1])
        step = dx + dy
        print(f"{galaxies.index(c[0])+1}->{galaxies.index(c[1])+1}", c, step)
        stps += step
    print(stps)

def solve_1_weights(lines):
    rows, cols = prepare_weights(lines)
    xmax, ymax = len(lines[0]), len(lines)
    galaxies = []
    for y in range(ymax):
        for x in range(xmax):
            if lines[y][x] == "#":
                galaxies.append((x, y,))
    comb = combinations(galaxies, 2)
    stps = 0
    for c in comb:
        gal1, gal2 = c[0], c[1]
        dx = abs(gal1[0] - gal2[0])
        dy = abs(gal1[1] - gal2[1])
        for row in rows:
            if min(gal1[1], gal2[1]) < row < max(gal1[1], gal2[1]):
                dy += 1
        for col in cols:
            if min(gal1[0], gal2[0]) < col < max(gal1[0], gal2[0]):
                dx += 1
        step = dx + dy
        stps += step
    print(stps)


def solve_2(lines):
    rows, cols = prepare_weights(lines)
    xmax, ymax = len(lines[0]), len(lines)
    galaxies = []
    for y in range(ymax):
        for x in range(xmax):
            if lines[y][x] == "#":
                galaxies.append((x, y,))
    comb = combinations(galaxies, 2)
    stps = 0
    scale = int(1e6)
    for c in comb:
        gal1, gal2 = c[0], c[1]
        dy, dx = 0, 0
        for i in range(min(gal1[1], gal2[1]), max(gal1[1], gal2[1])):
            dy += scale if i in rows else 1
        for i in range(min(gal1[0], gal2[0]), max(gal1[0], gal2[0])):
            dx += scale if i in cols else 1
        step = dx + dy
        # print(f"{galaxies.index(c[0])+1}->{galaxies.index(c[1])+1}", c, step)
        stps += step
    print(stps)

DAY = 11
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_file(filename)
for l in lines:
    print(l)

# solve_1_weights(lines)
solve_2(lines)
