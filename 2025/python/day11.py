from functools import total_ordering
from utils import read_lines

example = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()


def parse_data(lines: list[str]):
    data = {}
    for line in lines:
        key, values = line.split(":")
        values = values.strip().split(" ")
        data[key] = values
    return data


def part1():
    lines = example.splitlines()
    lines = read_lines("../data/day11.txt")
    data = parse_data(lines)

    seen = set()
    stack = [("you", ["you"])]
    found = []
    while stack:
        current, path = stack.pop()
        if current == "out":
            found.append(path)
            continue
        if current in seen:
            continue
        next_items = data[current]
        for next_item in next_items:
            next_path = list(path) + [next_item]
            stack.append((next_item, next_path))
    print(len(found))


example2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()


def part2():
    from functools import cache

    lines = example2.splitlines()
    lines = read_lines("../data/day11.txt")
    data = parse_data(lines)

    @cache
    def find(src, dst):
        if src == dst:
            return 1
        return sum(find(x, dst) for x in data.get(src, []))

    print(
        find("svr", "dac") * find("dac", "fft") * find("fft", "out")
        + find("svr", "fft") * find("fft", "dac") * find("dac", "out")
    )


part2()
