import utils
from collections import deque

def walk2(start, dir, grid):
    q = deque()
    n = utils.take_step(start, dir)
    visited = set([(start, dir,)])
    q.append((n, dir, 0,))
    found = []
    while True:
        p, prev_dir, cost = q.pop()
        if grid[p] == "E":
            found.append(cost)
            continue
        for dir in [utils.N, utils.S, utils.E, utils.W]:
            n = utils.take_step(p, dir)
            if grid[n] == "#" or (n, dir) in visited:
                continue
            print(n, dir)
            visited.add((n, dir,))
            if dir == prev_dir:
                q.append((n, dir, cost+1))
            else:
                q.append((n, dir, cost+1001))
        if len(q) == 0:
            break
    return min(found)


def solve1():
    grid = utils.LineGrid(utils.read_lines("../input/sample16.txt"))
    start = grid.find(lambda x: x == "S")
    dir = utils.E
    c = walk2(start, dir, grid)
    print(c)


solve1()
