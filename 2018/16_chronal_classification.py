##########################################
# --- Day 16: Chronal Classification --- #
##########################################

import AOCUtils

##########################################

raw_data = AOCUtils.load_input(16)
data = [s for s in raw_data if s]

split = 0
while data[split+2].startswith('After:'):
    split += 3

program = [list(map(int, s.split())) for s in data[split:]]

samples = []
for x in range(0, split, 3):
    b = list(map(int, str(data[x].split(': ')[1][1:-1]).split(', ')))
    i = list(map(int, data[x+1].split()))
    a = list(map(int, str(data[x+2].split(':  ')[1][1:-1]).split(', ')))
    
    samples.append((b, i, a))

# Record instruction possibilities for each opcode
possible_instructions = [set() for i in range(16)]
many_instructions_sample_count = 0
for sample in samples:
    mem_1, mem_2 = sample[0], sample[2]
    opcode, a, b, c = sample[1]

    possibilities = set()

    if mem_2[c] == mem_1[a] + mem_1[b]: possibilities.add('addr')
    if mem_2[c] == mem_1[a] + b: possibilities.add('addi')

    if mem_2[c] == mem_1[a] * mem_1[b]: possibilities.add('mulr')
    if mem_2[c] == mem_1[a] * b: possibilities.add('muli')

    if mem_2[c] == mem_1[a] | mem_1[b]: possibilities.add('borr')
    if mem_2[c] == mem_1[a] | b: possibilities.add('bori')

    if mem_2[c] == mem_1[a] & mem_1[b]: possibilities.add('banr')
    if mem_2[c] == mem_1[a] & b: possibilities.add('bani')

    if mem_2[c] == mem_1[a]: possibilities.add('setr')
    if mem_2[c] == a: possibilities.add('seti')

    if mem_2[c] == int(a > mem_1[b]): possibilities.add('gtir')
    if mem_2[c] == int(mem_1[a] > b): possibilities.add('gtri')
    if mem_2[c] == int(mem_1[a] > mem_1[b]): possibilities.add('gtrr')

    if mem_2[c] == int(a == mem_1[b]): possibilities.add('eqir')
    if mem_2[c] == int(mem_1[a] == b): possibilities.add('eqri')
    if mem_2[c] == int(mem_1[a] == mem_1[b]): possibilities.add('eqrr')

    if len(possibilities) >= 3: many_instructions_sample_count += 1

    if len(possible_instructions[opcode]) == 0:
        possible_instructions[opcode] = possibilities
    else:
        possible_instructions[opcode] = possible_instructions[opcode].intersection(possibilities)

AOCUtils.print_answer(1, many_instructions_sample_count)

# Keep eliminating possibilities until there's only one for each opcode
opcodes = dict()
while len(opcodes) < 16:
    for op, code in enumerate(possible_instructions):
        if len(code) == 1:
            code = list(code)[0]
            opcodes[code] = op
            for p in possible_instructions:
                if code in p: p.remove(code)

registers = [0 for _ in range(4)]
pc = 0
while pc < len(program):
    opcode, a, b, c = program[pc]
    
    if opcode == opcodes['addr']:
        registers[c] = registers[a] + registers[b]
    elif opcode == opcodes['addi']:
        registers[c] = registers[a] + b
    elif opcode == opcodes['mulr']:
        registers[c] = registers[a] * registers[b]
    elif opcode == opcodes['muli']:
        registers[c] = registers[a] * b
    elif opcode == opcodes['borr']:
        registers[c] = registers[a] | registers[b]
    elif opcode == opcodes['bori']:
        registers[c] = registers[a] | b
    elif opcode == opcodes['banr']:
        registers[c] = registers[a] & registers[b]
    elif opcode == opcodes['bani']:
        registers[c] = registers[a] & b
    elif opcode == opcodes['setr']:
        registers[c] = registers[a]
    elif opcode == opcodes['seti']:
        registers[c] = a
    elif opcode == opcodes['gtir']:
        registers[c] = int(a > registers[b])
    elif opcode == opcodes['gtri']:
        registers[c] = int(registers[a] > b)
    elif opcode == opcodes['gtrr']:
        registers[c] = int(registers[a] > registers[b])
    elif opcode == opcodes['eqir']:
        registers[c] = int(a == registers[b])
    elif opcode == opcodes['eqri']:
        registers[c] = int(registers[a] == b)
    elif opcode == opcodes['eqrr']:
        registers[c] = int(registers[a] == registers[b])

    pc += 1

AOCUtils.print_answer(2, registers[0])

AOCUtils.print_time_taken()