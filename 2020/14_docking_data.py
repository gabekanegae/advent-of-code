################################
# --- Day 14: Docking Data --- #
################################

import AOCUtils

################################

program = AOCUtils.load_input(14)

mem = dict()
mask = None

for instruction in program:
    var, data = instruction.split(' = ')
    if var == 'mask':
        mask = data
    elif var.startswith('mem'):
        idx = var[4:-1]

        data = list(bin(int(data))[2:].zfill(36))
        for i, c in enumerate(mask):
            if c != 'X':
                data[i] = c
        data = int(''.join(data), 2)

        mem[idx] = data

AOCUtils.print_answer(1, sum(mem.values()))

mem = dict()
mask = None

for instruction in program:
    var, data = instruction.split(' = ')
    if var == 'mask':
        mask = data
    elif var.startswith('mem'):
        idx = var[4:-1]

        idx = list(bin(int(idx))[2:].zfill(36))
        for i, c in enumerate(mask):
            if c == '1':
                idx[i] = c

        floating = [i for i, c in enumerate(mask) if c == 'X']
        n = len(floating)
        for bits in range(2**n):
            bits = bin(bits)[2:].zfill(n)

            new_idx = idx[:]
            for i, b in zip(floating, bits):
                new_idx[i] = b

            new_idx = int(''.join(new_idx), 2)
            mem[new_idx] = int(data)

AOCUtils.print_answer(2, sum(mem.values()))

AOCUtils.print_time_taken()