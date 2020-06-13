#############################################
# --- Day 8: I Heard You Like Registers --- #
#############################################

import AOCUtils

class Instruction:
    def __init__(self, inst):
        inst = inst.split()

        self.reg = inst[0]
        self.mul = {"inc": 1, "dec": -1}[inst[1]]
        self.val = int(inst[2])
        self.condReg = inst[4]
        self.cond = inst[5]
        self.condVal = int(inst[6])

    def meetsCondition(self, regs):
        conditions = {">": lambda x, y: x > y,
                      "<": lambda x, y: x < y,
                      ">=": lambda x, y: x >= y,
                      "<=": lambda x, y: x <= y,
                      "==": lambda x, y: x == y,
                      "!=": lambda x, y: x != y}

        return conditions[self.cond](regs.get(self.condReg, 0), self.condVal)

#############################################

instructions = [Instruction(inst) for inst in AOCUtils.loadInput(8)]

registers = dict()

maxEver = 0
for inst in instructions:
    if inst.meetsCondition(registers):
        if inst.reg not in registers:
            registers[inst.reg] = 0

        registers[inst.reg] += inst.mul * inst.val
        maxEver = max(maxEver, registers[inst.reg])

print("Part 1: {}".format(max(registers.values())))

print("Part 2: {}".format(maxEver))

AOCUtils.printTimeTaken()