#################################
# --- Day 23: Safe Cracking --- #
#################################

import AOCUtils
from math import factorial

class VM:
    def __init__(self, program):
        self.program = program[:]
        self.pc = 0
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

        self.toggled = set()
        self.toggledProgram = [cmd.split() for cmd in program]
        for i in range(len(self.toggledProgram)):
            if len(self.toggledProgram[i]) == 2: # one-argument instruction
                if self.toggledProgram[i][0] == 'inc':
                    self.toggledProgram[i][0] = 'dec'
                else:
                    self.toggledProgram[i][0] = 'inc'
            else: # two-argument instruction
                if self.toggledProgram[i][0] == 'jnz':
                    self.toggledProgram[i][0] = 'cpy'
                else:
                    self.toggledProgram[i][0] = 'jnz'
        self.toggledProgram = [' '.join(cmd) for cmd in self.toggledProgram]

    def run(self):
        while self.pc < len(self.program):
            if self.pc in self.toggled:
                cmd = self.toggledProgram[self.pc].split()
            else:
                cmd = self.program[self.pc].split()

            inst = cmd[0]

            x = cmd[1]
            xVal = int(x) if not x.isalpha() else self.registers[x]
            if len(cmd) > 2:
                y = cmd[2]
                yVal = int(y) if not y.isalpha() else self.registers[y]

            if inst == 'cpy':
                if y.isalpha():
                    self.registers[y] = xVal
            elif inst == 'inc':
                if x.isalpha():
                    self.registers[x] += 1
            elif inst == 'dec':
                if x.isalpha():
                    self.registers[x] -= 1
            elif inst == 'jnz':
                if xVal != 0:
                    self.pc += yVal - 1
            elif inst == 'tgl':
                n = self.pc + xVal
                if 0 <= n < len(self.program):
                    if n in self.toggled:
                        self.toggled.remove(n)
                    else:
                        self.toggled.add(n)

            self.pc += 1

#################################

program = AOCUtils.load_input(23)

# vm = VM(program)
# vm.registers['a'] = 7
# vm.run()
# AOCUtils.print_answer(1, vm.registers['a']))

# vm = VM(program)
# vm.registers['a'] = 12
# vm.run()
# AOCUtils.print_answer(2, vm.registers['a']))

X = int(program[19].split()[1])
Y = int(program[20].split()[1])

a = factorial(7) + X * Y
AOCUtils.print_answer(1, a)

a = factorial(12) + X * Y
AOCUtils.print_answer(2, a)

AOCUtils.print_time_taken()

'''
  0 | cpy a b   | jnz a b   | b = 12                    |               |
  1 | dec b     | inc b     | b -= 1                    | b -= 1        |
  2 | cpy a d   | jnz a d   | d = b <<<<<<<<<<<<<<<<<<< | d = b         | d = 11*12, 10*11*12, ...
  3 | cpy 0 a   | jnz 0 a   | a = 0                  ^  | a = 0         |
  4 | cpy b c   | jnz b c   | c = b <<<<<<<<<<<<<<<  ^  | c = b         | c = 11, 10, 9, ...
    |           |           |                     ^  ^  |               |
  5 | inc a     | dec a     | a += 1 <<<<<<<<<<<  ^  ^  | a += c * d    | 11*12, 10*11*12, 9*10*11*12, ...
  6 | dec c     | inc c     | c -= 1           ^  ^  ^  |               |
  7 | jnz c -2  | cpy c -2  | while c != 0: >>>>  ^  ^  |               |
    |           |           |                     ^  ^  |               |
  8 | dec d     | inc d     | d -= 1              ^  ^  |               |
  9 | jnz d -5  | cpy d -5  | while d != 0: >>>>>>>  ^  |               |
    |           |           |                        ^  |               |
 10 | dec b     | inc b     | b -= 1                 ^  | b -= 1        | b = 10, 9, 8, ...
 11 | cpy b c   | jnz b c   | c = b                  ^  |               |
 12 | cpy c d   | jnz c d   | d = b                  ^  |               |
    |           |           |                        ^  |               |
 13 | dec d     | inc d     | d -= 1 <<<<<<<<<<<     ^  | c = 2*b       | c = 20, 18, 16, ...
 14 | inc c     | dec c     | c += 1           ^     ^  |               |
 15 | jnz d -2  | cpy d -2  | while d != 0: >>>>     ^  |               |
    |           |           |                        ^  |               |
 16 | tgl c     | inc c     | tgl c                  ^  | tgld | c += 1 | toggles all inst below on even offsets 
 17 | cpy -16 c | jnz -16 c | c = -16                ^  | c = -16       |
    |           |           |                        ^  |               |
 18 | jnz 1 c   | cpy 1 c   | >>>>.. / c = 1 ..>>>>>>>  | tgld          |
    |           |           |                           |               
    |           |           |                           | After calculating a!, c becomes 0 and inst 16
    |           |           |                           | toggles itself, thus exiting the loop and
    |           |           |                           | running the (modified/toggled) code below
    |           |           |                           |  
 19 | cpy 75 c  | jnz 75 c  | c = 75                    | c = 75        | c = 75
    |           |           |                           |               |
 20 | jnz 97 d  | cpy 97 d  | >>...? / d = 97 <<<<<     | tgld          | d = 97
    |           |           |                     ^     |               |
 21 | inc a     | dec a     | a += 1 <<<<<<<<<<<  ^     |               | a += c * d
 22 | inc d     | dec d     | d += 1 / d -= 1  ^  ^     | tgld          |
 23 | jnz d -2  | cpy d -2  | while d != 0: >>>>  ^     |               |
    |           |           |                     ^     |               |
 24 | inc c     | dec c     | c += 1 / c -= 1     ^     | tgld          |
 25 | jnz c -5  | cpy c -5  | while c != 0: >>>>>>>     |               |
'''