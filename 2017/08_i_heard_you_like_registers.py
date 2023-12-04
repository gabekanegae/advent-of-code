#############################################
# --- Day 8: I Heard You Like Registers --- #
#############################################

import AOCUtils

class Instruction:
    def __init__(self, inst):
        inst = inst.split()

        self.reg = inst[0]
        self.mul = {'inc': 1, 'dec': -1}[inst[1]]
        self.val = int(inst[2])
        self.cond_reg = inst[4]
        self.cond = inst[5]
        self.cond_val = int(inst[6])

    def meets_condition(self, regs):
        conditions = {'>': lambda x, y: x > y,
                      '<': lambda x, y: x < y,
                      '>=': lambda x, y: x >= y,
                      '<=': lambda x, y: x <= y,
                      '==': lambda x, y: x == y,
                      '!=': lambda x, y: x != y}

        return conditions[self.cond](regs.get(self.cond_reg, 0), self.cond_val)

#############################################

raw_instructions = AOCUtils.load_input(8)
instructions = list(map(Instruction, raw_instructions))

registers = dict()

max_ever = 0
for inst in instructions:
    if inst.meets_condition(registers):
        registers[inst.reg] = registers.get(inst.reg, 0) + inst.mul*inst.val
        max_ever = max(max_ever, registers[inst.reg])

AOCUtils.print_answer(1, max(registers.values()))

AOCUtils.print_answer(2, max_ever)

AOCUtils.print_time_taken()