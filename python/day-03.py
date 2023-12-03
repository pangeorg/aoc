from functools import reduce
import operator

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([c for c in line if c != "\n"])
    return grid

def print_grid(grid):
    for row in grid:
        print([r for r in row])


## for whatever reason this does not work
def solve_1(grid):
    xmax = len(grid[0]) - 1
    ymax = len(grid) - 1
    nums = []
    valid_nums = []
    for iy, row in enumerate(grid):
        current_num = ""
        current_valid = False
        for ix, char in enumerate(row):
            if char.isdigit():
                current_num += char
                # check surroundings
                # we can improve here to not check (0, 0) e.g.
                for check_y in [-1, 0, 1]:
                    for check_x in [-1, 0, 1]:
                        y = min(max(iy+check_y, 0), ymax)
                        x = min(max(ix+check_x, 0), xmax)
                        check_char = grid[y][x]
                        if check_char != "." and not check_char.isdigit():
                            # found symbol
                            current_valid = True
            if (not (char.isdigit()) or ix == xmax) and current_num:
                new_num = int(current_num)
                nums.append(new_num)
                valid_nums.append(current_valid)
                current_num = ""
                current_valid = False

    result = 0
    for iy, n in enumerate(nums):
        if valid_nums[iy]:
            result += n
    return result

def take_num(x, y, grid):
    num = ""
    # walk backwards first
    xmin = x
    while xmin >= 0:
        if not grid[y][xmin].isdigit():
            break
        xmin -= 1
    for xx in range(xmin + 1, len(grid[0])):
        if not grid[y][xx].isdigit():
            break
        num = num + grid[y][xx]
        grid[y][xx] = "."
    return num


def solve_2(grid):
    gears = {}
    xmax = len(grid[0]) - 1
    ymax = len(grid) - 1
    nums = []
    for iy, row in enumerate(grid):
        for ix, char in enumerate(row):
            if char == "*":
                gears[(ix, iy,)] = []
                for check_y in [-1, 0, 1]:
                    for check_x in [-1, 0, 1]:
                        y = min(max(iy+check_y, 0), ymax)
                        x = min(max(ix+check_x, 0), xmax)
                        if grid[y][x].isdigit():
                            num = take_num(x, y, grid)
                            gears[(ix, iy)].append(num)
    result = 0
    for _, nums in gears.items():
        if len(nums) > 1:
            ratio = reduce(operator.mul, [int(n) for n in nums], 1)
            result += ratio
    return result

test = False
if test:
    filename = "../data/sample-03-01.txt"
else:
    filename = "../data/day-03.txt"

grid = read_file(filename)
result1 = solve_1(grid)

if test:
    assert result1 == 4361, f"Expected: 4361 but got {result1}"
else:
    print(f"Result 1: {result1}")


result2 = solve_2(grid)

if test:
    assert result2 == 467835, f"Expected: 467835 but got {result2}"
else:
    print(f"Result 2: {result2}")

