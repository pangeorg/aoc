import re

mul_pattern = r"mul\(\d+,\d+\)"
mul_if_pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

def parse_line_regex(line):
    multiplications = re.findall(mul_pattern, line)
    result = 0
    for mult in multiplications:
        l, r = mult.split(',')
        l = int(l.strip().replace("mul(", ""))
        r = int(r.strip().replace(")", ""))
        result += (l*r)
    return result

def parse_line_regex2(line):
    operation = re.findall(mul_if_pattern, line)
    result = 0
    enabled = True
    for op in operation:
        if op == "don't()":
            enabled = False

        if op == "do()":
            enabled = True

        if "mul" in op and enabled:
            l, r = op.split(',')
            l = int(l.strip().replace("mul(", ""))
            r = int(r.strip().replace(")", ""))
            result += (l*r)
    return result

def solve_1():
    with open("part1.txt", "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        result += parse_line_regex(line)
    print(result)

def solve_2():
    with open("part1.txt", "r") as f:
        lines = f.readlines()

    line = "".join(lines)
    result = parse_line_regex2(line)
    print(result)


solve_2()
