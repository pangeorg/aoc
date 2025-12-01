# directions on a grid where 0, 0 is top left corner
N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
NE, NW, SE, SW = (1, -1), (-1, -1), (1, 1), (-1, 1)

DIRS = [N, S, E, W, NE, NW, SE, SW]

REVERSE_DIR = {
    N: S,
    S: N,
    W: E,
    E: W,
    NE: SW,
    SW: NE,
    SE: NW,
    SW: NE,
    NW: SE,
    NE: SW,
}


def read_filestr(filename):
    """
    Read whole file as str
    """
    with open(filename, 'r') as f:
        return f.read()


def read_lines(filename):
    """
    Read lines from file
    """
    return read_filestr(filename).splitlines()


def read_lines_groups(filename, pattern="\n\n"):
    blocks = read_filestr(filename).split(pattern)
    return [b.splitlines() for b in blocks]


def grid_transpose(lines):
    return list(list(x) for x in zip(*lines))


def grid_rotate_right(lines):
    return [list(reversed(x)) for x in zip(*lines)]


def point_rotate_right(point: tuple[int, int]):
    n = complex(point[0], point[1])
    n = n * 1j
    return (int(n.real), int(n.imag))


def point_rotate_left(point: tuple[int, int]):
    n = complex(point[0], point[1])
    n = n * -1j
    return (int(n.real), int(n.imag))


def grid_rotate_left(lines):
    return list(reversed([list(x) for x in zip(*lines)]))


def take_step(point: tuple[int, int], direction: tuple[int, int], count: int = 1):
    return (point[0] + direction[0] * count, point[1] + direction[1] * count,)


def neighbors(point: tuple[int, int]):
    return [take_step(point, dir) for dir in [N, W, S, E]]


def distance_path(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class LineGrid:
    def __init__(self, lines):
        """
        lines should come from 'read_lines'
        """
        # mae each char its own point in the grid
        self.lines = [[c for c in line] for line in lines]
        self.width = len(lines[0])
        self.height = len(lines)
        self.rows = self.height
        self.cols = self.width

    def __getitem__(self, coords):
        """ assumes x, y coordinates where 0,0 is top-left corner"""
        return self.lines[coords[1]][coords[0]]

    def __setitem__(self, coords, value):
        """ assumes x, y coordinates where 0,0 is top-left corner"""
        self.lines[coords[1]][coords[0]] = value

    def __repr__(self):
        return f"LineGrid({self.width, self.height})\n" + self.__str__()

    def __str__(self):
        return "\n".join(["".join(str(line)) for line in self.lines])

    def print(self):
        for line in self.lines:
            print("".join(line))

    def has_point(self, point):
        return 0 <= point[0] < self.width and 0 <= point[1] < self.height

    def find(self, condition):
        for x in range(self.width):
            for y in range(self.height):
                if condition(self[(x, y)]):
                    return x, y
        return None

    def find_all(self, condition):
        r = []
        for x in range(self.width):
            for y in range(self.height):
                if condition(self[(x, y)]):
                    r.append((x, y, ))
        return r

    def transpose(self):
        t = grid_transpose(self.lines)
        return LineGrid(t)

    def get_region(self, start, condition=None):
        """Flood fill to get region with same entry in start"""
        from collections import deque
        if not condition:
            def condition(p): return self[p] == self[start]
        result = set()
        visited = set()
        queue = deque([start])
        while True:
            parcel = queue.popleft()
            visited.add(parcel)
            if not self.has_point(parcel):
                continue
            if condition(parcel):
                result.add(parcel)
                for next in neighbors(parcel):
                    if not self.has_point(next) or next in visited:
                        continue
                    queue.insert(0, next)
            if len(queue) == 0:
                break

        return result


if __name__ == "__main__":
    print("Running tests...")
    lines = read_lines_groups("../data/tests.txt")[0]
    g = LineGrid(lines)
    assert g[0, 0] == "#"
    t = g.transpose()
    print(t)
