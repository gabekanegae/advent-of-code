######################################
# --- Day 21: Chronal Conversion --- #
######################################

import AOCUtils

def emulateCode(args):
    haltValues = []
    seen = set()
                                                              # 0-4 (self-test)
    regs = [0 for _ in range(6)]                              # 5 (seti)
    while True:
        regs[args[6][2]] = regs[args[6][0]] | args[6][1]      # 6 (bori)
        regs[args[7][2]] = args[7][0]                         # 7 (seti)
        while True:
            regs[args[8][2]] = regs[args[8][0]] & args[8][1]  # 8 (bani)
            regs[args[9][2]] += regs[args[9][1]]              # 9 (addr)
            regs[args[10][2]] &= args[10][1]                  # 10 (bani)
            regs[args[11][2]] *= args[11][1]                  # 11 (muli)
            regs[args[12][2]] &= args[12][1]                  # 12 (bani)

            magicValue = regs[args[28][0]]
            if (256 > regs[args[13][1]]):                     # 13 (gtir)
                if magicValue in seen:                        # 14,16,28,29 (would halt)
                    return haltValues
                else:
                    haltValues.append(magicValue)
                    seen.add(magicValue)
                break                                         # 30 (would not halt)

            regs[args[13][1]] //= 256                         # 18-25 (loop)

######################################

program = AOCUtils.loadInput(21)[1:]
args = [[int(i) for i in instr.split()[1:]] for instr in program]

haltValues = emulateCode(args)
print("Part 1: {}".format(haltValues[0]))
print("Part 2: {}".format(haltValues[-1]))

AOCUtils.printTimeTaken()

'''
#ip 4
PC = E

PC = 0
A, B, C, D, F = X, 0, 0, 0, 0

==================================

 0   seti 123 0 5       F = 123
 1   bani 5 456 5       F = F & 456
 2   eqri 5 72 5        F = (F == 72)    if 123 & 456 == 72: (self-test)
 3   addr 5 4 4         PC += F              GOTO 5
 4   seti 0 0 4         PC = 0           else: GOTO 1

 5   seti 0 9 5         F = 0            
 6   bori 5 65536 3     D = 65536        D = 65536
 7   seti 10828530 0 5  F = 10828530     F = 10828530
 8   bani 3 255 2       C = D & 255      C = 0
 9   addr 5 2 5         F += B           F += B
10   bani 5 16777215 5  F = F & 16777215 F &= 16777215
11   muli 5 65899 5     F *= 65899       F *= 65899
12   bani 5 16777215 5  F = F & 16777215 F &= 16777215
13   gtir 256 3 2       C = (256 > D)    if 256 > D:
14   addr 2 4 4         PC += C              GOTO 16
15   addi 4 1 4         PC += 1          else: GOTO 17

16   seti 27 4 4        PC = 27          GOTO 28

17   seti 0 4 2         C = 0            C = 0
18   addi 2 1 1         B += 1           B += 1
19   muli 1 256 1       B *= 256         B *= 256
20   gtrr 1 3 1         B = (B > D)      if B > D:
21   addr 1 4 4         PC += B              GOTO 23
22   addi 4 1 4         PC += 1          else: GOTO 24

23   seti 25 9 4        PC = 25          GOTO 26

24   addi 2 1 2         C += 1           C += 1
25   seti 17 9 4        PC = 17          GOTO 18
26   setr 2 8 3         D = C            D = C
27   seti 7 9 4         PC = 7           GOTO 8
28   eqrr 5 0 2         C = (F == X)     if (F == X):
29   addr 2 4 4         PC += C              halt
30   seti 5 5 4         PC = 5           else: GOTO 6
'''