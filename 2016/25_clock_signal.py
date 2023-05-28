################################
# --- Day 25: Clock Signal --- #
################################

import AOCUtils

class VM:
    def __init__(self, program):
        self.program = program[:]
        self.pc = 0
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

        self.last_output = 1
        self.output_length = 0
        self.loops = False

    def run(self):
        while self.pc < len(self.program):
            cmd = self.program[self.pc].split()

            inst = cmd[0]

            x = cmd[1]
            x_val = int(x) if not x.isalpha() else self.registers[x]
            if len(cmd) > 2:
                y = cmd[2]
                y_val = int(y) if not y.isalpha() else self.registers[y]

            if inst == 'cpy':
                self.registers[y] = x_val
            elif inst == 'inc':
                self.registers[x] += 1
            elif inst == 'dec':
                self.registers[x] -= 1
            elif inst == 'jnz':
                if x_val != 0:
                    self.pc += y_val - 1
            elif inst == 'out':
                if x_val == self.last_output:
                    break

                self.last_output = x_val
                self.output_length += 1

                # Assume that the clock loops forever if it keeps oscillating after 100 cycles
                if self.output_length > 100:
                    self.loops = True
                    break

            self.pc += 1

################################

program = AOCUtils.load_input(25)

# i = 0
# while True:
#     vm = VM(program)
#     vm.registers['a'] = i
#     vm.run()

#     if vm.loops:
#         AOCUtils.print_answer(1, i))
#         break

#     i += 1

X = int(program[1].split()[1])
Y = int(program[2].split()[1])

n = 1
while True:
    repeat = int('10'*n, 2)
    if repeat > X * Y: break
    n += 1

a = repeat - X * Y
AOCUtils.print_answer(1, a)

AOCUtils.print_time_taken()

# Part 1: Smallest a such that a + x*y = 0b10...10

'''
    |           | <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< | while True:                  | loop forever:
  0 | cpy a d   | d = a                        ^ |   d = a                      |
  1 | cpy 7 c   | c = 7                        ^ |                              |
    |           |                              ^ |                              |
  2 | cpy 362 b | b = 362 <<<<<<<<<<<<<        ^ |   d += 362 * 7               |
  3 | inc d     | d += 1 <<<<<<<<<<<  ^        ^ |                              |
  4 | dec b     | b -= 1           ^  ^        ^ |                              |
  5 | jnz b -2  | while b != 0: >>>>  ^        ^ |                              |
  6 | dec c     | c -= 1              ^        ^ |                              |
  7 | jnz c -5  | while c != 0: >>>>>>>        ^ |                              |
    |           |                              ^ |                              |
  8 | cpy d a   | a = d                        ^ |   a = d                      |   a = a + 362 * 7
    |           |                              ^ |                              |
  9 | jnz 0 0   | <<<<<<<<<<<<<<<<<<<<<<<<<<<  ^ |   while a != 0:              |   while a != 0:
 10 | cpy a b   | b = a                     ^  ^ |     b = a                    |    
 11 | cpy 0 a   | a = 0                     ^  ^ |     a = 0                    |    
 12 | cpy 2 c   | c = 2 <<<<<<<<<<<<<<<     ^  ^ |     c = 2                    |    
 13 | jnz b 2   | if b != 0: >>>> <<  ^     ^  ^ |     while b != 0 and c != 0: |    
 14 | jnz 1 6   | >>>>>>>>>>>>. v  ^  ^ .v  ^  ^ |                              |    
 15 | dec b     | b -= 1 <<<<<<<<  ^  ^  v  ^  ^ |       b -= 1                 |    
 16 | dec c     | c -= 1           ^  ^  v  ^  ^ |       c -= 1                 |    
 17 | jnz c -4  | while c != 0: >>>>  ^  v  ^  ^ |                              |    
 18 | inc a     | a += 1              ^  v  ^  ^ |     a += 1                   |     a = b // 2
 19 | jnz 1 -7  | >>>>>>>>>>>>>>>>>>>>>  v  ^  ^ |                              |     c = 2 - (a % 2)
 20 | cpy 2 b   | <<<<<<<<<<<<<<<<<<<<<<<<  ^  ^ |                              |    
    |           |                           ^  ^ |                              |    
 21 | jnz c 2   | if c != 0: >>>>>>>v <<    ^  ^ |   while c != 0:              |     b = 2 - c = a % 2
 22 | jnz 1 4   | >>>>>>>>>>>>>>>>  v  ^    ^  ^ |                              |
 23 | dec b     | b -= 1 <<<<<<. v .v  ^    ^  ^ |     b -= 1                   |
 24 | dec c     | c -= 1         v     ^    ^  ^ |     c -= 1                   |
 25 | jnz 1 -4  | >>>>>>>>>>>>>. v .>>>>    ^  ^ |                              |
 26 | jnz 0 0   | <<<<<<<<<<<<<<<<          ^  ^ |                              |
    |           |                           ^  ^ |                              |
 27 | out b     | out b                     ^  ^ |   out b                      |     print(b)
 28 | jnz a -19 | if a != 0: >>>>>>>>>>>>>>>>  ^ |                              |
 29 | jnz 1 -21 | >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |                              |
'''