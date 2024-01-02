from collections import OrderedDict

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [l.replace("\n", "") for l in lines]

    directions = lines[0]
    node_lines = lines[2:]
    nodes = OrderedDict()

    for nl in node_lines:
        start = nl.split(" = ")[0]
        dirs = nl.split(" = ")[1].replace(")", "").replace("(", "")
        left = dirs.split(",")[0].strip()
        right = dirs.split(",")[1].strip()
        nodes[start] = (left, right,)

    return directions, nodes

def solve_1(filename):
    directions, nodes = read_file(filename)
    key = "AAA"
    current = nodes[key]
    i = 0
    steps = 0
    while key != "ZZZ":
        if i == len(directions):
            i = 0
        direction = directions[i]

        if direction == "L":
            key = current[0]
        else:
            key = current[1]

        current = nodes[key]

        steps += 1
        i += 1
    print(steps)


def solve_2(filename):
    directions, nodes = read_file(filename)
    ndirs = len(directions)
    keys = [k for k in nodes.keys() if k.endswith("A")]
    current = nodes[keys[0]]
    first = nodes[keys[0]]
    i = 0
    steps = 0
    sl = []
    while True:
        if i == ndirs:
            i = 0
        direction = directions[i]

        if direction == "L":
            key = current[0]
        else:
            key = current[1]

        current = nodes[key]

        steps += 1
        i += 1
        if first == current:
            print(steps)
            sl.append(steps)
            print([sl[i+1]/sl[i] for i in range(len(sl)-1)])
    print(steps)

DAY = 8
test = False
if test:
    filename = r"..\data\sample-{:02d}.txt".format(DAY)
else:
    filename = r"..\data\day-{:02d}.txt".format(DAY)

# solve_1(filename)
solve_2(filename)
