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

def solve_1(lines):
    x, y = find_animal(lines)
    print(f"Animal found at {x}, {y}")
    firstx, firsty = x, y

    # check where to go first
    tile = ""
    d = (0, 0)
    for d in dirs:
        lookx, looky = x + d[0], y + d[1]
        tile = lines[looky][lookx]
        if tile in tiles.keys():
            x, y = lookx, looky 
            break

    l = 1
    while True:   
        d1, d2 = tiles[tile]
        if d1 == (-d[0], -d[1]):
            d = d2
        else:
            d = d1
        x, y = x + d[0], y + d[1]
        tile = lines[y][x]
        l += 1
        if x == firstx and y == firsty:
            break
    print(l // 2)
        
def solve_1_working(filename):
    from collections import deque

    grid = open(filename).read().strip().splitlines()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                sr = r
                sc = c
                break
        else:
            continue
        break

    loop = {(sr, sc)}
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in loop:
            loop.add((r - 1, c))
            q.append((r - 1, c))
            
        if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
            loop.add((r + 1, c))
            q.append((r + 1, c))

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
            loop.add((r, c - 1))
            q.append((r, c - 1))

        if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
            loop.add((r, c + 1))
            q.append((r, c + 1))

    print(len(loop) // 2)

def solve_2():
    pass

DAY = 10
test = True
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_file(filename)
for l in lines:
    print(l)
solve_1(lines)
solve_1_working(filename)
