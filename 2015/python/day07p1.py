lines = open("../input/day07.txt").readlines()
lines = [l.strip() for l in lines]

instructions = {}
for line in lines:
    split = line.split(' -> ')
    out = split[-1]
    instr = split[0].split(" ")
    if len(instr) == 1:
        instructions[out] = "", "SET", instr[0]
    elif len(instr) == 2:
        instructions[out] = "", "NOT", instr[1]
    else:
        print(instr)
        left, op, right = instr
        instructions[out] = left, op, right


def calculate(out) -> int:
    def getValue(value) -> int:
        try:
            return int(value)
        except Exception:
            return calculate(value)

    left, op, right = instructions[out]
    if op == "SET":
        return getValue(right)
    elif op == "NOT":
        return ~calculate(right)
    elif op == "LSHIFT":
        return getValue(left) << getValue(right)
    elif op == "RSHIFT":
        return getValue(left) >> getValue(right)
    elif op == "RSHIFT":
        return getValue(left) | getValue(right)
    elif op == "AND":
        return getValue(left) & getValue(right)
    else:
        raise Exception("Unknown op " + op)


print(calculate('i'))
