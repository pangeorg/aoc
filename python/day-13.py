from utils import *

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines

def get_patterns(lines):
    patterns = []
    p = []
    for l in lines:
        if l == "":
            patterns.append(p)
            p = []
        else:
            p.append(l.strip())
    patterns.append(p)
    return patterns

def transpose(lines):
    xmax, ymax = len(lines[0]), len(lines)
    new_lines = []
    for x in range(xmax):
        new_lines.append("")
        for y in range(ymax):
            new_lines[x] += lines[y][x]
    return new_lines

def check_mirror(lines):
    n = len(lines)
    for i in range(1, n):
        above = lines[:i][::-1]
        below = lines[i:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return i
    return 0

def check_smudge(lines):
    n = len(lines)
    for i in range(1, n):
        above = lines[:i][::-1]
        below = lines[i:]
        
        above = above[:len(below)]
        below = below[:len(above)]

        # create a diff and check if there is only one missing
        # compare lines
        diff = 0
        for a, b in zip(above, below):
            # compare chars
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1
        if diff == 1:
            return i
    return 0

def solve_1(patterns):
    total = 0
    np = len(patterns)
    for np in range(len(patterns)):
        l = patterns[np]
        print()
        for line in l:
            print(line)
        # horizontal
        d = check_mirror(l)
        print(f"H: {d}")
        total += 100*d

        d = check_mirror(list(zip(*l)))
        total += d
        print(f"V: {d}")
    print(total)


def solve_2(patterns):
    total = 0
    np = len(patterns)
    for np in range(len(patterns)):
        l = patterns[np]
        print()
        for line in l:
            print(line)
        # horizontal
        d = check_smudge(l)
        print(f"H: {d}")
        total += 100*d

        d = check_smudge(list(zip(*l)))
        total += d
        print(f"V: {d}")
    print(total)

DAY = 13
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

patterns = read_lines_groups(filename, "\n\n")

# solve_1(patterns)
solve_2(patterns)

