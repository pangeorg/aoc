import utils

def solve1():
    lines = utils.read_lines("../input/day07.txt")
    from itertools import product, chain

    ops = ['+', '*', '||']
    opsm = {'+': lambda x, y: x+y, '*': lambda x, y: x*y}

    total = 0
    for line in lines:
        result, numlist = line.split(": ")
        result = int(result)
        nums = list(map(int, numlist.split(" ")))
        n = len(nums) - 1
        combs = list(product(ops, repeat=n))

        print(f"Need to find {result}")
        for comb in combs:
            calc = list(chain.from_iterable(zip(nums, comb)))
            calc.append(nums[-1])
            i = 0
            x = calc[i]
            while True:
                op = calc[i+1]
                y = calc[i+2]
                r = opsm[op](x, y)
                x = r
                i = i + 2
                if i == len(calc) - 1:
                    break
            if x == result:
                print("Found: ", calc, f"= {result}")
                total += result
                break
    print(total)

def solve2():
    lines = utils.read_lines("../input/day07.txt")
    from itertools import product, chain

    ops = ['+', '*', '||']
    opsm = {'+': lambda x, y: x+y, '*': lambda x, y: x*y, '||': lambda x, y: int(str(x) + str(y))}

    total = 0
    for line in lines:
        result, numlist = line.split(": ")
        result = int(result)
        nums = list(map(int, numlist.split(" ")))
        n = len(nums) - 1
        combs = list(product(ops, repeat=n))

        print(f"Need to find {result}")
        for comb in combs:
            calc = list(chain.from_iterable(zip(nums, comb)))
            calc.append(nums[-1])
            i = 0
            x = calc[i]
            while True:
                op = calc[i+1]
                y = calc[i+2]
                r = opsm[op](x, y)
                x = r
                i = i + 2
                if i == len(calc) - 1:
                    break
            if x == result:
                print("Found: ", calc, f"= {result}")
                total += result
                break
    print(total)


solve2()
