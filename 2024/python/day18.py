import utils

def solve1():
    # from heapq import heappop, heappush
    from collections import deque
    X, Y = 70, 70
    bts = utils.read_lines("../input/day18.txt")
    bts = [tuple(map(int, line.split(","))) for line in bts]

    grid = [(X + 1)*"." for _ in range(Y + 1)]
    grid = utils.LineGrid(grid)
    for i in range(1024):
        grid[bts[i]] = "#"

    start = (0, 0)
    q = deque()
    q.append((0, start,))
    visited = set()

    while q:
        steps, pos = q.popleft()
        for n in utils.neighbors(pos):
            if n in visited:
                continue
            if not grid.has_point(n) or grid[n] == "#":
                continue
            if n == (X, Y):
                print(steps + 1)
                break
            visited.add(n)
            q.append((steps + 1, n))

def solve2():
    X, Y = 70, 70
    bts = utils.read_lines("../input/day18.txt")
    bts = [tuple(map(int, line.split(","))) for line in bts]

    grid = [(X + 1)*"." for _ in range(Y + 1)]
    grid = utils.LineGrid(grid)

    iblocks = 1
    while True:
        for i in range(iblocks):
            grid[bts[i]] = "#"
        r = grid.get_region((X, Y))
        if (0, 0) not in r:
            break
        iblocks += 1
    print(iblocks, bts[iblocks - 1])


solve2()
