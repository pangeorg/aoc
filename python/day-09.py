def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines

def list_diff(a):
    return [a[i+1] - a[i] for i in range(len(a) - 1)]


def solve_1(lines):
    seqs = [list(map(int, l.split(' '))) for l in lines]
    result = 0
    for seq in seqs:
        diffs = []
        dif = seq
        diffs.append(dif)
        while not all([d == 0 for d in dif]):
            dif = list_diff(dif)
            diffs.append(dif)
        diffs = list(reversed(diffs))
        ex = 0
        for i in range(len(diffs) - 1):
            ex = ex + diffs[i+1][-1]
        result += ex
    print(result)

def solve_2(lines):
    seqs = [list(map(int, l.split(' '))) for l in lines]
    result = 0
    for seq in seqs:
        diffs = []
        dif = seq
        diffs.append(dif)
        while not all([d == 0 for d in dif]):
            dif = list_diff(dif)
            diffs.append(dif)
        diffs = list(reversed(diffs))
        ex = 0
        for i in range(len(diffs) - 1):
            ex = diffs[i+1][0] - ex
        result += ex
    print(result)

DAY = 9
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_file(filename)
# solve_1(lines)
solve_2(lines)
