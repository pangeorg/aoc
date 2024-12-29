from functools import cache
from collections import defaultdict
from array import array


def mix(number: int, value: int):
    return number ^ value


def prune(number: int):
    return number % 16777216


@cache
def calculate(number: int):
    result = number * 64
    number = mix(number, result)
    number = prune(number)

    result = number // 32
    number = mix(number, result)
    number = prune(number)

    result = number * 2048
    number = mix(number, result)
    return prune(number)


assert prune(100000000) == 16113920, "prune is wrong"
assert mix(42, 15) == 37, "mix is wrong"
assert calculate(123) == 15887950
assert calculate(15887950) == 16495136


def simulate(number: int, times: int):
    prices = array('i')
    prices.append(number % 10)

    for i in range(times):
        number = calculate(number)
        prices.append(number % 10)

    # mapping sequences: max price
    sequences = {}
    for i in range(len(prices) - 4):
        a, b, c, d, e = prices[i: i + 5]
        k = (b - a, c - b, d - c, e - d)
        if k in sequences:
            continue
        sequences[k] = e

    return sequences


def test(num):
    seq_to_total = {}
    buyer = [num % 10]
    for _ in range(20):
        num = calculate(num)
        buyer.append(num % 10)
    seen = set()
    for i in range(len(buyer) - 4):
        a, b, c, d, e = buyer[i:i + 5]
        seq = (b - a, c - b, d - c, e - d)
        if seq in seen:
            continue
        seen.add(seq)
        if seq not in seq_to_total:
            seq_to_total[seq] = 0
        seq_to_total[seq] += e
    return seq_to_total


def solve(number):
    seqs = {}
    for k, v in (simulate(number, 20)).items():
        if k not in seqs:
            seqs[k] = 0
        seqs[k] += v
    return seqs


def solve1():
    import utils
    lines = utils.read_lines("../input/day22.txt")
    total = 0
    for line in lines:
        number = int(line)
        for _ in range(2000):
            number = calculate(number)
        total += number
    print(total)


def solve2():
    import utils
    lines = utils.read_lines("../input/day22.txt")
    seqs = defaultdict(lambda: 0)
    for line in lines:
        number = int(line)
        for k, v in (simulate(number, 2000)).items():
            seqs[k] += v
    print(max(seqs.values()))


solve2()
