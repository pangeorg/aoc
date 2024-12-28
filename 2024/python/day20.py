from typing import List
import utils


def find_path(grid, start, end) -> List[tuple[int, int]]:
    from collections import deque

    q = deque()
    q.append((start, [start],))
    visited = set()

    while q:
        p, hist = q.popleft()
        if p == end:
            return hist
        for n in utils.neighbors(p):
            if n in visited or not grid.has_point(n) or grid[n] == "#":
                continue
            visited.add(n)
            q.append((n, hist + [n]))
    return []


def solve1():
    grid = utils.LineGrid(utils.read_lines("../input/day20.txt"))
    start = grid.find(lambda x: x == "S")
    end = grid.find(lambda x: x == "E")
    path = find_path(grid, start, end)

    saves = {}  # map time saved : count

    for i, p in enumerate(path):
        for dir in [utils.E, utils.W, utils.S, utils.N]:
            n = utils.take_step(p, dir)
            if not grid[n] == "#":
                continue
            # found a wall so lets jump
            n = utils.take_step(n, dir)
            if n not in path:
                continue
            index = path.index(n)
            if index > i:
                save = index - i - 2
                if save in saves:
                    saves[save] += 1
                else:
                    saves[save] = 1
    result = sorted([(k, v) for k, v in saves.items()])
    total = 0
    for r in result[::-1]:
        print(r)
        if r[0] >= 100:
            total += r[1]
    print(total)


def reachable(p, index, pxs, pys, dist=100):
    result = []
    for i in range(len(pxs)):
        px, py = pxs[i], pys[i]
        d = utils.distance_path(p, (px, py,))
        if d <= dist:
            result.append((d, i + index, px, py))
    return result


def solve2():
    from array import array
    grid = utils.LineGrid(utils.read_lines("../input/day20.txt"))
    start = grid.find(lambda x: x == "S")
    end = grid.find(lambda x: x == "E")
    path = find_path(grid, start, end)

    pxs = array("i", [p[0] for p in path])
    pys = array("i", [p[1] for p in path])

    saves = {}  # map time saved : count

    for i, p in enumerate(path):
        points = reachable(p, i, pxs[i:], pys[i:], 20)
        for r in points:
            d = r[0]
            index = r[1]
            save = index - i - d
            if save <= 0:
                continue
            if save in saves:
                saves[save] += 1
            else:
                saves[save] = 1

    result = sorted([(k, v) for k, v in saves.items()])
    total = 0
    for r in result[::-1]:
        if r[0] >= 100:
            print(r)
            total += r[1]
    print(total)


solve2()
