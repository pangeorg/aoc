import re
import utils
from functools import cache


numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['X', '0', 'A'],
]

numpad_map = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    'X': (0, 3),
    '0': (1, 3),
    'A': (2, 3),
}

directional = [
    ['X', '^', 'A'],
    ['<', 'v', '>'],
]

directional_map = {
    'X': (0, 0),
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

dirs = {
    '^': utils.N,
    'v': utils.S,
    '<': utils.W,
    '>': utils.E,
}


def compute_sequences(map):
    # compute all possible ways to go from A -> B
    from itertools import permutations
    seqs = {}
    for a, av in map.items():
        for b, bv in map.items():
            if a == 'X' or b == 'X':
                continue
            if a == b:
                seqs[(a, b)] = ['A']
                continue
            dx = bv[0] - av[0]
            dy = bv[1] - av[1]
            moves = []
            if dy > 0:
                moves.extend(abs(dy) * ['v'])
            if dx > 0:
                moves.extend(abs(dx) * ['>'])
            if dy < 0:
                moves.extend(abs(dy) * ['^'])
            if dx < 0:
                moves.extend(abs(dx) * ['<'])
            possibilities = list(set(permutations(moves, len(moves))))

            seqs[(a, b)] = [
                "".join(list(p) + ['A'])
                for _, p in enumerate(possibilities)
            ]

    # filter out passes through X
    rmap = {v: k for k, v in map.items()}
    for k, possibilities in seqs.items():
        passesx = set()
        for i, path in enumerate(possibilities):
            pos = map[k[0]]
            for move in path[:-1]:
                if rmap[pos] == 'X':
                    passesx.add(i)
                    break
                pos = utils.take_step(pos, dirs[move])
        seqs[k] = [p for i, p in enumerate(possibilities) if i not in passesx]

    return seqs


def solve(code, seqs):
    from itertools import product
    options = [seqs[(x, y)] for x, y in zip('A' + code, code)]
    options = [o for o in options if len(o) > 0]
    return [(''.join(s)) for s in product(*options)]


def get_moves(code, map):
    pos = map['A']
    moves = []
    for c in code:
        next_pos = map[c]
        dx = next_pos[0] - pos[0]
        dy = next_pos[1] - pos[1]
        if dy > 0:
            moves.extend(abs(dy) * ['v'])
        if dx > 0:
            moves.extend(abs(dx) * ['>'])
        if dy < 0:
            moves.extend(abs(dy) * ['^'])
        if dx < 0:
            moves.extend(abs(dx) * ['<'])
        moves.append('A')
        pos = next_pos
    return "".join(moves)


numpad_seq = compute_sequences(numpad_map)
key_seq = compute_sequences(directional_map)
key_seq_len = {k: len(v[0]) for k, v in key_seq.items()}


@cache
def compute_length(x, y, d=25):
    if d == 1:
        return key_seq_len[(x, y)]
    optimal = float("inf")
    for s in key_seq[(x, y)]:
        l = 0
        for a, b in zip("A" + s, s):
            l += compute_length(a, b, d - 1)
        optimal = min(optimal, l)
    return optimal


def solve1():
    import utils
    lines = utils.read_lines("../input/day21.txt")
    total = 0
    # lines = [lines[0]]
    for code in lines:
        number_code = int(re.findall(r'\d+', code)[0])
        moves = solve(code, numpad_seq)
        for _ in range(2):
            pn = []
            for c in moves:
                pn += solve(c, key_seq)
            minlen = min(map(len, pn))
            moves = [s for s in pn if len(s) == minlen]
        total += len(moves[0]) * number_code
        print(code, moves[0], len(moves[0]), number_code, total)

    print()
    print(total)


def solve2():
    import utils
    lines = utils.read_lines("../input/day21.txt")
    total = 0
    # lines = [lines[0]]
    for code in lines:
        number_code = int(re.findall(r'\d+', code)[0])
        moves = solve(code, numpad_seq)
        optimal = float("inf")
        for s in moves:
            l = 0
            for x, y in zip("A" + s, s):
                l += compute_length(x, y)
            optimal = min(optimal, l)

        total += optimal * number_code

    print()
    print(total)


solve2()
