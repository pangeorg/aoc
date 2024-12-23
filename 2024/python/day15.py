import utils
from collections import deque

dir_map = {
    '>': utils.E,
    '<': utils.W,
    'v': utils.S,
    '^': utils.N,
}

def solve1():
    with open("../input/day15.txt", "r") as f:
        text = f.read()
    movements_text = text.split("\n\n")[-1]
    movements = "".join(movements_text.split("\n"))
    lines = text.split("\n\n")[0].split("\n")

    grid = utils.LineGrid(lines)
    start = grid.find(lambda x: x == "@")

    if start is None:
        raise Exception("aaaq")

    current = start
    for move in movements:
        next = utils.take_step(current, dir_map[move])
        if grid[next] == "#":
            continue
        if grid[next] == ".":
            grid[next] = "@"
            grid[current] = "."
            current = next
            continue
        if grid[next] == "O":
            next_robot_pos = next
            while grid[next] == "O":
                next = utils.take_step(next, dir_map[move])
            if grid[next] == "#":
                continue
            if grid[next] != ".":
                raise Exception("something not .")
            grid[next] = "O"
            grid[current] = "."
            grid[next_robot_pos] = "@"
            current = next_robot_pos

    boxes = grid.find_all(lambda x: x == "O")
    total = 0
    for box in boxes:
        total += (box[0] + 100 * box[1])
    print(total)


def solve2():
    with open("../input/day15.txt", "r") as f:
        text = f.read()
    movements_text = text.split("\n\n")[-1]
    movements = "".join(movements_text.split("\n"))
    lines = text.split("\n\n")[0].split("\n")

    new_lines = []
    for line in lines:
        new_line = line.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")
        new_lines.append(new_line)

    grid = utils.LineGrid(new_lines)
    start = grid.find(lambda x: x == "@")

    if start is None:
        raise Exception("aaaa")

    def get_other_box_side(start):
        if grid[start] == "]":
            return utils.take_step(start, utils.W)
        elif grid[start] == "[":
            return utils.take_step(start, utils.E)
        else:
            raise Exception("[][][][[[][]")

    def box_move(start, dir, grid):
        q = deque([start])
        to_move = [start]

        if dir in [utils.N, utils.S]:
            other = get_other_box_side(start)
            q.append(other)
            to_move.append(other)

        while len(q) != 0:
            c = q.popleft()
            n = utils.take_step(c, dir)
            if grid[n] == "#":
                return False
            if grid[n] in "[]":
                q.append(n)
                if n not in to_move:
                    to_move.append(n)
                if dir in [utils.N, utils.S]:
                    other = get_other_box_side(n)
                    q.append(other)
                    if other not in to_move:
                        to_move.append(other)
            if len(q) == 0:
                break

        for p in to_move[::-1]:
            n = utils.take_step(p, dir)
            grid[n] = grid[p]
            grid[p] = "."

        return True

    grid.print()

    current = start
    for move in movements:
        # print(10*"=" + move)
        next = utils.take_step(current, dir_map[move])
        if grid[next] == ".":
            grid[next] = "@"
            grid[current] = "."
            current = next
        if grid[next] in "[]":
            if box_move(next, dir_map[move], grid):
                grid[current] = "."
                grid[next] = "@"
                current = next
        # grid.print()

    boxes = grid.find_all(lambda x: x == "[")
    total = 0
    for box in boxes:
        total += (box[0] + 100 * box[1])
    print(total)


solve2()
