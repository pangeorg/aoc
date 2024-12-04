from utils import *

def tilt(lines):
    grid = [list(l) for l in lines]
    for row in range(1, len(grid)):
        for col, c in enumerate(grid[row]):
            if c == "O":
                pos = row
                while True:
                    if grid[pos - 1][col] == ".":
                        # swap
                        grid[pos - 1][col] = "O"
                        grid[pos][col] = "."
                        pos -= 1
                        if pos == 0:
                            break
                    else:
                        break
    return grid

def calculate_load(grid):
    n = len(grid)
    total = 0
    for i, row in enumerate(grid):
        for c in row:
            if c == "O":
                total += (n - i)
    return total

def solve_1(lines):
    grid = tilt(lines)
    for g in grid:
        print("".join(g))
    total = calculate_load(grid)
    print(total)

def solve_2(lines):
    grid = tuple(["".join(l) for l in lines])
    seen = {grid}
    grids = [grid]
    i = 0
    while True:
        i += 1
        for _ in range(4):
            grid = tilt(grid)
            grid = grid_rotate_right(grid)
        grid = tuple(["".join(g) for g in grid])
        if grid in seen:
            print("Found")
            break
        seen.add(grid)
        grids.append(grid)

    first = grids.index(grid)
    grid = grids[(1000000000 - first) % (i - first) + first]

    total = calculate_load(grid)
    print(total)

DAY = 14
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_lines(filename)
# solve_1(lines)
solve_2(lines)
