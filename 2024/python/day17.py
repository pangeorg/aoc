from dataclasses import dataclass
from os import initgroups
import re
from typing import List


@dataclass
class Registers:
    A: int
    B: int
    C: int

    def zero(self):
        return self.A == self.B == self.C == 0


def combo(operand: int, regs: Registers):
    match (operand):
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return regs.A
        case 5:
            return regs.B
        case 6:
            return regs.C
        case _:
            raise Exception("77777")


class Programm:
    def __init__(self, regs: Registers, instructions: List[int]):
        self.regs = regs
        self.instructions = instructions
        self.ip = 0  # instruction pointer
        self.output = []
        self.instruction_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def debug_print(self):
        print("A: ", self.regs.A)
        print("B: ", self.regs.B)
        print("C: ", self.regs.C)
        print(",".join([str(i) for i in self.instructions]))
        s = "  " * self.ip + "^"
        print(s)
        print("output: ", self.output)
        print("----------")

    def run(self, debug=True):
        while self.ip < len(self.instructions):
            if debug:
                self.debug_print()
            i, op = self.instructions[self.ip], self.instructions[self.ip + 1]
            f = self.instruction_map[i]
            f(op)

    def adv(self, operand: int):
        self.regs.A //= 2**combo(operand, self.regs)
        self.ip += 2

    def bxl(self, operand: int):
        self.regs.B ^= operand
        self.ip += 2

    def bst(self, operand: int):
        self.regs.B = combo(operand, self.regs) % 8
        self.ip += 2

    def jnz(self, operand: int):
        if self.regs.A != 0:
            self.ip = operand
        else:
            self.ip += 2

    def bxc(self, operand: int):
        _ = operand
        self.regs.B ^= self.regs.C
        self.ip += 2

    def out(self, operand: int):
        self.output.append(combo(operand, self.regs) % 8)
        self.ip += 2

    def bdv(self, operand: int):
        self.regs.B = self.regs.A // (2**combo(operand, self.regs))
        self.ip += 2

    def cdv(self, operand: int):
        self.regs.C = self.regs.A // (2**combo(operand, self.regs))
        self.ip += 2

    def print(self):
        print(",".join([str(i) for i in self.output]))


def num_from_list(values: List[int]):
    if len(values) != 16:
        raise Exception()
    return sum([v*8**i for i, v in enumerate(values)])


def solve1():
    import utils

    reginfo, inst = utils.read_filestr("../input/day17.txt").split("\n\n")
    reginfo = list(map(int, [r.split()[-1] for r in reginfo.split("\n")]))
    inst = list(map(int, inst.replace("Program: ", "").split(",")))

    regs = Registers(*reginfo)
    prog = Programm(regs, inst)
    prog.run(True)
    prog.print()


def solve2():
    import utils

    reginfo, inst = utils.read_filestr("../input/day17.txt").split("\n\n")
    reginfo = list(map(int, [r.split()[-1] for r in reginfo.split("\n")]))
    inst = list(map(int, inst.replace("Program: ", "").split(",")))

    regs = Registers(*reginfo)
    num = [0 for _ in range(len(inst))]
    pos = 0
    while pos < len(inst):
        for i in range(0, 8):
            num[pos] = i
            regs = Registers(A=num_from_list(num), B=0, C=0)
            prog = Programm(regs, inst)
            prog.run(False)
            if len(prog.output) != len(inst):
                continue
            if prog.output[pos] == inst[pos]:
                break
        # if prog.output[pos] != inst[pos]:
        #     print("err", i, pos)
        #     break
        pos += 1

    num = [7, 7, 4, 7, 0, 1, 1, 0, 7, 3, 5, 3, 2, 2, 3, 5]
    n = num_from_list(num)
    n = sum([7*8**i for i in range(len(inst))]) + 1
    regs = Registers(A=n, B=0, C=0)
    while True:
        prog = Programm(regs, inst)
        prog.run(False)
        if prog.output == inst:
            break
        add = 0
        for i in range(len(inst) - 1, -1, -1):
            if prog.output[i] != inst[i]:
                add = 8**i
                regs.A += add
                break
    print(num)
    print(prog.output)
    print(inst)


solve2()
