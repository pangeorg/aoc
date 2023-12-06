
import math
from functools import reduce
from operator import mul

def read_file(filename):
    import re
    with open(filename, "r") as f:
        lines = f.readlines()

    def get_data(line):
        data = line.split(":")[-1]
        data = data.strip().split(" ")
        data = [int(s.strip()) for s in data if s.strip() != ""]
        return data
    
    return get_data(lines[0]), get_data(lines[1])

def get_winning(time, distance):

    x = lambda wait: wait * (time - wait)
    distances = []
    for w in range(time):
        d = x(w)
        if d > distance:
            distances.append(d)
    return len(distances)

def get_winning_alaytic(time, distance):

    hit1 = -0.5 +  math.sqrt(time**2 - 4 * distance) / 2
    hit2 = -0.5 -  math.sqrt(time**2 - 4 * distance) / 2
    
    print("====")
    hit1 = (math.ceil(hit1))
    hit2 = round(hit2)
    print(int(math.ceil(hit1 - hit2)))
    
get_winning_alaytic(7, 9)
get_winning_alaytic(15, 40)
get_winning_alaytic(30, 200)

def solve_1(times, distances):
    wins = [get_winning(t, d) for t, d in zip(times, distances)]
    print(reduce(mul, wins, 1))

def solve_2(times, distances):
    def to_str(x):
        s = "".join([str(xx) for xx in x])
        return int(s)
    time = to_str(times)
    distance = to_str(distances)
    d = get_winning(time, distance)
    print(d)

def solve_2_analytic(times, distances):
    def to_str(x):
        s = "".join([str(xx) for xx in x])
        return int(s)
    time = to_str(times)
    distance = to_str(distances)
    get_winning_alaytic(time, distance)


test = False
if test:
    filename = "../data/sample-06.txt"
else:
    filename = "../data/day-06.txt"

times, dist = read_file(filename)
solve_1(times, dist)
solve_2_analytic(times, dist)

