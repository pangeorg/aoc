
def create_node_2(p1, p2, grid, nodes, f):
    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
    for p in [p1, p2]:
        n = p
        while True:
            n = (n[0] + dx, n[1] + dy,)
            if not grid.has_point(n):
                break
            # if grid[n] != f:
            nodes.add(n)
            grid[n] = '#'

def create_node_1(p1, p2, grid, nodes, f):
    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
    for p in [p1, p2]:
        n = (p[0] + dx, p[1] + dy,)
        if grid[n] != f and grid.has_point(n):
            nodes.add(n)
            grid[n] = '#'

def solve1():
    import utils
    from collections import defaultdict
    from itertools import combinations

    lines = utils.read_lines("../input/day08.txt")
    grid = utils.LineGrid(lines)

    frequenzy_collection = defaultdict(list)
    for ix in range(grid.width):
        for iy in range(grid.height):
            if grid[(ix, iy,)] != ".":
                frequenzy_collection[grid[(ix, iy,)]].append((ix, iy,))

    nodes = set()
    for f, positions in frequenzy_collection.items():
        comb = combinations(positions, 2)
        for c in comb:
            create_node_1(c[0], c[1], grid, nodes, f)
            create_node_1(c[1], c[0], grid, nodes, f)

    print(len(nodes))


def solve2():
    import utils
    from collections import defaultdict
    from itertools import combinations

    lines = utils.read_lines("../input/day08.txt")
    grid = utils.LineGrid(lines)

    frequenzy_collection = defaultdict(list)
    for ix in range(grid.width):
        for iy in range(grid.height):
            if grid[(ix, iy,)] != ".":
                frequenzy_collection[grid[(ix, iy,)]].append((ix, iy,))

    nodes = set()
    for f, positions in frequenzy_collection.items():
        comb = combinations(positions, 2)
        for c in comb:
            create_node_2(c[0], c[1], grid, nodes, f)
            create_node_2(c[1], c[0], grid, nodes, f)
    print(str(grid))
    print(len(nodes))


solve2()
