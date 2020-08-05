#######################################
# --- Day 12: Leonardo's Monorail --- #
#######################################

import AOCUtils

class VM:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.registers = dict()

    def run(self):
        while self.pc < len(self.program):
            if self.pc == 15: print(self.registers)
            cmd = self.program[self.pc].split()

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

            if inst == "cpy":
                self.registers[y] = xVal
            elif inst == "inc":
                self.registers[x] += 1
            elif inst == "dec":
                self.registers[x] -= 1
            elif inst == "jnz":
                if xVal != 0:
                    self.pc += yVal - 1

            self.pc += 1

#######################################

program = AOCUtils.loadInput(12)

# vm = VM(program)
# vm.run()
# print("Part 1: {}".format(vm.registers["a"]))

# vm = VM(program)
# vm.registers["c"] = 1
# vm.run()
# print("Part 2: {}".format(vm.registers))

D = int(program[2].split()[1])
C = int(program[5].split()[1])

X = int(program[16].split()[1])
Y = int(program[17].split()[1])

a, b, c, d = 1, 1, C, D
for _ in range(d):
    c = a
    a += b
    b = c
a += X * Y
print("Part 1: {}".format(a))

a, b, c, d = 1, 1, C, D
d += c
for _ in range(d):
    c = a
    a += b
    b = c
a += X * Y
print("Part 2: {}".format(a))

AOCUtils.printTimeTaken()

# Part 1: (2+d)th fibonacci number + (x+y)
# Part 2: (2+c+d)th fibonacci number + (x+y)
# (fibonacci indexing being 0th=0, 1st=1, 2nd=1, 3rd=2...)

'''
  0 | cpy 1 a  | a = 1                  | a = 1
  1 | cpy 1 b  | b = 1                  | b = 1
  2 | cpy 26 d | d = 26                 | d = 26
    |          |                        |
  3 | jnz c 2  | if c != 0:             |
  4 | jnz 1 5  |                        |
  5 | cpy 7 c  |   c = 7                | c = 7
    |          |                        |
  6 | inc d    | d += 1 <<<<<<<<<<<     | d += c
  7 | dec c    | c -= 1           ^     |
  8 | jnz c -2 | while c != 0: >>>>     |
    |          |                        | loop d times:
  9 | cpy a c  | c = a <<<<<<<<<<<<<<<  |     c = a
    |          |                     ^  | 
 10 | inc a    | a += 1 <<<<<<<<<<<  ^  |     a += b
 11 | dec b    | b -= 1           ^  ^  |
 12 | jnz b -2 | while b != 0: >>>>  ^  |
    |          |                     ^  |
 13 | cpy c b  | b = c               ^  |     b = c
 14 | dec d    | d -= 1              ^  |
    |          |                     ^  |
 15 | jnz d -6 | while d != 0: >>>>>>>  |
    |          |                        |
 16 | cpy 17 c | c = 17                 | c = 17
    |          |                        |
 17 | cpy 18 d | d = 18 <<<<<<<<<<<<<<  |
    |          |                     ^  |
 18 | inc a    | a += 1 <<<<<<<<<<<  ^  | a += 18 * c
 19 | dec d    | d -= 1           ^  ^  |
 20 | jnz d -2 | while d != 0: >>>>  ^  |
    |          |                     ^  |
 21 | dec c    | c -= 1              ^  |
 22 | jnz c -5 | while c != 0: >>>>>>>  |
'''