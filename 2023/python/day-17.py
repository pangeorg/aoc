from utils import *

dirs = [E, W, S, N]
test_dirs = []
for d1 in dirs:
    for d2 in filter(lambda d: d != (-d1[0], -d1[1],), dirs):
        for d3 in filter(lambda d: d != (-d2[0], -d2[1],), dirs):
            test_dirs.append((d1, d2, d3,))

def try_block(pos, grid, visited):
    costs = []
    points = []
    for steps in test_dirs:
        cost = 0 
        count = 0
        n = pos
        for step in steps:
            n = take_step(n, step)
            if grid.has_point(n) and not n in visited:
                c = int(grid[n[0], n[1]])
                print(c)
                cost += c
                count += 1
                visited.add(n)
            else:
                break
        if count == 3:
            costs.append(cost)
            points.append(n)
    imin = costs.index(min(costs))
    return min(costs), points[imin]

def solve_1(lines):
    g = LineGrid(lines)
    pos = (0, 0)
    cost = 0
    visited = set()
    while pos != (g.width - 1, g.height - 1):
        c, p = try_block(pos, g, visited)
        cost += c
        pos = p
        print(pos, c, cost)

def solve_2():
    pass

def hyper(filename):
    from heapq import heappush, heappop

    grid = [list(map(int, line.strip())) for line in open(filename)]

    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            print(hl)
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

DAY = 17
test = True
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)


hyper(filename)

# lines = read_lines(filename)
# solve_1(lines)
# for td in test_dirs:
#     for d in td:
#         if d == N: print("N ", end="")
#         if d == E: print("E ", end="")
#         if d == W: print("W ", end="")
#         if d == S: print("S ", end="")
#     print()
