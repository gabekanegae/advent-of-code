###########################################
# --- Day 23: Opening the Turing Lock --- #
###########################################

import AOCUtils

class VM:
    def __init__(self, program):
        self.program = program[:]
        self.pc = 0
        self.registers = {'a': 0, 'b': 0}

    def run(self):
        while self.pc < len(self.program):
            cmd = self.program[self.pc].split()

            inst = cmd[0]

            x = cmd[1].rstrip(',')
            y = cmd[2] if len(cmd) > 2 else None

            if inst == 'hlf':
                self.registers[x] //= 2
            elif inst == 'tpl':
                self.registers[x] *= 3
            elif inst == 'inc':
                self.registers[x] += 1
            elif inst == 'jmp':
                self.pc += int(x) - 1
            elif inst == 'jie':
                if self.registers[x] % 2 == 0:
                    self.pc += int(y) - 1
            elif inst == 'jio':
                if self.registers[x] == 1:
                    self.pc += int(y) - 1

            self.pc += 1

#######################################

program = AOCUtils.load_input(23)

vm = VM(program)
vm.run()
AOCUtils.print_answer(1, vm.registers['b'])

vm = VM(program)
vm.registers['a'] = 1
vm.run()
AOCUtils.print_answer(2, vm.registers['b'])

AOCUtils.print_time_taken()