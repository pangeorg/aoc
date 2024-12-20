import utils
from collections import deque

def get_region(grid, start):
    marker = grid[start]
    result = set()
    visited = set()
    queue = deque()
    queue.append(start)
    while True:
        parcel = queue.popleft()
        visited.add(parcel)
        if (not grid.has_point(parcel)):
            continue
        if grid[parcel] == marker:
            result.add(parcel)
            for dir in [utils.N, utils.S, utils.E, utils.W]:
                next = utils.take_step(parcel, dir)
                if (not grid.has_point(next)):
                    continue
                if (next in visited):
                    continue
                queue.insert(0, next)
        if len(queue) == 0:
            break

    return result

def price(garden):
    area = len(garden)
    perimeter = 0
    for parcel in garden:
        neighours = 4
        for dir in [utils.N, utils.S, utils.E, utils.W]:
            next = utils.take_step(parcel, dir)
            if next in garden:
                neighours -= 1
        perimeter += neighours
    return area * perimeter

def price_discount(garden):
    fences = set()
    for p in garden:
        for dir in [utils.N, utils.S, utils.E, utils.W]:
            next = utils.take_step(p, dir)
            if next not in garden:
                fences.add((p, dir))

    def find_side(start, fences):
        dir = start[1]
        dirs_to_walk = []
        if dir in [utils.E, utils.W]:
            dirs_to_walk = [utils.S, utils.N]
        if dir in [utils.S, utils.N]:
            dirs_to_walk = [utils.E, utils.W]
        result = set()
        visited = set()
        queue = deque()
        queue.append(start)
        while True:
            parcel = queue.popleft()
            visited.add(parcel[0])
            if parcel[1] == dir:
                result.add(parcel)
                for d in dirs_to_walk:
                    next = utils.take_step(parcel[0], d)
                    if (next, dir) not in fences:
                        continue
                    if (next in visited):
                        continue
                    queue.insert(0, (next, dir))
            if len(queue) == 0:
                break

        return result

    checked = set()
    result = []
    for f in fences:
        if f in checked:
            continue
        r = find_side(f, fences)
        checked = checked.union(r)
        result.append(r)

    return len(result) * len(garden)


def solve1():
    grid = utils.LineGrid(utils.read_lines("../input/day12.txt"))

    checked = set()
    gardens = []
    for x in range(grid.width):
        for y in range(grid.height):
            if (x, y) not in checked:
                r = get_region(grid, (x, y))
                checked = checked.union(r)
                gardens.append(r)

    total = 0
    for g in gardens:
        total += price(g)
    print(total)

def solve2():
    grid = utils.LineGrid(utils.read_lines("../input/day12.txt"))

    checked = set()
    gardens = []
    for x in range(grid.width):
        for y in range(grid.height):
            if (x, y) not in checked:
                r = get_region(grid, (x, y))
                checked = checked.union(r)
                gardens.append(r)

    total = 0
    for g in gardens:
        r = price_discount(g)
        total += r
    print(total)


solve2()
