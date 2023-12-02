from pprint import pprint

def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def get_dict():
    return {"red": 0, "green": 0, "blue": 0}

def parse_file(lines):
    games = {}
    for l in lines:
        l_split = l.replace("\n", "").split(": ")
        game = l_split[0]
        games[game] = []
        rounds = l_split[-1].split(";")
        for rnd in rounds:
            draws = get_dict()
            ncolors = rnd.split(",")
            for nc in ncolors:
                cc = nc.strip().split(" ")
                color = cc[-1]
                n = cc[0]
                draws[color] = int(n)
            games[game].append(draws)
    return games

def part_1(games):
    maxs = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for k, game in games.items():
        id_game = int(k.split(" ")[-1])
        possible = True
        for rounds in game:
            for color, count in rounds.items():
                if count > maxs[color]:
                    possible = False
        if possible:
            result += id_game
    return result

def part_2(games):
    result = 0
    for game in games.values():
        maxs = get_dict()
        for rounds in game:
            for color, count in rounds.items():
                maxs[color] = max(maxs[color], count)
        power = 1
        for count in maxs.values():
            power *= count
        result += power

    return result

test = False
if test:
    path = "../../data/sample-02-01.txt"
else:
    path = "../../data/day-02.txt"

lines = read_file(path)
games = parse_file(lines)
result_1 = part_1(games)
result_2 = part_2(games)

if test:
    assert result_1 == 8
    assert result_2 == 2286

print("Result 1: ", result_1)
print("Result 2: ", result_2)

