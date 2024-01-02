south, north, east, west = (0, 1), (0, -1), (1, 0), (-1, 0)
dirs = (north, east, south, west,)
tiles = {
        "|":(north, south),
        "-":(east, west),
        "L":(north, east),
        "J":(north, west),
        "7":(south, west),
        "F":(south, east),
        }

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def find_animal(lines):
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] == "S":
                return x, y
    return 0, 0

def get_loop(lines):
    x, y = find_animal(lines)
    print(f"Animal found at {x}, {y}")

    # check where to go first
    tile = ""
    d = (0, 0)
    loop = [(x, y,)]
    for d in dirs:
        lookx, looky = x + d[0], y + d[1]
        if 0 <= lookx < len(lines[0]) and 0 <= looky < len(lines):
            tile = lines[looky][lookx]
            if tile in tiles:
                d1, d2 = tiles[tile]
                if d1 == (-d[0], -d[1]) or d2 == (-d[0], -d[1]):
                    x, y = lookx, looky 
                    loop.append((x, y,))
                    break

    while True:   
        d1, d2 = tiles[tile]
        if d1 == (-d[0], -d[1]):
            d = d2
        else:
            d = d1
        x, y = x + d[0], y + d[1]
        tile = lines[y][x]
        if tile == "S":
            break
        loop.append((x, y,))
    return loop

def is_in_loop(origin, loop, xmax, ymax, lines):
    """
    Cast rays in 4 directions and check how often we cross the loop
    https://en.wikipedia.org/wiki/Point_in_polygon
    """
    is_inside = []

    for d in dirs:
        crossings = 0
        was_on_loop = False
        print(f"checking dir, {d}")
        x, y = origin
        while True:
            if x < 0 or x == xmax or y < 0 or y == ymax:
                break
            on_loop = (x, y,) in loop
            print(f"checking {x},{y} {on_loop}")
            tile = lines[y][x]
            if was_on_loop and not on_loop:
                crossings += 1
            # check if we just are following the loop 
            if was_on_loop and on_loop:
                d1, d2 = tiles[tile]
                if d not in [d1, d2, (-d1[0], -d1[1],), (-d2[0], -d2[1],)]:
                    # perpendicular crossing
                    crossings += 1
            x, y = x + d[0], y + d[1]
            was_on_loop = on_loop
        # crossings -= 1
        # crossings = max(0, crossings)
        print(f"Crossings: {crossings}")
        is_inside.append(crossings % 2 != 0 and crossings != 0)
    print(is_inside)
    return all(is_inside)

def winding_number(origin, loop):
    wind = 0
    n = len(loop)
    o = origin
    for i in range(n):
        p = loop[i]
        q = loop[(i+1)%n]
        delta = (p[0] - o[0])*(q[1] - o[1]) - (p[1] - o[1])*(q[0] - o[0])
        if p[0] <= o[0] < q[0] and delta > 0:
            wind += 1
        elif q[0] <= o[0] < p[0] and delta < 0:
            wind -= 1
    return wind


def solve_1(lines):
    loop = get_loop(lines)
    print(len(loop) // 2)


def solve_2(lines):
    loop = get_loop(lines)
    print(f"Loop with len {len(loop)}")
    xmax, ymax = len(lines[0]), len(lines)
    inner_points = []
    for x in range(xmax):
        for y in range(ymax):
            if not (x, y) in loop:
                w = winding_number((x, y,), loop)
                inside = w % 2 != 0
                if inside:
                    inner_points.append((lines[y][x], y, x))
    # x, y = 2, 4
    # inside = is_in_loop((x, y,), loop, xmax, ymax, lines)
    # if inside:
    #     inner_points.append((lines[y][x], y, x))
    print(len(inner_points))
    print(inner_points)

DAY = 10
test = False
part = 2

if part == 1:
    if test:
        filename = "../data/sample-{:02d}.txt".format(DAY)
    else:
        filename = "../data/day-{:02d}.txt".format(DAY)
else:
    if test:
        filename = "../data/sample-{:02d}_02.txt".format(DAY)
    else:
        filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_file(filename)
# loop = get_loop(lines)
# xmax, ymax = len(lines[0]), len(lines)
# for l in lines:
#     print(l)

if part == 1:
    solve_1(lines)
else:
    solve_2(lines)
