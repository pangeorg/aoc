example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def part1():
    with open("../data/day05.txt") as f:
        data = f.read()
    # data = example
    ranges, items = data.split("\n\n")
    ranges = ranges.splitlines()
    ranges = [
        (
            int(line.split("-")[0]),
            int(line.split("-")[1]),
        )
        for line in ranges
    ]
    items = [int(i) for i in items.splitlines()]
    count = 0
    for i in items:
        for r in ranges:
            if r[0] <= i <= r[1]:
                count += 1
                break
    print(count)


def part2():
    with open("../data/day05.txt") as f:
        data = f.read()
    # data = example
    ranges, _ = data.split("\n\n")
    ranges = ranges.splitlines()
    ranges = [
        [
            int(line.split("-")[0]),
            int(line.split("-")[1]),
        ]
        for line in ranges
    ]
    ranges.sort()
    result = [ranges[0]]
    for i in range(1, len(ranges)):
        last = result[-1]
        current = ranges[i]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)
    count = 0
    for r in result:
        count += r[1] - r[0] + 1
    print(count)


part2()
