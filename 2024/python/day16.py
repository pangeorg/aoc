import utils


def walk2(start, dir, grid):
    from collections import deque
    q = deque()
    q.append((start, set([start]), 0, dir,))
    found = []
    visited = {}
    while len(q):
        p, hist, cost, cur_dir = q.pop()

        if grid[p] == "E":
            found.append((hist, cost))
            continue

        if (p, cur_dir) in visited and visited[(p, cur_dir)] < cost:
            continue

        visited[(p, cur_dir)] = cost

        for dir in [utils.N, utils.S, utils.E, utils.W]:
            if dir == utils.REVERSE_DIR[cur_dir]:
                continue
            n = utils.take_step(p, dir)
            if grid[n] == "#" or n in hist:
                continue
            if dir == cur_dir:
                q.append((n, hist.union([n]), cost+1, dir))
            else:
                q.append((p, hist, cost+1000, dir))
    return found


def solve1():
    grid = utils.LineGrid(utils.read_lines("../input/day16.txt"))
    start = grid.find(lambda x: x == "S")
    dir = utils.E
    c = walk2(start, dir, grid)
    costs = [a[1] for a in c]
    min_cost = min(costs)
    print(min_cost)
    # for p in c[i][0]:
    #     grid[p] = "x"
    # grid.print()


def solve2():
    grid = utils.LineGrid(utils.read_lines("../input/sample16.txt"))
    start = grid.find(lambda x: x == "S")
    dir = utils.E
    c = walk2(start, dir, grid)
    costs = [a[1] for a in c]
    min_cost = min(costs)
    best = [r for r in c if r[1] == min_cost]
    tiles = {t for r in best for t in r[0]}
    print(len(tiles))
    # for p in c[i][0]:
    #     grid[p] = "x"
    # grid.print()


solve2()
