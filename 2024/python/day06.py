from concurrent import futures
import utils

def solve_1():
    lines = utils.read_lines("../input/sample06.txt")
    grid = utils.LineGrid(lines)
    start = grid.find(lambda x: x == "v" or x == "<" or x == "^" or x == ">")

    if start is None:
        raise Exception("aaaa")

    direction: tuple[int, int] = (0, 0)
    match grid[start]:
        case "v":
            direction = utils.S
        case "^":
            direction = utils.N
        case ">":
            direction = utils.E
        case "<":
            direction = utils.W

    visited = set([start])
    while True:
        grid[start] = "X"
        next_pos = utils.take_step(start, direction)
        if not grid.has_point(next_pos):
            break
        if grid[next_pos] == "#":
            direction = utils.point_rotate_right(direction)
            next_pos = utils.take_step(start, direction)
        start = next_pos
        visited.add(start)

    print(str(grid))
    print(len(visited))

def walk(p, d, grid, turnPos):
    visited = set()
    while True:
        visited.add((p, d))
        next = utils.take_step(p, d)
        if not grid.has_point(next):
            return 0
        if grid[next] == "#" or next == turnPos:
            d = utils.point_rotate_right(d)
        else:
            p = next
        if ((p, d)) in visited:
            return 1

def solve_2():
    lines = utils.read_lines("../input/day06.txt")
    grid = utils.LineGrid(lines)
    start = grid.find(lambda x: x == "v" or x == "<" or x == "^" or x == ">")

    if start is None:
        raise Exception("aaaa")

    direction: tuple[int, int] = (0, 0)
    match grid[start]:
        case "v":
            direction = utils.S
        case "^":
            direction = utils.N
        case ">":
            direction = utils.E
        case "<":
            direction = utils.W

    obstructions = 0
    for x in range(grid.width):
        for y in range(grid.height):
            pos = (x, y)
            if grid[pos] != ".":
                continue
            turnpos = pos
            obstructions += walk(start, direction, grid, turnpos)

    print(obstructions)


solve_2()
