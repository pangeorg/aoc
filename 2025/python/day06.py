from functools import reduce
import re

example = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip()

pattern = r"(\d+)"
ops_pattern = r"(\+|\*+)"

import operator

def part1():
    data = example
    with open("../data/day06.txt", "r") as f:
        data = f.read()
    lines = data.splitlines()

    ops = re.findall(ops_pattern, lines[-1])
    nums = list(map(int, re.findall(pattern, lines[0])))
    assert len(ops) == len(nums)

    for line in lines[1:-1]:
        for i, n in enumerate(re.findall(pattern, line)):
            op = ops[i]
            match op:
                case "*":
                    nums[i] *= int(n)
                case "+":
                    nums[i] += int(n)
    print(sum(nums))

def prod(iterable):
    return reduce(operator.mul, iterable)

def part2():

    data = example
    with open("../data/day06.txt", "r") as f:
        data = f.read()
    lines = data.splitlines()
    ops = re.findall(ops_pattern, lines[-1])
    ops = [operator.add if op == "+" else operator.mul for op in ops]
    lines = lines[:-1]

    cells = [[c for c in line] for line in lines]

    split_indices = []
    for x in range(len(lines[0])):
        is_split = True
        for y in range(len(lines)):
            if cells[y][x] != " ":
                is_split = False
                break
        if is_split:
            split_indices.append(x)

    pos = 0
    values = []
    total = 0
    for x in range(len(lines[0]) + 1):
        if x in split_indices or x == len(lines[0]):
            r = reduce(ops[pos], values)
            total += r
            values = []
            pos += 1
            if x == len(lines[0]):
                break
            else:
                continue
        mul = 1
        value = 0
        for y in reversed(range(len(lines))):
            n = cells[y][x]
            if n != " ":
                value += int(n) * mul
                mul *= 10
        values.append(value)
    print(total)

part2()



