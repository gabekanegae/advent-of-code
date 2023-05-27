##########################################
# --- Day 16: Chronal Classification --- #
##########################################

import AOCUtils

##########################################

rawInput = [s for s in AOCUtils.loadInput(16) if s]

split = 0
while rawInput[split+2].startswith("After:"): split += 3

program = [[int(i) for i in s.split()] for s in rawInput[split:]]

samples = []
for x in range(0, split, 3):
    b, i, a = rawInput[x].split(": ")[1], rawInput[x+1], rawInput[x+2].split(":  ")[1]
    b = [int(s) for s in str(b[1:-1]).split(", ")]
    i = [int(s) for s in i.split()]
    a = [int(s) for s in str(a[1:-1]).split(", ")]
    
    samples.append((b, i, a))

# Record instruction possibilities for each opcode
possibleInstr = [set() for i in range(16)]
manyInstrSampleCount = 0
for sample in samples:
    mem1, mem2 = sample[0], sample[2]
    opcode, a, b, c = sample[1]

    possibilities = set()

    if mem2[c] == mem1[a] + mem1[b]: possibilities.add("addr")
    if mem2[c] == mem1[a] + b: possibilities.add("addi")

    if mem2[c] == mem1[a] * mem1[b]: possibilities.add("mulr")
    if mem2[c] == mem1[a] * b: possibilities.add("muli")

    if mem2[c] == mem1[a] | mem1[b]: possibilities.add("borr")
    if mem2[c] == mem1[a] | b: possibilities.add("bori")

    if mem2[c] == mem1[a] & mem1[b]: possibilities.add("banr")
    if mem2[c] == mem1[a] & b: possibilities.add("bani")

    if mem2[c] == mem1[a]: possibilities.add("setr")
    if mem2[c] == a: possibilities.add("seti")

    if mem2[c] == int(a > mem1[b]): possibilities.add("gtir")
    if mem2[c] == int(mem1[a] > b): possibilities.add("gtri")
    if mem2[c] == int(mem1[a] > mem1[b]): possibilities.add("gtrr")

    if mem2[c] == int(a == mem1[b]): possibilities.add("eqir")
    if mem2[c] == int(mem1[a] == b): possibilities.add("eqri")
    if mem2[c] == int(mem1[a] == mem1[b]): possibilities.add("eqrr")

    if len(possibilities) >= 3: manyInstrSampleCount += 1

    if len(possibleInstr[opcode]) == 0:
        possibleInstr[opcode] = possibilities
    else:
        possibleInstr[opcode] = possibleInstr[opcode].intersection(possibilities)

print("Part 1: {}".format(manyInstrSampleCount))

# Keep eliminating possibilities until there's only one for each opcode
opcodes = dict()
while len(opcodes) < 16:
    for op, code in enumerate(possibleInstr):
        if len(code) == 1:
            code = list(code)[0]
            opcodes[code] = op
            for p in possibleInstr:
                if code in p: p.remove(code)

registers = [0 for _ in range(4)]
pc = 0
while pc < len(program):
    opcode, a, b, c = program[pc]
    
    if opcode == opcodes["addr"]:
        registers[c] = registers[a] + registers[b]
    elif opcode == opcodes["addi"]:
        registers[c] = registers[a] + b
    elif opcode == opcodes["mulr"]:
        registers[c] = registers[a] * registers[b]
    elif opcode == opcodes["muli"]:
        registers[c] = registers[a] * b
    elif opcode == opcodes["borr"]:
        registers[c] = registers[a] | registers[b]
    elif opcode == opcodes["bori"]:
        registers[c] = registers[a] | b
    elif opcode == opcodes["banr"]:
        registers[c] = registers[a] & registers[b]
    elif opcode == opcodes["bani"]:
        registers[c] = registers[a] & b
    elif opcode == opcodes["setr"]:
        registers[c] = registers[a]
    elif opcode == opcodes["seti"]:
        registers[c] = a
    elif opcode == opcodes["gtir"]:
        registers[c] = int(a > registers[b])
    elif opcode == opcodes["gtri"]:
        registers[c] = int(registers[a] > b)
    elif opcode == opcodes["gtrr"]:
        registers[c] = int(registers[a] > registers[b])
    elif opcode == opcodes["eqir"]:
        registers[c] = int(a == registers[b])
    elif opcode == opcodes["eqri"]:
        registers[c] = int(registers[a] == b)
    elif opcode == opcodes["eqrr"]:
        registers[c] = int(registers[a] == registers[b])

    pc += 1

print("Part 2: {}".format(registers[0]))

AOCUtils.printTimeTaken()