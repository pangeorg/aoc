import utils

def get_games(fname):
    def read_game_line(line, button="A"):
        a = line.replace(f"Button {button}: ", "")
        x, y = a.split(", ")
        return (int(x.replace("X+", "").strip()), int(y.replace("Y+", "").strip()))

    def read_price_line(line):
        a = line.replace("Prize: ", "")
        x, y = a.split(", ")
        return (int(x.replace("X=", "").strip()), int(y.replace("Y=", "").strip()))

    with open(fname, "r") as f:
        lines = f.readlines()

    games = []
    i = 0
    while i < len(lines):
        game = {}
        game['a'] = read_game_line(lines[i], 'A')
        i += 1
        game['b'] = read_game_line(lines[i], 'B')
        i += 1
        game['price'] = read_price_line(lines[i])
        i += 2
        games.append(game)
    return games


def solve1():
    games = get_games("../input/day13.txt")
    total = 0
    for g in games:
        a, b, p = g['a'], g['b'], g['price']
        ia = 0
        cost = None
        while ia <= 100:
            ia += 1
            ib = 0
            while ib <= 100:
                ib += 1
                ca = (a[0] * ia, a[1] * ia)
                cb = (b[0] * ib, b[1] * ib)
                cp = (ca[0] + cb[0], ca[1] + cb[1])
                if (cp == p):
                    if cost:
                        cost = min(ia * 3 + ib, cost)
                    else:
                        cost = ia * 3 + ib
        if cost:
            total += cost
    print(total)

def solve2():
    games = get_games("../input/day13.txt")
    total = 0

    # p = n1 * (a1 + a2) + n2 * (b1 + b2)
    # p = n1 * a1 + n1 * a2 + n2 * b1 + n2 * b2
    # p1 = n1 * a1 + n2 * b1
    # p2 = n1 * a2 + n2 * b2

    for g in games:
        a, b, p = g['a'], g['b'], g['price']
        p = (p[0] + 10000000000000, p[1] + 10000000000000)
        n1 = (b[1] * p[0] - b[0] * p[1])/(a[0]*b[1] - a[1]*b[0])
        n2 = (a[1] * p[0] - a[0] * p[1])/(a[1]*b[0] - a[0]*b[1])
        if (n1 > 0 and n2 > 0 and n1 % 1 == 0 and n2 % 1 == 0):
            total += (3*n1 + n2)
    print(int(total))


# solve1()
solve2()
