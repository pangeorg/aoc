import os
import sys
path = os.path.abspath(os.path.dirname(__file__) + "/..")
sys.path.append(path)

def solve_1():
    import utils

    lines = utils.read_lines("part1.txt")
    grid = utils.LineGrid(lines)
    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    result = 0
    for x in range(X_MAX):
        for y in range(Y_MAX):
            for d in utils.DIRS:
                c = (x, y)
                v = ""
                cinit = c[0], c[1]
                for _ in range(4):
                    if (not grid.has_point(c)):
                        break
                    v += grid[c]
                    c = utils.take_step(c, d)
                if v == "XMAS":
                    print(f"{cinit[0]}:{c[0]},{cinit[1]}:{c[1]}")
                    result += 1

    print(result)

def solve_2():
    import utils

    lines = utils.read_lines("part1.txt")
    grid = utils.LineGrid(lines)
    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    result = 0
    # visited = set()
    for y in range(Y_MAX):
        print("====")
        for x in range(X_MAX):
            x0, x1 = x, x + 2
            y0, y1 = y, y + 2
            if (not grid.has_point((x1, y1))):
                continue
            crosspoints1 = (grid[x0, y0], grid[x0 + 1, y0 + 1], grid[x1, y1])
            crosspoints2 = (grid[x1, y0], grid[x0 + 1, y0 + 1], grid[x0, y1])
            # if crosspoints2 in visited and crosspoints2 in visited:
            #     continue
            # visited.add(crosspoints2)
            # visited.add(crosspoints1)
            cross1 = "".join(crosspoints1)
            cross2 = "".join(crosspoints2)
            print(cross1, cross2)
            if cross1 in ["MAS", "SAM"] and cross2 in ["MAS", "SAM"]:
                result += 1

    print(result)


solve_2()
