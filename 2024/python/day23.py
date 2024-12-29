import utils


def solve1():
    lines = utils.read_lines("../input/sample23.txt")
    # map node: [node]
    graph = {}
    for line in lines:
        l, r = line.split("-")
        if l not in graph:
            graph[l] = set([r])
        else:
            graph[l].add(r)

        if r not in graph:
            graph[r] = set([l])
        else:
            graph[r].add(l)

    sets = set()
    for start in graph.keys():
        s = [start]
        for k, v in graph.items():
            if k == start:
                continue
            if start in v:
                s.append(k)
            if len(s) == 3:
                sets.add(tuple(s))
                s = [start]

    for s in sorted(sets):
        print(s)


solve1()
