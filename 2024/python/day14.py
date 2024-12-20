from functools import reduce
import utils

def read_robot_line(line):
    p, v = line.split(" ")
    p = tuple(map(int, p[2:].split(",")))
    v = tuple(map(int, v[2:].split(",")))
    return p, v


def solve1():
    with open("../input/day14.txt", "r") as f:
        lines = f.readlines()
    X = 101
    Y = 103

    robots = []
    for line in lines:
        p, v = read_robot_line(line)
        robots.append((p, v))

    time = 100
    positions = []
    for robot in robots:
        p, v = robot
        px = (p[0] + time * v[0]) % X
        py = (p[1] + time * v[1]) % Y
        positions.append((px, py))

    quadrants = [0, 0, 0, 0]
    for p in positions:
        if 0 <= p[0] < X//2 and 0 <= p[1] < Y//2:
            quadrants[0] += 1
        if X//2 < p[0] <= X and 0 <= p[1] < Y//2:
            quadrants[1] += 1
        if 0 <= p[0] < X//2 and Y//2 < p[1] <= Y:
            quadrants[2] += 1
        if X//2 < p[0] <= X and Y//2 < p[1] <= Y:
            quadrants[3] += 1

    total = reduce(lambda x, y: x * y, quadrants, 1)
    print(total)


def solve2():
    # this is based on hyperneutrinos assumption..... I wouldnt have guessed that....
    with open("../input/day14.txt", "r") as f:
        lines = f.readlines()
    X = 101
    Y = 103

    robots = []
    for line in lines:
        p, v = read_robot_line(line)
        robots.append((p, v))

    minimum = 999999999999999
    iteration = 0

    for s in range(X*Y):
        time = s
        positions = []
        for robot in robots:
            p, v = robot
            px = (p[0] + time * v[0]) % X
            py = (p[1] + time * v[1]) % Y
            positions.append((px, py))

        quadrants = [0, 0, 0, 0]
        for p in positions:
            if 0 <= p[0] < X//2 and 0 <= p[1] < Y//2:
                quadrants[0] += 1
            if X//2 < p[0] <= X and 0 <= p[1] < Y//2:
                quadrants[1] += 1
            if 0 <= p[0] < X//2 and Y//2 < p[1] <= Y:
                quadrants[2] += 1
            if X//2 < p[0] <= X and Y//2 < p[1] <= Y:
                quadrants[3] += 1

        total = reduce(lambda x, y: x * y, quadrants, 1)
        if total < minimum:
            minimum = total
            iteration = s
    print(iteration, minimum)


solve2()
