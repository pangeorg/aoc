from os import stat


def read(filename):
    import utils
    s = utils.read_filestr("../input/day24.txt").split("\n\n")
    transistions = {}
    states = {}

    for line in s[0].split("\n"):
        gate, v = line.split(": ")
        states[gate] = int(v)

    for rule in s[1].split("\n"):
        if rule == "":
            break
        inp, outp = rule.split(" -> ")
        l, op, r = inp.split(" ")
        f = None
        if op == "AND":
            f = lambda x, y: x and y
        if op == "OR":
            f = lambda x, y: x or y
        if op == "XOR":
            f = lambda x, y: x ^ y
        if f is None:
            raise Exception()
        transistions[outp] = f, r, l
    return states, transistions

def calc(w, states, transistions):
    if w in states:
        return states[w]
    f, right, left = transistions[w]
    states[w] = f(calc(left, states, transistions), calc(right, states, transistions))
    return states[w]

def get_zs(states, transistions):
    # calculate zs backwards
    z = []
    i = 0

    while True:
        key = f"z{i:02d}"
        if key not in transistions:
            break
        z.append(calc(key, states, transistions))
        i += 1
    return z[::-1]

def binstr(zs):
    return "".join(map(str, zs))

def run_addition(states, transistions):
    zs = get_zs(states, transistions)
    xs = [states[f"x{i:02d}"] for i in range(len(zs) - 2, -1, -1)]
    ys = [states[f"y{i:02d}"] for i in range(len(zs) - 2, -1, -1)]
    print("x", " " + binstr(xs))
    print("y", " " + binstr(ys))
    print("z", binstr(zs))


def solve1():
    states, transistions = read("../input/day24.txt")

    z = get_zs(states, transistions)
    print(int("".join(map(str, z)), 2))

def solve2():
    states, transistions = read("../input/day24.txt")
    run_addition(states, transistions)


solve2()
