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

def read_lines_groups(filename, pattern):
    blocks = read_filestr(filename).split(pattern)
    return [b.splitlines() for b in blocks]
