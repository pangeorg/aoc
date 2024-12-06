import os
import sys
import functools

path = os.path.abspath(os.path.dirname(__file__) + "/..")
sys.path.append(path)

def unsorted(update, rules):
    needs_sorting = False
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            cmp1 = update[i]
            cmp2 = update[j]
            for rule in rules:
                if cmp1 in rule and cmp2 in rule:
                    if rule[0] != cmp1:
                        needs_sorting = True
    return needs_sorting


def solve_1():
    import utils

    lines = utils.read_lines_groups("sample.txt")
    rules = [list(map(int, rule.split('|'))) for rule in lines[0]]
    updates = [list(map(int, rule.split(','))) for rule in lines[1]]

    result = 0
    for update in updates:
        if not unsorted(update, rules):
            result += update[len(update)//2]

def solve_2():
    import utils

    lines = utils.read_lines_groups("part1.txt")
    rules = [list(map(int, rule.split('|'))) for rule in lines[0]]
    updates = [list(map(int, rule.split(','))) for rule in lines[1]]

    rules_d = {}
    for r in rules:
        rules_d[tuple(r)] = -1
        rules_d[(r[1], r[0])] = 1

    def cmp(x1, x2):
        r = rules_d.get((x1, x2), 0)
        if r is None:
            return 0
        return r

    result = 0
    for update in updates:
        if unsorted(update, rules):
            u = sorted(update, key=functools.cmp_to_key(cmp))
            result += u[len(u)//2]
            print(update, u)
    print(result)


solve_2()
