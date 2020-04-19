####################################
# --- Day 19: Go With The Flow --- #
####################################

import AOCUtils

####################################

program = AOCUtils.loadInput(19)
pc, program = int(program[0].split()[1]), program[1:]

registers = [0 for _ in range(6)]
while registers[pc] < len(program):
    instr = program[registers[pc]].split()
    op = instr[0]
    a, b, c = [int(i) for i in instr[1:]]
    
    if op == "addr":
        registers[c] = registers[a] + registers[b]
    elif op == "addi":
        registers[c] = registers[a] + b
    elif op == "mulr":
        registers[c] = registers[a] * registers[b]
    elif op == "muli":
        registers[c] = registers[a] * b
    elif op == "borr":
        registers[c] = registers[a] | registers[b]
    elif op == "bori":
        registers[c] = registers[a] | b
    elif op == "banr":
        registers[c] = registers[a] & registers[b]
    elif op == "bani":
        registers[c] = registers[a] & b
    elif op == "setr":
        registers[c] = registers[a]
    elif op == "seti":
        registers[c] = a
    elif op == "gtir":
        registers[c] = int(a > registers[b])
    elif op == "gtri":
        registers[c] = int(registers[a] > b)
    elif op == "gtrr":
        registers[c] = int(registers[a] > registers[b])
    elif op == "eqir":
        registers[c] = int(a == registers[b])
    elif op == "eqri":
        registers[c] = int(registers[a] == b)
    elif op == "eqrr":
        registers[c] = int(registers[a] == registers[b])

    registers[pc] += 1

print("Part 1: {}".format(registers[0]))

args = [[int(i) for i in instr.split()[1:]] for instr in program]

x = (args[17][1] * args[17][1] * 19 * args[20][1]) + (args[21][1] * 22 + args[23][1])
y = (27 * 28 + 29) * 30 * args[31][1] * 32
magicValue = x + y

sumFactors = sum([i for i in range(1, magicValue+1) if magicValue % i == 0])
print("Part 2: {}".format(sumFactors))

AOCUtils.printTimeTaken()

'''
#ip 5
PC = F

PC = 0
A, B, C, D, E = 1, 0, 0, 0, 0

==================================

 0   addi 5 16 5  PC = 16       GOTO 17

 1   seti 1 9 1   B = 1         B = 1
 2   seti 1 5 4   E = 1         E = 1
 3   mulr 1 4 3   D = A * E     
 4   eqrr 3 2 3   D = (D == C)  if A == C:
 5   addr 3 5 5   PC += D           GOTO 7
 6   addi 5 1 5   PC = 7        else: GOTO 8

 7   addr 1 0 0   A += 1

 8   addi 4 1 4   E += 1
 9   gtrr 4 2 3   D = (E > C)
10   addr 5 3 5   PC = 10 * D
11   seti 2 4 5   PC = 2
12   addi 1 1 1   B = B + 1
13   gtrr 1 2 3   D = (B > C)
14   addr 3 5 5   PC += D
15   seti 1 9 5   PC = 1
16   mulr 5 5 5   PC = 256

17   addi 2 2 2   C += 2         C = 2
18   mulr 2 2 2   C *= C         C = 4
19   mulr 5 2 2   C *= 19        C = 76
20   muli 2 11 2  C *= 11        C = 836
21   addi 3 8 3   D += 8         D = 8
22   mulr 3 5 3   D *= 22        D = 176
23   addi 3 16 3  D += 16        D = 192
24   addr 2 3 2   C += D         C = 1028           x = ((2*2)*19*11 + (8*22)+16)
25   addr 5 0 5   PC += A        if part2: GOTO 27
26   seti 0 7 5   PC = 0         else: GOTO 1

27   setr 5 3 3   D = 27         D = 27
28   mulr 3 5 3   D *= 28        D = 756
29   addr 5 3 3   D += 29        D = 785
30   mulr 5 3 3   D *= 30        D = 23550
31   muli 3 14 3  D *= 14        D = 329700
32   mulr 3 5 3   D *= 32        D = 10550400       y = ((27*28+29)*30*14*32)
33   addr 2 3 2   C += D         C = 10551428       will get sum of factors of (x+y)
34   seti 0 1 0   A = 0          A = 0
35   seti 0 6 5   PC = 0         GOTO 1

'''