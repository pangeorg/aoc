
def solve1():
    import utils
    line = utils.read_lines("../input/day11.txt")[0]
    values = [int(v) for v in line.split(" ")]

    # values = [125, 17]

    nblinks = 25
    while nblinks > 0:
        new = []
        for v in values:
            v_str = str(v)
            if v == 0:
                v = 1
                new.append(v)
            elif len(v_str) % 2 == 0:
                new.append(int(v_str[:len(v_str)//2]))
                new.append(int(v_str[len(v_str)//2:]))
            else:
                v = v * 2024
                new.append(v)
        values = new
        nblinks = nblinks - 1
    print(len(values))

def solve2():
    import utils

    line = utils.read_lines("../input/day11.txt")[0]
    values = [int(v) for v in line.split(" ")]

    cache = {}

    def pebble_count(pebble, blinks):
        if (pebble, blinks) in cache:
            return cache[(pebble, blinks)]
        if blinks == 0:
            return 1
        if pebble == 0:
            c = pebble_count(1, blinks - 1)
            cache[(pebble, blinks)] = c
            return c

        pebble_str = str(pebble)
        if len(pebble_str) % 2 == 0:
            v1 = int(pebble_str[:len(pebble_str)//2])
            v2 = int(pebble_str[len(pebble_str)//2:])
            c1, c2 = pebble_count(v1, blinks - 1), pebble_count(v2, blinks - 1)
            cache[(pebble, blinks)] = c1 + c2
            return c1 + c2

        c = pebble_count(pebble * 2024, blinks - 1)
        cache[(pebble, blinks)] = c
        return c

    t = 0
    blinks = 75
    for v in values:
        t += pebble_count(v, blinks)
    print(t)


solve2()
