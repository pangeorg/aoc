from contextlib import contextmanager
import utils

def solve1():
    grid = utils.LineGrid(utils.read_lines("../input/sample10.txt"))
    for x in range(grid.width):
        for y in range(grid.height):
            grid[(x, y)] = int(grid[(x, y)])

    zeros = grid.find_all(lambda x: x == 0)

    def find_trail(pos, grid, visited=None, found=[]):
        if not visited:
            visited = set()

        if grid[pos] == 9:
            found.append(pos)

        for dir in [utils.N, utils.S, utils.W, utils.E]:
            next = utils.take_step(pos, dir)
            if grid.has_point(next) and grid[pos] + 1 == grid[next] and next not in visited:
                visited.add(next)
                find_trail(next, grid, visited, found)

        return visited

    total = 0
    for zp in zeros:
        found = []
        find_trail(zp, grid, None, found)
        total += len(found)
    print(total)


def solve2():
    grid = utils.LineGrid(utils.read_lines("../input/day10.txt"))
    for x in range(grid.width):
        for y in range(grid.height):
            grid[(x, y)] = int(grid[(x, y)])

    zeros = grid.find_all(lambda x: x == 0)

    def find_trail(pos, prev, grid, visited):

        if grid[pos] == 9:
            visited[pos] += 1
            return

        for dir in [utils.N, utils.S, utils.W, utils.E]:
            next = utils.take_step(pos, dir)
            if next == prev:
                continue
            if not grid.has_point(next):
                continue
            if not (grid[pos] + 1 == grid[next]):
                continue
            find_trail(next, pos, grid, visited)

    from collections import defaultdict
    total = 0
    for zp in zeros:
        visited = defaultdict(int)
        find_trail(zp, (-1, -1), grid, visited)
        total += sum(visited.values())
    print(total)


solve2()
