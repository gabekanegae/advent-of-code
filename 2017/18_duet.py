########################
# --- Day 18: Duet --- #
########################

import AOCUtils
from collections import deque

class Program:
    def __init__(self, code, pid, in_buffer=None):
        self.pc = 0
        self.code = code
        self.registers = {'p': pid}

        self.in_buffer = in_buffer
        self.out_buffer = deque()
        self.out_count = 0

        self.blocked = False

    def run(self):
        while self.pc < len(self.code):
            cmd = self.code[self.pc].split()

            inst = cmd[0]

            x = cmd[1]
            if x.isalpha() and x not in self.registers:
                self.registers[x] = 0
            x_val = int(x) if not x.isalpha() else self.registers[x]

            if len(cmd) > 2:
                y = cmd[2]
                if y.isalpha() and y not in self.registers:
                    self.registers[y] = 0
                y_val = int(y) if not y.isalpha() else self.registers[y]

            if inst == 'snd':
                self.out_buffer.append(x_val)
                self.out_count += 1
            elif inst == 'set':
                self.registers[x] = y_val
            elif inst == 'add':
                self.registers[x] += y_val
            elif inst == 'mul':
                self.registers[x] *= y_val
            elif inst == 'mod':
                self.registers[x] %= y_val
            elif inst == 'rcv':
                if self.in_buffer:
                    self.registers[x] = self.in_buffer.popleft()
                else:
                    self.blocked = True
                    break
            elif inst == 'jgz':
                if x_val > 0:
                    self.pc += y_val - 1

            self.pc += 1

########################

code = AOCUtils.load_input(18)

p0 = Program(code, 0)
p0.run()

AOCUtils.print_answer(1, p0.out_buffer[-1])

p0 = Program(code, 0)
p1 = Program(code, 1)

p0.in_buffer = p1.out_buffer
p1.in_buffer = p0.out_buffer

while not (p0.blocked and not p0.out_buffer and p1.blocked and not p1.out_buffer):
    p0.run()
    p1.run()

AOCUtils.print_answer(2, p1.out_count)

AOCUtils.print_time_taken()