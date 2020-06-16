########################
# --- Day 18: Duet --- #
########################

import AOCUtils
from collections import deque

class Program:
    def __init__(self, code, pid, inBuffer=None):
        self.pc = 0
        self.code = code
        self.registers = {"p": pid}

        self.inBuffer = inBuffer
        self.outBuffer = deque()
        self.outCount = 0

        self.blocked = False

    def run(self):
        while self.pc < len(self.code):
            cmd = self.code[self.pc].split()

            inst = cmd[0]

            x = cmd[1]
            if x.isalpha() and x not in self.registers:
                self.registers[x] = 0
            xVal = int(x) if not x.isalpha() else self.registers[x]

            if len(cmd) > 2:
                y = cmd[2]
                if y.isalpha() and y not in self.registers:
                    self.registers[y] = 0
                yVal = int(y) if not y.isalpha() else self.registers[y]

            if inst == "snd":
                self.outBuffer.append(xVal)
                self.outCount += 1
            elif inst == "set":
                self.registers[x] = yVal
            elif inst == "add":
                self.registers[x] += yVal
            elif inst == "mul":
                self.registers[x] *= yVal
            elif inst == "mod":
                self.registers[x] %= yVal
            elif inst == "rcv":
                if self.inBuffer:
                    self.registers[x] = self.inBuffer.popleft()
                else:
                    self.blocked = True
                    break
            elif inst == "jgz":
                if xVal > 0:
                    self.pc += yVal - 1

            self.pc += 1

########################

code = AOCUtils.loadInput(18)

p0 = Program(code, 0)
p0.run()

print("Part 1: {}".format(p0.outBuffer[-1]))

p0 = Program(code, 0)
p1 = Program(code, 1)

p0.inBuffer = p1.outBuffer
p1.inBuffer = p0.outBuffer

while not (p0.blocked and not p0.outBuffer and p1.blocked and not p1.outBuffer):
    p0.run()
    p1.run()

print("Part 2: {}".format(p1.outCount))

AOCUtils.printTimeTaken()