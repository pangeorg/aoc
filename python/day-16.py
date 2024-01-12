from utils import *

def solve_1(lines):
    grid = LineGrid(lines)
    pos, d = (0, 0,), S
    # beam list of positions and current direction
    beams = [(pos, d)]
    visited = set()
    visited.add((pos, d))
    while beams:
        beam = beams.pop(0)
        pos, d = beam
        next_pos = take_step(pos, d)
        if not grid.has_point(next_pos):
            continue
        pos = next_pos
        ch = grid[pos]
        if ch == "|" and d in [E, W]:
            d = N
            if (pos, d) not in visited:
                beams.append((pos, d,))
            d = S
            if (pos, d) not in visited:
                beams.append((pos, d,))
        elif ch == "\\":
            d = d[1], d[0]
            if (pos, d) not in visited:
                beams.append((pos, d,))
        elif ch == "/":
            d = -d[1], -d[0]
            if (pos, d) not in visited:
                beams.append((pos, d,))
        elif ch == "-" and d in [S, N]:
            d = E
            if (pos, d) not in visited:
                beams.append((pos, d,))
            d = W
            if (pos, d) not in visited:
                beams.append((pos, d,))
        else:
            if (pos, d) not in visited:
                beams.append((pos, d,))
        visited.add((pos, d))

    coords = [(pos[1], pos[0]) for (pos, _,) in visited]
    total = 0
    for row in range(grid.height):
        line = ""
        for col in range(grid.width):
            if (row, col) in coords:
                line += "#"
                total += 1
            else:
                line += "."
        print(line)
    print(total)

def solve_2(lines):
    pass

DAY = 16
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
    print("Should")
    print("######....")
    print(".#...#....")
    print(".#...#####")
    print(".#...##...")
    print(".#...##...")
    print(".#...##...")
    print(".#..####..")
    print("########..")
    print(".#######..")
    print(".#...#.#..")
    print("")
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_lines(filename)
solve_1(lines)
# solve_2(lines)
