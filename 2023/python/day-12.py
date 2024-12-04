import re 
from itertools import *

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def search_indices(s: str, find: str):
    indices = []
    for i, ch in enumerate(s):
        if ch == find:
            indices.append(i)
    return indices

def str_replace_index(s: str, replace: str, index: int):
 return s[:index] + replace + s[index + 1:]

def solve_1_brute_force(lines):
    total = 0
    for row in lines:
        locs, infostr = row.split(" ")
        groups = [int(g) for g in infostr.split(",")]
        indices = search_indices(locs, "?")
        n = len(indices)
        perm = []
        perm.append((n * (True,)))
        for i in range(n):
            l = i * [True] + (n - i) * [False]
            perm.extend(list(permutations(l, n)))
        perm = set(perm)
        possibilities = 0
        for p in perm:
            nlocs = locs
            for i, index in enumerate(indices):
                if p[i]:
                    nlocs = str_replace_index(nlocs, "#", index) 
            springs = re.findall(r"#+", nlocs)
            spring_count = [len(s) for s in springs]
            if spring_count == groups:
                # print(p, spring_count, groups)
                possibilities += 1
            
        total += possibilities
        print(possibilities)
        # unknown = re.findall(r"\?+", locs)
        # springs = re.findall(r"#+", locs)
        # print(unknown)
        # print(springs)
    print(total)

def solve_1(lines):
    total = 0
    for row in lines:
        locs, infostr = row.split(" ")
        groups = [int(g) for g in infostr.split(",")]
        for g in groups:
            for l in locs:
                if l in ".?":
                    pass

def solve_1_hn(lines):
    def count(cfg, nums):
        if cfg == "":
            return 1 if nums == () else 0

        if nums == ():
            return 0 if "#" in cfg else 1

        result = 0
        
        if cfg[0] in ".?":
            result += count(cfg[1:], nums)
            
        if cfg[0] in "#?":
            if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                result += count(cfg[nums[0] + 1:], nums[1:])

        return result

    total = 0

    for line in lines:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        total += count(cfg, nums)
    print(total)

def solve_2():
    pass

DAY = 12
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_file(filename)
solve_1_hn(lines)
