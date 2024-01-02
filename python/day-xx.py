def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines

def solve_1():
    pass

def solve_2():
    pass

DAY = 10
test = True
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)
