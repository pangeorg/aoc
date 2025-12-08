from collections import defaultdict
from utils import S, E, W, read_lines
from utils import LineGrid, take_step

example = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

def part1():
    # data = example.splitlines()
    data = read_lines("../data/day07.txt")
    grid = LineGrid(data)
    start = grid.find(lambda x: x == "S")
    assert start is not None

    tachyons = [start]
    splits = 0
    for _ in range(grid.height - 1):
        next_tachyons = set()
        for tachyon in tachyons:
            next_pos = take_step(tachyon, S)
            if grid[next_pos] == "^":
                de = take_step(next_pos, E)
                dw = take_step(next_pos, W)
                if grid.has_point(de) and grid.has_point(dw):
                    next_tachyons.add(dw)
                    next_tachyons.add(de)
                    grid[de] = "|"
                    grid[dw] = "|"
                    splits += 1
            else:
                next_tachyons.add(next_pos)
                grid[next_pos] = "|"
        grid.print()
        tachyons = list(next_tachyons)
    print(splits)


def part2_counts():
    data = example.splitlines()
    # data = read_lines("../data/day07.txt")
    grid = LineGrid(data)
    start = grid.find(lambda x: x == "S")
    assert start is not None

    tachyons: dict[tuple[int, int], int] = {}
    tachyons[start] = 0
    for _ in range(grid.height - 1):
        next_tachyons: dict[tuple[int, int], int] = defaultdict(int)
        for tachyon, c in tachyons.items():
            next_pos = take_step(tachyon, S)
            if grid[next_pos] == "^":
                for d in [E, W]:
                    n = take_step(next_pos, d)
                    if grid.has_point(n) and n not in tachyons:
                        next_tachyons[n] += c + 1
                        grid[n] = "|"
            else:
                next_tachyons[next_pos] = c
                grid[next_pos] = "|"
        tachyons = next_tachyons
        print(tachyons)
        grid.print()
        input()

    mt = min(tachyons.values())
    d = {k: v // mt for k, v in tachyons.items()}
    print(d)
    print(sum(d.values()))


def part2_brute():
    data = example.splitlines()
    # data = read_lines("../data/day07.txt")
    grid = LineGrid(data)
    start = grid.find(lambda x: x == "S")
    assert start is not None

    tachyons = [start]
    us = 0
    counts = {}
    while len(tachyons) > 0:
        pos = tachyons.pop()
        for _ in range(grid.height - 1):
            next_pos = take_step(pos, S)
            if not grid.has_point(next_pos):
                break
            if grid[next_pos] == "^":
                for d in [E, W]:
                    n = take_step(next_pos, d)
                    if grid.has_point(n) and n not in tachyons:
                        tachyons.append(n)
                        # grid[n] = "|"
            else:
                if next_pos not in tachyons:
                    tachyons.append(next_pos)
                    # grid[next_pos] = "|"
        for t in tachyons:
            if t[1] == grid.height - 1:
                break
        # grid.print()
        # print(pos, tachyons, us)
        # input()
    print(us)


def part2():
    # data = example.splitlines()
    from functools import cache
    data = read_lines("../data/day07.txt")
    grid = LineGrid(data)
    start = grid.find(lambda x: x == "S")
    assert start is not None

    @cache
    def solve(pos):
        if not grid.has_point(pos):
            return 1
        if grid[pos] == "." or grid[pos] == "S":
            return solve(take_step(pos, S))
        else:
            return solve(take_step(pos, W)) + solve(take_step(pos, E))
    print(solve(start))


part2()


