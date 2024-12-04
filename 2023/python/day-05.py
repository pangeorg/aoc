from pprint import pprint

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    data = {}
    seeds = list(map(int, lines[0].strip().split(": ")[-1].split(" ")))
    data["seeds"] = seeds
    data["maps"] = []
    data["map_names"] = []

    for l in lines[2:]:
        if l == "\n":
            data["maps"].append(ranges)
            in_map = False
            continue
        if "map" in l:
            data["map_names"].append(l.split("-")[2].replace(" map:", "").strip())
            ranges = []
            in_map = True
            continue
        if in_map:
            line_data = list(map(int, l.strip().split(" ")))
            ranges.append(line_data)

    # dont forget the last one
    data["maps"].append(ranges)

    return data

def solve_1(data):
    import sys
    min_location = sys.maxsize
    for seed in data["seeds"]:
        start = seed
        for _, seed_map in enumerate(data["maps"]):
            for rng in seed_map:
                dst, src, n = rng
                if src <= start < src + n:
                    start = dst + (start - src)
                    break
        min_location = min(min_location, start)
    return min_location



def solve_2(data):
    from functools import reduce

    seed_starts = data["seeds"][::2]
    seed_nums = data["seeds"][1::2]
    seeds = [(s, s + n) for s, n in zip(seed_starts, seed_nums)]

    for seed_map in data["maps"]:
        new_ranges = []
        while seeds:
            start, end = seeds.pop()
            for rng in seed_map:
                dst, src, n = rng
                overlap_start = max(start, src)
                overlap_end = min(end, src + n)
                if overlap_start < overlap_end:
                    new_ranges.append((overlap_start - src + dst, overlap_end - src + dst))
                    if overlap_start > start:
                        seeds.append((start, overlap_start,))
                    if end > overlap_end:
                        seeds.append((overlap_end, end,))
            else:
                new_ranges.append((start, end,))
        seeds = new_ranges

    print(seeds)
    return min(seeds)

def solve_2_other(filename):
    inputs, *blocks = open(filename).read().split("\n\n")

    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
        seeds = new

    return min(seeds)[0]


test = False
if test:
    filename = "../data/sample-05.txt"
else:
    filename = "../data/day-05.txt"

data = read_file(filename)

result1 = solve_1(data)
print(f"Result 1: {result1}")

result2 = solve_2_other(filename)
print(f"Result 2: {result2}")
