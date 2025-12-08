from typing import cast
from utils import read_lines
from functools import cache

example = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()

Point = tuple[int, int, int]


def parse_data(lines: list[str]) -> list[Point]:
    return cast(list[Point], [tuple(map(int, line.split(","))) for line in lines])


@cache
def distance(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2


def find_closest_points(
    distances: dict[Point, list[tuple[float, Point]]],
) -> tuple[Point, Point]:
    d = float("inf")
    p1, p2 = None, None
    for p, values in distances.items():
        pd = min(values)
        if pd[0] < d:
            p1 = p
            p2 = pd[1]
    assert p1 is not None
    assert p2 is not None
    return p1, p2


def part01():
    data = example.splitlines()
    data = read_lines("../data/day08.txt")
    points = parse_data(data)

    distances = []
    seen = set()
    for p1 in points:
        for p2 in points:
            if p1 == p2 or (p1, p2) in seen or (p2, p1) in seen:
                continue
            distances.append((distance(p1, p2), p1, p2))
            seen.add((p1, p2))
            seen.add((p2, p1))
    distances.sort()

    circuits: list[set[Point]] = [{p} for p in points]

    limit = 1000
    for _, p1, p2 in distances[:limit]:
        c1, c2 = None, None
        for circuit in circuits:
            if p1 in circuit:
                c1 = circuit
            if p2 in circuit:
                c2 = circuit

        assert c1 is not None
        assert c2 is not None
        union = c1.union(c2)
        for x in [c1, c2]:
            if x in circuits:
                circuits.remove(x)
        circuits.append(union)

        # for c in circuits:
        #     print(len(c), c)

    circuits.sort(key=lambda c: len(c), reverse=True)
    # for circuit in circuits:
    #     print(len(circuit), circuit)
    total = 1
    for circuit in circuits[:3]:
        total *= len(circuit)
    print(total)


def part02():
    data = example.splitlines()
    data = read_lines("../data/day08.txt")
    points = parse_data(data)

    distances = []
    seen = set()
    for p1 in points:
        for p2 in points:
            if p1 == p2 or (p1, p2) in seen or (p2, p1) in seen:
                continue
            distances.append((distance(p1, p2), p1, p2))
            seen.add((p1, p2))
            seen.add((p2, p1))
    distances.sort()

    circuits: list[set[Point]] = [{p} for p in points]

    for _, p1, p2 in distances:
        c1, c2 = None, None
        for circuit in circuits:
            if p1 in circuit:
                c1 = circuit
            if p2 in circuit:
                c2 = circuit

        assert c1 is not None
        assert c2 is not None
        union = c1.union(c2)
        for x in [c1, c2]:
            if x in circuits:
                circuits.remove(x)
        circuits.append(union)
        if len(circuits) == 1:
            print(p1, p2, p1[0] * p2[0])
            break

        # for c in circuits:
        #     print(len(c), c)

    # circuits.sort(key=lambda c: len(c), reverse=True)
    # for circuit in circuits:
    #     print(len(circuit), circuit)
    # total = 1
    # for circuit in circuits[:3]:
    #     total *= len(circuit)
    # print(total)


part02()
