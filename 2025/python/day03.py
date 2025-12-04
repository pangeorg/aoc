example = """987654321111111
811111111111119
234234234234278
818181911112111"""

example2 = """987654321111111
811111111111119
234234234234278
999999999999999
111111111111119
111111111111191
111161111111111
874389274928789
111161111111189
999999999999189
818181911112111"""


def process_1(line: str):
    nums = [int(c) for c in line]
    num_1 = max(nums[:-1])
    imax = nums.index(num_1)
    num_2 = max(nums[imax + 1 :])
    return num_1 * 10 + num_2


def part1():
    with open("../data/day03.txt") as f:
        lines = f.readlines()
    # lines = example2.split("\n")

    total = 0
    for line in lines:
        if line == "\n" or not line:
            continue
        n = process_1(line.strip())
        # print(line, "->", n)
        total += n
    print(total)


def process_2(line: str):
    nums = [int(c) for c in line]
    value = 0
    pos = 0
    results = []
    for w in range(12, 0, -1):
        max_val = -1
        max_pos = pos
        for i in range(pos, len(nums) - w + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_pos = i + 1
        pos = max_pos
        results.append(max_val)

    mul = 1
    for r in results[::-1]:
        value += mul * r
        mul *= 10

    return value


def part2():
    with open("../data/day03.txt") as f:
        lines = f.readlines()
    # lines = example.split("\n")

    total = 0
    for line in lines:
        if line == "\n" or not line:
            continue
        n = process_2(line.strip())
        print(line, "->", n)
        total += n
    print(total)


part2()
# print(process_2("234234234234278"))
