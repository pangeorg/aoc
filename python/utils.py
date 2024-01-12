# directions on a grid where 0, 0 is top left corner
N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
NE, NW, SE, SW = (1, -1), (-1, -1), (1, 1), (-1, 1)

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

def grid_rotate_left(lines):
    return list(reversed([list(x) for x in zip(*lines)]))

def take_step(point: tuple[int, int], direction: tuple[int, int]):
    return (point[0] + direction[0], point[1] + direction[1],)


class LineGrid:
    def __init__(self, lines):
        """
        lines should come from 'read_lines'
        """
        # mae each char its own point in the grid
        self.lines = [[c for c in l] for l in lines]
        self.width = len(lines[0])
        self.height = len(lines)

    def __getitem__(self, coords):
        """ assumes x, y coordinates where 0,0 is top-left corner"""
        return self.lines[coords[1]][coords[0]]

    def __setitem__(self, coords, value):
        """ assumes x, y coordinates where 0,0 is top-left corner"""
        print(coords)
        self.lines[coords[1]][coords[0]] = value

    def __repr__(self):
        return f"LineGrid({self.width, self.height})\n" + self.__str__()

    def __str__(self):
        return "\n".join(["".join(l) for l in self.lines])

    def has_point(self, point):
        return 0 <= point[0] < self.width and 0 <= point[1] < self.height

    def find(self, condition):
        for x in range(self.width):
            for y in range(self.height):
                if condition(self[x, y]):
                    return x, y
        return False

    def find_all(self, condition):
        r = []
        for x in range(self.width):
            for y in range(self.height):
                if condition(self[x, y]):
                    r.append((x, y, ))
        return r

    def transpose(self):
        t = grid_transpose(self.lines)
        try:
            return LineGrid(t)
        except:
            print("Cannot transpose")
            raise

if __name__ == "__main__":
    print("Running tests...")
    lines = read_lines_groups("../data/tests.txt")[0]
    g = LineGrid(lines)
    assert g[0,0] == "#"
    t = g.transpose()
    print(t)

