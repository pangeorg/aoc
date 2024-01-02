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

def transpose_grid(lines):
    return list(zip(*lines))

class LineGrid:
    def __init__(self, lines):
        """
        lines should come from 'read_lines'
        """
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def __getitem__(self, coords):
        return self.lines[coords[1]][coords[0]]

    def __repr__(self):
        return f"LineGrid({self.width, self.height})\n" + "\n".join(self.lines)

    def __str__(self):
        return "\n".join(self.lines)

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
        t = transpose_grid(self.lines)
        for i in range(len(t)):
            t[i] = "".join(t[i])
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

