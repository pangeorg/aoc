from functools import cache
from typing import List

# this is too slow
def possible(design: str, patterns: List[str]):
    from collections import deque
    q = deque()
    q.append(([], design,))
    while q:
        p, d = q.popleft()
        for pattern in patterns:
            if d.startswith(pattern):
                n = d[len(pattern):]
                q.append((p + [pattern], n))
            check = "".join(p + [pattern])
            if check == design:
                return True

    return False


def solve1():
    import utils
    s = utils.read_lines("../input/day19.txt")
    patterns, designs = s[0], s[2:]
    print(len(designs))
    patterns = set(patterns.split(", "))
    maxl = max([len(p) for p in patterns])

    @cache
    def possible_cached(design):
        n = len(design)
        if not n:
            return True
        for i in range(min(n, maxl) + 1):
            if design[:i] in patterns and possible_cached(design[i:]):
                return True
        return False

    total = 0
    for d in designs:
        if possible_cached(d):
            total += 1
    # print(possible("bwurrg", patterns))

    print(total)

def solve2():
    import utils
    s = utils.read_lines("../input/day19.txt")
    patterns, designs = s[0], s[2:]
    print(len(designs))
    patterns = set(patterns.split(", "))
    maxl = max([len(p) for p in patterns])

    @cache
    def possible_cached(design):
        n = len(design)
        if not n:
            return 1
        count = 0
        for i in range(min(n, maxl) + 1):
            if design[:i] in patterns:
                count += possible_cached(design[i:])
        return count

    total = 0
    for d in designs:
        total += possible_cached(d)
    # print(possible("bwurrg", patterns))

    print(total)


solve2()
