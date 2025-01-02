import utils
from typing import Dict, List


def solve1():
    lines = utils.read_lines("../input/day23.txt")
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

    total = 0
    for x in graph.keys():
        for y in graph.keys():
            for z in graph.keys():
                if x == y == z:
                    continue
                if y in graph[x] and z in graph[x] and y in graph[z]:
                    if y[0] == "t" or x[0] == "t" or z[0] == "t":
                        print(y, x, z)
                        total += 1
    print(total // 6)

# algorithm BronKerbosch2(R, P, X) is
#     if P and X are both empty then
#         report R as a maximal clique
#     choose a pivot vertex u in P ⋃ X
#     for each vertex v in P \ N(u) do
#         BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#         P := P \ {v}
#         X := X ⋃ {v}
def BronKerbosch2(r: set[str], p: set[str], x: set[str], graph: Dict[str, List[str]]):
    if len(p) == len(x) == 0:
        yield r
    pux = p.union(x)  # P u X
    if pux:
        u = pux.pop()
        nu: set[str] = set(graph[u])  # N(u)
        pnu = p - nu  # P \ N(u)
    else:
        pnu = set()
    for v in pnu:
        nv: set[str] = set(graph[v])  # N(v)
        a, b, c = r.union(set([v])), p.intersection(nv), x.intersection(nv)
        yield from BronKerbosch2(r=a, p=b, x=c, graph=graph)
        p.remove(v)
        x.add(v)

def TestBron():
    graph = {}
    graph['2'] = ['3', '5', '1']
    graph['1'] = ['5', '2']
    graph['6'] = ['4']
    graph['5'] = ['1', '2', '4']
    graph['3'] = ['4', '2']
    graph['4'] = ['6', '5', '3']

    r = list(BronKerbosch2(set(), set(graph.keys()), set(), graph))
    print(r)

def solve2():
    lines = utils.read_lines("../input/day23.txt")
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

    r = list(BronKerbosch2(set(), set(graph.keys()), set(), graph))
    best = r[0]
    for n in r[1:]:
        if len(n) > len(best):
            best = n
    print(",".join(list(sorted(best))))


solve2()
