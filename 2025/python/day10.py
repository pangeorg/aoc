from dataclasses import dataclass
from utils import read_lines
from multiprocessing import Lock

example = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()


def as_mask(positions: tuple[int, ...], big: int):
    shifted = [1 << (big - p) for p in positions]
    v = shifted[0]
    if len(shifted) > 0:
        for s in shifted[1:]:
            v = v ^ s
    return v


@dataclass
class Machine:
    target_indicators: list[bool]
    buttons: list[tuple[int, ...]]
    joltage: list[int]


@dataclass
class BinaryMachine:
    target: int
    buttons: list[int]
    joltage: list[int]

    @classmethod
    def from_machine(cls, machine: Machine):
        b = "".join([str(i) for i in list(map(int, machine.target_indicators))])
        target = int(b, base=2)
        buttons = [
            as_mask(b, len(machine.target_indicators) - 1) for b in machine.buttons
        ]
        return BinaryMachine(target=target, buttons=buttons, joltage=machine.joltage)


def parse_line(line: str) -> Machine:
    right_bracket = line.find("]")
    left_brace = line.find("{")

    indicators = [c == "#" for c in line[1:right_bracket]]

    buttons = line[right_bracket + 1 : left_brace - 1].strip().split(" ")
    buttons = [b[1:-1] for b in buttons]
    buttons = [tuple(map(int, b.split(","))) for b in buttons]

    joltage = list(map(int, line[left_brace + 1 : len(line) - 1].split(",")))

    return Machine(
        target_indicators=indicators,
        buttons=buttons,
        joltage=joltage,
    )


def toggle(value: int, mask: int):
    return value ^ mask


def solve_machine_1(machine: Machine):
    from itertools import product

    m = BinaryMachine.from_machine(machine)
    target = m.target
    count = 1
    while True:
        for presses in product(m.buttons, repeat=count):
            i = 0
            for mask in presses:
                r = toggle(i, mask)
                if r == target:
                    return count
                i = r
        count += 1
    return -1


def solve_machine_2(machine: Machine):
    from functools import cache

    def decrease(joltage: tuple[int, ...], button: tuple[int, ...]):
        new_joltage = list(joltage)
        for b in button:
            new_joltage[b] -= 1
        return tuple(new_joltage)

    assert decrease((2, 2), (0, 1)) == (1, 1)

    target = tuple(machine.joltage)  # type: ignore

    # target = (2, 2)
    # machine.buttons = [(0, 1), (0,), (1,)]

    zeros = tuple(0 for _ in target)

    @cache
    def dp(state: tuple[int, ...]):
        # Return minimal additional presses to reach zeros from 'state'
        if any(x < 0 for x in state):
            return float("inf")
        if state == zeros:
            return 0

        # Quick infeasibility check: any positive counter with no button affecting it
        affected = [False] * len(target)
        for b in machine.buttons:
            for i in b:
                affected[i] = True
        if any(val > 0 and not affected[i] for i, val in enumerate(target)):
            return float("inf")

        best = min(dp(decrease(state, b)) + 1 for b in machine.buttons)
        return best

    c = dp(target)

    return c


def test_as_mask():
    assert 55 == as_mask((0, 1, 2, 4, 5), 5)
    assert 17 == as_mask((0, 4), 4)


def tests():
    target = int("110", base=2)
    value = 0
    buttons = [(0, 2), (0, 1)]
    buttons = [as_mask(b, 3) for b in buttons]
    for mask in buttons:
        t = toggle(value, mask)
        value = t
    print(target, value)
    print(f"{target:08b} {value:08b}")
    assert value == target

    target = int("00010", base=2)
    value = 0
    buttons = [
        (0, 4),
        (0, 1, 2),
        (1, 2, 3, 4),
    ]
    buttons = [as_mask(b, 4) for b in buttons]
    for mask in buttons:
        t = toggle(value, mask)
        value = t
    print(target, value)
    print(f"{target:08b} {value:08b}")
    assert value == target

    target = int("011101", base=2)
    value = 0
    buttons = [
        (0, 3, 4),
        (0, 1, 2, 4, 5),
    ]
    buttons = [as_mask(b, 5) for b in buttons]
    for mask in buttons:
        t = toggle(value, mask)
        value = t
    print(target, value)
    print(f"{target:08b} {value:08b}")
    assert value == target


def part1():
    lines = example.splitlines()
    lines = read_lines("../data/day10.txt")
    total = 0
    for line in lines:
        machine = parse_line(line)
        count = solve_machine_1(machine)
        total += count

    print(total)


lock = Lock()
_processed = 0
_total = 0


def update_processed():
    lock.acquire()
    try:
        global _processed
        _processed += 1
        print(f"{_processed}/{_total}")
    finally:
        lock.release()


def process_and_solve(line):
    machine = parse_line(line)
    count = solve_machine_2(machine)
    update_processed()
    return count


def part2():
    from multiprocessing import Pool

    global _total

    lines = example.splitlines()
    lines = read_lines("../data/day10.txt")
    _total = len(lines)
    print(f"# of lines: {_total}")
    with Pool(1) as p:
        results = p.map(process_and_solve, lines)

    print(sum(results))


part2()
