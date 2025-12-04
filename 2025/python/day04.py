from utils import DIRS, LineGrid, read_lines, take_step

example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()


def part1():
    # lines = example.splitlines()
    lines = read_lines("../data/day04.txt")
    grid = LineGrid(lines)
    total = 0
    for iy in range(grid.rows):
        for ix in range(grid.cols):
            pos = (ix, iy)
            if grid[pos] == ".":
                continue
            count = 0
            for other in [take_step(pos, dir) for dir in DIRS]:
                if not grid.has_point(other):
                    continue
                if grid[other] == "@":
                    count += 1
            if count < 4:
                total += 1
    print(total)


def part2():
    # lines = example.splitlines()
    lines = read_lines("../data/day04.txt")
    grid = LineGrid(lines)
    total = 0
    removed = True
    while removed:
        removed = False
        for iy in range(grid.rows):
            for ix in range(grid.cols):
                pos = (ix, iy)
                if grid[pos] == ".":
                    continue
                count = 0
                for other in [take_step(pos, dir) for dir in DIRS]:
                    if not grid.has_point(other):
                        continue
                    if grid[other] == "@":
                        count += 1
                if count < 4:
                    total += 1
                    grid[pos] = "."
                    removed = True
    print(total)


part2()
