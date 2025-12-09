from utils import read_lines
from typing import cast

example = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

# X-X....X-X
# |.|....|.|
# |.X----X.|
# |........|
# X--------X
test_data = """
1,1
3,1
3,3
8,3
8,1
10,1
10,5
1,5
""".strip()


Point = tuple[float, float]


def parse_data(lines: list[str]) -> list[Point]:
    return cast(list[Point], [tuple(map(int, line.split(","))) for line in lines])


def area(p1: Point, p2: Point):
    return abs((p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))


def part01():
    data = example.splitlines()
    data = read_lines("../data/day09.txt")
    points = parse_data(lines=data)
    max_area = -1
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            carea = area(p1, p2)
            if carea > max_area:
                max_area = carea
    print(max_area)


def intersect_segment(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    x, y = 0, 1
    x0, x1, x2, x3 = p1[x], p2[x], p3[x], p4[x]
    y0, y1, y2, y3 = p1[y], p2[y], p3[y], p4[y]

    p_0 = (y3 - y2) * (x3 - x0) - (x3 - x2) * (y3 - y0)
    p_1 = (y3 - y2) * (x3 - x1) - (x3 - x2) * (y3 - y1)
    p_2 = (y1 - y0) * (x1 - x2) - (x1 - x0) * (y1 - y2)
    p_3 = (y1 - y0) * (x1 - x3) - (x1 - x0) * (y1 - y3)

    result = p_0 * p_1 < 0 and p_2 * p_3 < 0
    return result


def shift_points(points):
    shifted_points = []

    for i, p in enumerate(points):
        p0 = points[i - 1]
        if i < len(points) - 1:
            p2 = points[i + 1]
        else:
            p2 = points[0]
        dx = p2[0] - p0[0]
        dy = p2[1] - p0[1]
        shift_x = 0
        shift_y = 0
        if dx >= 0 and dy <= 0:
            shift_x = -0.5
            shift_y = -0.5
        elif dx >= 0 and dy >= 0:
            shift_x = 0.5
            shift_y = -0.5
        elif dx <= 0 and dy <= 0:
            shift_x = -0.5
            shift_y = 0.5
        elif dx <= 0 and dy >= 0:
            shift_x = 0.5
            shift_y = 0.5
        shifted_points.append((p[0] + shift_x, p[1] + shift_y))
    return shifted_points


def build_rectangle(p1, p2):
    return [
        p1,
        (p2[0], p1[1]),
        p2,
        (p1[0], p2[1]),
    ]


def is_inside(p, walls, xmin, xmax):
    line = ((xmin, p[1]), (xmax, p[1]))
    intersects = 0
    for wall in walls:
        if intersect_segment(line[0], line[1], wall[0], wall[1]):
            intersects += 1

    return intersects % 2 != 0


def build_walls(points):
    walls = []
    for i in range(len(points)):
        walls.append((points[i - 1], points[i]))
    return walls


def part02_is_inside():
    # WRONG APPROACH BECAUSE
    # ...............
    # ...X-X....X-X.. <- WILL NOT DETECT THIS
    # ...|.|....|.|..
    # ...|.X----X.|..
    # ...|........|..
    # ...X--------X..
    # ...............
    data = example.splitlines()
    data = read_lines("../data/day09.txt")
    points = parse_data(lines=data)
    xmin, xmax = float("inf"), -1
    for p in points:
        xmin = min(p[0], xmin)
        xmax = max(p[0], xmax)

    max_area = -1
    walls = build_walls(points)

    seen = set()
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            if (p1, p2) in seen:
                continue
            seen.add((p1, p2))
            rectangle = build_rectangle(p1, p2)
            intersected = False
            for r in rectangle:
                if not is_inside(r, walls, xmin, xmax):
                    intersected = True
                    break
            if intersected:
                continue
            carea = area(p1, p2)
            if carea > max_area:
                max_area = carea
    print(max_area)


def solve_2_also_broken(data):
    points = parse_data(lines=data)
    shifted_points = shift_points(points)

    walls = build_walls(shifted_points)

    max_area = -1
    seen = set()
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            if (p1, p2) in seen:
                continue
            seen.add((p1, p2))
            rectangle_walls = [
                (p1, (p2[0], p1[1])),
                ((p2[0], p1[1]), p2),
                (p2, (p1[0], p2[1])),
                ((p1[0], p2[1]), p1),
            ]
            carea = area(p1, p2)
            if carea <= max_area:
                continue
            intersected = False
            for wall in walls:
                if intersected:
                    break
                for rw in rectangle_walls:
                    if intersect_segment(rw[0], rw[1], wall[0], wall[1]):
                        intersected = True
                        break
            if intersected:
                continue
            if carea > max_area:
                max_area = carea
    print(max_area)


def test_shift_points():
    # X--X
    # |..|
    # X--X
    points = [
        (1, 1),
        (4, 1),
        (4, 3),
        (1, 3),
    ]
    shifted = shift_points(points)
    expected = [
        (0.5, 0.5),
        (4.5, 0.5),
        (4.5, 3.5),
        (0.5, 3.5),
    ]
    for s, e in zip(shifted, expected):
        assert s == e

    # X-X....X-X
    # |.|....|.|
    # |.X----X.|
    # |........|
    # X--------X

    points = [
        (1, 1),
        (3, 1),
        (3, 3),
        (8, 3),
        (8, 1),
        (10, 1),
        (10, 5),
        (1, 5),
    ]
    shifted = shift_points(points)
    expected = [
        (0.5, 0.5),
        (3.5, 0.5),
        (3.5, 2.5),
        (7.5, 2.5),
        (7.5, 0.5),
        (10.5, 0.5),
        (10.5, 5.5),
        (0.5, 5.5),
    ]
    for s, e in zip(shifted, expected):
        assert s == e


def test_intersections():
    # ..| <- here
    # O-X....X-O
    # |.|....|.|
    # |.X----X.|
    # |........|
    # O--------O
    wall = ((3.5, 0.5), (3.5, 2.5))
    rw = ((1, 1), (10, 1))
    assert intersect_segment(rw[0], rw[1], wall[0], wall[1])


def rect_contained(min_x, max_x, min_y, max_y, edges):
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return False
    return False


def solve_2(data):
    from itertools import combinations

    tiles = parse_data(lines=data)
    edges = []
    n = len(tiles)
    for i in range(n - 1):
        p1 = tiles[i]
        p2 = tiles[i + 1]
        edges.append(
            (min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1]))
        )

    p_last = tiles[-1]
    p_first = tiles[0]
    edges.append(
        (
            min(p_last[0], p_first[0]),
            min(p_last[1], p_first[1]),
            max(p_last[0], p_first[0]),
            max(p_last[1], p_first[1]),
        )
    )

    max_area = -1
    for p1, p2 in combinations(tiles, 2):
        min_x, max_x = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
        min_y, max_y = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])
        carea = area(p1, p2)
        if carea > max_area:
            if rect_contained(min_x, max_x, min_y, max_y, edges):
                max_area = carea
    print(max_area)


def is_fully_contained(
    edges: list[tuple[int, int, int, int]],
    min_x: int,
    min_y: int,
    max_x: int,
    max_y: int,
) -> bool:
    """Check if the rectangle is fully contained."""
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return False
    return True


def part2_opt(data) -> int:
    from itertools import combinations

    tiles = []
    for line in data:
        parts = line.split(",")
        tiles.append((int(parts[0]), int(parts[1])))

    edges = []
    n = len(tiles)
    for i in range(n - 1):
        p1 = tiles[i]
        p2 = tiles[i + 1]
        edges.append(
            (min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1]))
        )

    p_last = tiles[-1]
    p_first = tiles[0]
    edges.append(
        (
            min(p_last[0], p_first[0]),
            min(p_last[1], p_first[1]),
            max(p_last[0], p_first[0]),
            max(p_last[1], p_first[1]),
        )
    )

    result = 0

    for p1, p2 in combinations(tiles, 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        if area <= result:
            continue

        min_x, max_x = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
        min_y, max_y = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])

        if is_fully_contained(edges, min_x, min_y, max_x, max_y):
            result = area

    print(result)
    return result


def part2():
    data = example.splitlines()
    data = read_lines("../data/day09.txt")
    part2_opt(data)


part2()
